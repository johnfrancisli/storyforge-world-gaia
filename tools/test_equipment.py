#!/usr/bin/env python3
"""Focused tests for Gaia's equipment-domain rules."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from equipment import (
    empty_equipment,
    equip_held_item,
    equip_wearable,
    equipment_modifiers,
    unequip_held_item,
    validate_character_equipment,
)
from migrate_equipment import clothing_assignment, item_metadata, special_assignment


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


def test_full_body_layers_can_overlap():
    regions = ["torso", "left_arm", "right_arm", "left_leg", "right_leg"]
    items = {
        item["id"]: item for item in (
            wearable("item:body-shift", "underwear", regions),
            wearable("item:dress", "clothing", regions),
            wearable("item:full-plate", "armor", regions),
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


def test_dual_wield_distinct_item_instances():
    iron = held("item:iron-dagger")
    steel = held("item:steel-dagger")
    items = {item["id"]: item for item in (iron, steel)}
    current = equip_held_item(character(), iron, items, "left")
    current = equip_held_item(current, steel, items, "right")
    assert validate_character_equipment(current, items) == []


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


def test_migration_maps_supported_character_clothing():
    sora = {
        "id": "character:akiyama-sora", "gender": "Female",
        "heritage": "Tsukuyomi",
        "appearance": "Sora wears a plum work kimono with sleeves tied back.",
    }
    assert clothing_assignment(sora) == ["item:hemp-work-kosode"]
    shrine_worker = {
        "id": "character:shrine-worker", "gender": "Female",
        "heritage": "Tsukuyomi",
        "appearance": "A woman in shrine robes, white top and red hakama pants.",
    }
    assert clothing_assignment(shrine_worker) == [
        "item:shrine-maiden-kosode", "item:shrine-maiden-hakama"
    ]


def test_migration_does_not_invent_missing_armor():
    knight = {
        "id": "character:knight", "gender": "Male", "heritage": "Valdris",
        "appearance": "A knight in worn plate armor with an ordinary sword.",
    }
    assert clothing_assignment(knight) == []
    assert special_assignment(knight) == ([], [])


def test_migration_classifies_underwear_and_two_handed_items():
    underwear = {
        "id": "item:test-underwear", "name": "Test Undershirt",
        "item_type": "clothing", "is_equippable": True, "slot": "chest",
        "item_tags": ["underwear"], "appearance": "A long-sleeved undershirt.",
    }
    assert item_metadata(underwear)["layer"] == "underwear"
    weapon = {
        "id": "item:test-weapon", "name": "Test Weapon",
        "item_type": "weapon", "is_equippable": True, "slot": "two_hand",
        "item_tags": ["weapon"], "appearance": "A long weapon.",
    }
    metadata = item_metadata(weapon)
    assert metadata["equipment_type"] == "weapon"
    assert metadata["hands_required"] == 2


def test_training_requirements_and_duplicate_references():
    plate = wearable(
        "item:plate", "armor", ["torso"],
        requirements={"armor_training": "heavy"},
    )
    items = {plate["id"]: plate}
    untrained = character()
    untrained["equipment"]["armor"] = ["item:plate", "item:plate"]
    errors = validate_character_equipment(untrained, items)
    assert any("duplicate" in error for error in errors)
    assert any("heavy" in error for error in errors)
    trained = character()
    trained["armor_training"] = {"heavy": 1}
    trained = equip_wearable(trained, plate, items)
    assert validate_character_equipment(trained, items) == []


def test_ammunition_compatibility():
    bow = held("item:bow", 2, ammo_types=["arrow"])
    arrow = {
        "id": "item:arrow", "name": "Arrow", "is_equippable": True,
        "equipment_type": "ammunition", "ammo_type": "arrow",
    }
    stone = {
        "id": "item:stone", "name": "Sling Stone", "is_equippable": True,
        "equipment_type": "ammunition", "ammo_type": "sling_stone",
    }
    items = {item["id"]: item for item in (bow, arrow, stone)}
    current = equip_held_item(character(), bow, items)
    current["equipment"]["ammo"] = {"item": "item:arrow", "quantity": 18}
    assert validate_character_equipment(current, items) == []
    current["equipment"]["ammo"] = {"item": "item:stone", "quantity": 18}
    assert any("incompatible" in error for error in validate_character_equipment(current, items))


def main():
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS: {test.__name__}")
    print(f"Results: {len(tests)} passed, 0 failed")


if __name__ == "__main__":
    main()
