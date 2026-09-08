#!/usr/bin/env python3
"""Focused tests for Gaia's equipment-domain rules."""

from equipment import (
    empty_equipment,
    equip_held_item,
    equip_wearable,
    equipment_modifiers,
    unequip_held_item,
    validate_character_equipment,
)


def wearable(item_id, layer, coverage, **extra):
    return {
        "id": item_id, "name": item_id, "is_equippable": True,
        "equipment_type": "wearable", "layer": layer, "coverage": coverage,
        **extra,
    }


def held(item_id, hands=1, **extra):
    return {
        "id": item_id, "name": item_id, "is_equippable": True,
        "equipment_type": "weapon", "hands_required": hands,
        "allowed_hands": ["left", "right"], **extra,
    }


def character():
    return {"id": "character:test", "equipment": empty_equipment()}


def test_three_layers_can_overlap():
    items = {
        item["id"]: item for item in (
            wearable("item:undershirt", "underwear", ["torso"]),
            wearable("item:tunic", "clothing", ["torso"]),
            wearable("item:breastplate", "armor", ["torso"]),
        )
    }
    current = character()
    for item in items.values():
        current = equip_wearable(current, item, items)
    assert validate_character_equipment(current, items) == []


def test_same_layer_conflict():
    iron = wearable("item:iron-plate", "armor", ["torso"])
    steel = wearable("item:steel-plate", "armor", ["torso"])
    items = {item["id"]: item for item in (iron, steel)}
    current = equip_wearable(character(), iron, items)
    try:
        equip_wearable(current, steel, items)
    except ValueError as exc:
        assert "torso" in str(exc) and "armor" in str(exc)
    else:
        raise AssertionError("second breastplate should conflict")


def test_dress_conflicts_with_trousers():
    dress = wearable(
        "item:dress", "clothing",
        ["torso", "left_arm", "right_arm", "left_leg", "right_leg"],
    )
    trousers = wearable("item:trousers", "clothing", ["left_leg", "right_leg"])
    items = {item["id"]: item for item in (dress, trousers)}
    current = equip_wearable(character(), dress, items)
    try:
        equip_wearable(current, trousers, items)
    except ValueError:
        pass
    else:
        raise AssertionError("dress and trousers should conflict")


def test_asymmetric_armor_and_gauntlet_with_sword():
    left = wearable("item:left-pauldron", "armor", ["left_arm"])
    right = wearable("item:right-pauldron", "armor", ["right_arm"])
    gauntlet = wearable("item:gauntlet", "armor", ["right_hand"])
    sword = held("item:sword")
    items = {item["id"]: item for item in (left, right, gauntlet, sword)}
    current = character()
    for item in (left, right, gauntlet):
        current = equip_wearable(current, item, items)
    current = equip_held_item(current, sword, items, "right")
    assert validate_character_equipment(current, items) == []


def test_sword_shield_and_two_handed_conflict():
    sword = held("item:sword")
    shield = {**held("item:shield"), "equipment_type": "shield"}
    greatsword = held("item:greatsword", 2)
    items = {item["id"]: item for item in (sword, shield, greatsword)}
    current = equip_held_item(character(), shield, items, "left")
    current = equip_held_item(current, sword, items, "right")
    try:
        equip_held_item(current, greatsword, items)
    except ValueError as exc:
        assert "both" in str(exc) or "left, right" in str(exc)
    else:
        raise AssertionError("greatsword should require two empty hands")


def test_two_handed_unequip_and_modifier_deduplication():
    greatsword = held("item:greatsword", 2, modifiers={"attack": 5})
    items = {greatsword["id"]: greatsword}
    current = equip_held_item(character(), greatsword, items)
    assert current["equipment"]["hands"] == {
        "left": "item:greatsword", "right": "item:greatsword"
    }
    assert equipment_modifiers(current, items) == {"attack": 5}
    current = unequip_held_item(current, "item:greatsword")
    assert current["equipment"]["hands"] == {"left": None, "right": None}


def test_overlay_can_share_layer():
    robe = wearable("item:robe", "clothing", ["torso", "left_arm", "right_arm"])
    coat = wearable(
        "item:coat", "clothing", ["torso", "left_arm", "right_arm"],
        stacking={"mode": "overlay"},
    )
    items = {item["id"]: item for item in (robe, coat)}
    current = equip_wearable(character(), robe, items)
    current = equip_wearable(current, coat, items)
    assert validate_character_equipment(current, items) == []


def main():
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS: {test.__name__}")
    print(f"Results: {len(tests)} passed, 0 failed")


if __name__ == "__main__":
    main()
