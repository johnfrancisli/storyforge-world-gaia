#!/usr/bin/env python3
"""Shared equipment-domain rules for Gaia's record data."""

from copy import deepcopy
from numbers import Real

WEARABLE_LAYERS = {"underwear", "clothing", "armor"}
BODY_REGIONS = {
    "head", "torso", "left_arm", "right_arm", "left_hand", "right_hand",
    "waist", "left_leg", "right_leg", "left_foot", "right_foot",
}
HAND_NAMES = {"left", "right"}
EQUIPMENT_TYPES = {"wearable", "weapon", "shield", "held", "accessory", "ammunition"}
STACKING_MODES = {"exclusive", "overlay", "stackable"}


def empty_equipment():
    return {
        "underwear": [], "clothing": [], "armor": [],
        "hands": {"left": None, "right": None},
        "accessories": [], "ammo": None,
    }


def stacking_mode(item):
    return (item.get("stacking") or {}).get("mode", "exclusive")


def hands_required(item):
    value = item.get("hands_required")
    if isinstance(value, int):
        return value, value
    if isinstance(value, dict):
        return value.get("minimum"), value.get("maximum")
    return None, None


def overlap_allowed(first, second):
    modes = {stacking_mode(first), stacking_mode(second)}
    return "overlay" in modes or modes == {"stackable"}


def requirement_errors(character, item):
    errors = []
    for field in ("armor_training", "weapon_training"):
        required = (item.get("requirements") or {}).get(field)
        if required is None:
            continue
        trained = character.get(field) or {}
        needs = {required: 1} if isinstance(required, str) else required
        if not isinstance(needs, dict):
            errors.append(f"{item.get('id')}: {field} requirement must be a string or mapping.")
            continue
        for category, minimum in needs.items():
            if not isinstance(trained, dict) or trained.get(category, 0) < minimum:
                errors.append(
                    f"{item.get('name', item.get('id'))} requires "
                    f"{field.replace('_', ' ')} {category} {minimum}."
                )
    return errors


def validate_item_definition(item):
    """Return human-readable errors for one canonical item definition."""
    errors = []
    item_id = item.get("id", "<missing item id>")
    if "slot" in item:
        errors.append(f"{item_id}: obsolete slot field remains.")
    if not item.get("is_equippable", False):
        return errors

    kind = item.get("equipment_type")
    if kind not in EQUIPMENT_TYPES:
        return [f"{item_id}: invalid or missing equipment_type {kind!r}."]
    modifiers = item.get("modifiers")
    if modifiers is not None and (
        not isinstance(modifiers, dict)
        or any(not isinstance(key, str) or not isinstance(value, Real)
               for key, value in modifiers.items())
    ):
        errors.append(f"{item_id}: modifiers must map stat names to numbers.")

    if kind == "wearable":
        if item.get("layer") not in WEARABLE_LAYERS:
            errors.append(f"{item_id}: invalid or missing wearable layer.")
        coverage = item.get("coverage")
        if not isinstance(coverage, list) or not coverage:
            errors.append(f"{item_id}: wearable coverage must be a non-empty array.")
        elif set(coverage) - BODY_REGIONS:
            errors.append(f"{item_id}: invalid coverage regions: {sorted(set(coverage) - BODY_REGIONS)}.")
        elif len(coverage) != len(set(coverage)):
            errors.append(f"{item_id}: duplicate coverage regions.")
        stacking = item.get("stacking") or {"mode": "exclusive"}
        if not isinstance(stacking, dict) or stacking.get("mode", "exclusive") not in STACKING_MODES:
            errors.append(f"{item_id}: invalid stacking mode.")
        elif stacking.get("mode") == "stackable":
            if not isinstance(stacking.get("max"), int) or stacking["max"] < 2:
                errors.append(f"{item_id}: stackable items require stacking.max >= 2.")
    elif kind in {"weapon", "shield", "held"}:
        minimum, maximum = hands_required(item)
        if minimum not in {1, 2} or maximum not in {1, 2} or minimum > maximum:
            errors.append(f"{item_id}: invalid hands_required.")
        allowed = item.get("allowed_hands")
        if allowed is not None and (
            not isinstance(allowed, list) or not allowed or set(allowed) - HAND_NAMES
        ):
            errors.append(f"{item_id}: allowed_hands must contain left/right.")
    elif kind == "accessory":
        if not isinstance(item.get("accessory_slot"), str) or not item["accessory_slot"]:
            errors.append(f"{item_id}: accessories require accessory_slot.")
    elif kind == "ammunition":
        if not isinstance(item.get("ammo_type"), str) or not item["ammo_type"]:
            errors.append(f"{item_id}: ammunition requires ammo_type.")
    return errors


def resolve(item_ref, item_index, context, errors):
    if not isinstance(item_ref, str):
        errors.append(f"{context} must contain a raw stable item ID.")
        return None
    item = item_index.get(item_ref)
    if item is None:
        errors.append(f"{context} references missing item {item_ref}.")
    return item


def validate_character_equipment(character, item_index):
    """Validate equipped references against canonical item metadata."""
    errors = []
    char_id = character.get("id", "<missing character id>")
    equipment = character.get("equipment")
    if not isinstance(equipment, dict):
        return [f"{char_id}: equipment must be a mapping."]

    for field in ("underwear", "clothing", "armor", "accessories"):
        if not isinstance(equipment.get(field), list):
            errors.append(f"{char_id}: equipment.{field} must be an array.")
    hands = equipment.get("hands")
    if not isinstance(hands, dict) or set(hands) != HAND_NAMES:
        errors.append(f"{char_id}: equipment.hands must contain exactly left and right.")
        hands = {"left": None, "right": None}

    for layer in sorted(WEARABLE_LAYERS):
        refs = equipment.get(layer)
        if not isinstance(refs, list):
            continue
        if len(refs) != len(set(refs)):
            errors.append(f"{char_id}: equipment.{layer} contains duplicate references.")
        items = []
        for item_ref in refs:
            item = resolve(item_ref, item_index, f"{char_id} equipment.{layer}", errors)
            if not item:
                continue
            if item.get("equipment_type") != "wearable" or item.get("layer") != layer:
                errors.append(f"{char_id}: {item_ref} is incompatible with equipment.{layer}.")
                continue
            errors.extend(f"{char_id}: {error}" for error in requirement_errors(character, item))
            items.append(item)
        for index, first in enumerate(items):
            for second in items[index + 1:]:
                overlap = sorted(set(first.get("coverage", [])) & set(second.get("coverage", [])))
                if overlap and not overlap_allowed(first, second):
                    errors.append(
                        f"{char_id}: cannot equip {second.get('name', second.get('id'))}; "
                        f"{', '.join(overlap)} is occupied on the {layer} layer by "
                        f"{first.get('name', first.get('id'))}."
                    )

    resolved_hands = {}
    for hand in ("left", "right"):
        item_ref = hands.get(hand)
        if item_ref is None:
            continue
        item = resolve(item_ref, item_index, f"{char_id} equipment.hands.{hand}", errors)
        if not item:
            continue
        if item.get("equipment_type") not in {"weapon", "shield", "held"}:
            errors.append(f"{char_id}: {item_ref} cannot occupy a held-item hand slot.")
            continue
        if hand not in (item.get("allowed_hands") or ["left", "right"]):
            errors.append(f"{char_id}: {item_ref} is not allowed in the {hand} hand.")
        errors.extend(f"{char_id}: {error}" for error in requirement_errors(character, item))
        resolved_hands[hand] = item
    for hand, item in resolved_hands.items():
        minimum, maximum = hands_required(item)
        other = "right" if hand == "left" else "left"
        same = hands.get(other) == item.get("id")
        if minimum == 2 and not same:
            errors.append(
                f"{char_id}: {item.get('name', item.get('id'))} requires both hands, "
                f"but the {other} hand is not occupied by the same item."
            )
        if maximum == 1 and same:
            errors.append(f"{char_id}: one-handed item {item.get('id')} cannot occupy both hands.")

    refs = equipment.get("accessories")
    if isinstance(refs, list):
        if len(refs) != len(set(refs)):
            errors.append(f"{char_id}: equipment.accessories contains duplicate references.")
        by_slot = {}
        for item_ref in refs:
            item = resolve(item_ref, item_index, f"{char_id} equipment.accessories", errors)
            if not item:
                continue
            if item.get("equipment_type") != "accessory":
                errors.append(f"{char_id}: {item_ref} is not an accessory.")
                continue
            slot = item.get("accessory_slot")
            if slot in by_slot and not overlap_allowed(by_slot[slot], item):
                errors.append(f"{char_id}: accessory slot {slot} has an exclusive conflict.")
            by_slot[slot] = item

    ammo = equipment.get("ammo")
    if ammo is not None:
        if not isinstance(ammo, dict) or set(ammo) != {"item", "quantity"}:
            errors.append(f"{char_id}: equipment.ammo must be null or an item/quantity mapping.")
        else:
            item = resolve(ammo.get("item"), item_index, f"{char_id} equipment.ammo", errors)
            if item and item.get("equipment_type") != "ammunition":
                errors.append(f"{char_id}: {ammo.get('item')} is not ammunition.")
            if not isinstance(ammo.get("quantity"), int) or ammo["quantity"] < 0:
                errors.append(f"{char_id}: equipment.ammo.quantity must be non-negative.")
            ammo_type = item.get("ammo_type") if item else None
            held = {value.get("id"): value for value in resolved_hands.values()}.values()
            if item and not any(ammo_type in (held_item.get("ammo_types") or []) for held_item in held):
                errors.append(f"{char_id}: equipped ammunition is incompatible with held weapons.")
    return errors


def equipped_references(character):
    """Return each equipped reference once; two-handed items are deduplicated."""
    equipment = character.get("equipment") or empty_equipment()
    refs = []
    for field in ("underwear", "clothing", "armor"):
        refs.extend(equipment.get(field) or [])
    hands = equipment.get("hands") or {}
    refs.extend(ref for ref in (hands.get("left"), hands.get("right")) if ref)
    refs.extend(equipment.get("accessories") or [])
    ammo = equipment.get("ammo")
    if isinstance(ammo, dict) and ammo.get("item"):
        refs.append(ammo["item"])
    return list(dict.fromkeys(refs))


def equipment_modifiers(character, item_index):
    totals = {}
    for item_ref in equipped_references(character):
        for stat, value in (item_index.get(item_ref, {}).get("modifiers") or {}).items():
            totals[stat] = totals.get(stat, 0) + value
    return totals


def equip_wearable(character, item, item_index):
    if item.get("equipment_type") != "wearable":
        raise ValueError(f"{item.get('id')} is not wearable.")
    result = deepcopy(character)
    result.setdefault("equipment", empty_equipment())
    result["equipment"][item["layer"]].append(item["id"])
    errors = validate_character_equipment(result, item_index)
    if errors:
        raise ValueError(errors[0])
    return result


def unequip_wearable(character, item_ref):
    result = deepcopy(character)
    for layer in WEARABLE_LAYERS:
        refs = (result.get("equipment") or {}).get(layer) or []
        result["equipment"][layer] = [ref for ref in refs if ref != item_ref]
    return result


def equip_held_item(character, item, item_index, preferred_hand="right", wield_mode=None):
    if item.get("equipment_type") not in {"weapon", "shield", "held"}:
        raise ValueError(f"{item.get('id')} is not held equipment.")
    if preferred_hand not in HAND_NAMES:
        raise ValueError(f"Unknown hand {preferred_hand!r}.")
    result = deepcopy(character)
    result.setdefault("equipment", empty_equipment())
    hands = result["equipment"]["hands"]
    minimum, maximum = hands_required(item)
    use_two = minimum == 2 or (wield_mode == "two_handed" and maximum == 2)
    required = ("left", "right") if use_two else (preferred_hand,)
    occupied = [hand for hand in required if hands.get(hand) is not None]
    if occupied:
        hand = occupied[0]
        raise ValueError(
            f"Cannot equip {item.get('name', item.get('id'))}: {', '.join(required)} "
            f"hand occupancy is required, but {hand} holds {hands[hand]}."
        )
    for hand in required:
        hands[hand] = item["id"]
    errors = validate_character_equipment(result, item_index)
    if errors:
        raise ValueError(errors[0])
    return result


def unequip_held_item(character, item_ref):
    result = deepcopy(character)
    hands = (result.get("equipment") or {}).get("hands") or {}
    for hand in HAND_NAMES:
        if hands.get(hand) == item_ref:
            hands[hand] = None
    return result


def equip_accessory(character, item, item_index):
    if item.get("equipment_type") != "accessory":
        raise ValueError(f"{item.get('id')} is not an accessory.")
    result = deepcopy(character)
    result.setdefault("equipment", empty_equipment())
    result["equipment"]["accessories"].append(item["id"])
    errors = validate_character_equipment(result, item_index)
    if errors:
        raise ValueError(errors[0])
    return result


def unequip_accessory(character, item_ref):
    result = deepcopy(character)
    refs = (result.get("equipment") or {}).get("accessories") or []
    result["equipment"]["accessories"] = [ref for ref in refs if ref != item_ref]
    return result


def equip_ammo(character, item, quantity, item_index):
    result = deepcopy(character)
    result.setdefault("equipment", empty_equipment())
    result["equipment"]["ammo"] = {"item": item["id"], "quantity": quantity}
    errors = validate_character_equipment(result, item_index)
    if errors:
        raise ValueError(errors[0])
    return result


def unequip_ammo(character):
    result = deepcopy(character)
    result.setdefault("equipment", empty_equipment())
    result["equipment"]["ammo"] = None
    return result
