#!/usr/bin/env python3
"""Idempotent Gaia item and character equipment migration.

The migration preserves prose and formatting. It replaces the legacy item slot
field with occupancy metadata and inserts a canonical equipment block in every
character. Assignments only map garments or distinctive catalog equipment
supported by existing appearance, role, or biography text.
"""

import argparse
from pathlib import Path
import re
import shutil
import subprocess

import yaml


FULL_BODY = {
    "item:crossover-desert-robe", "item:hemp-work-kosode",
    "item:laced-kirtle",
    "item:merchants-silk-kosode", "item:strap-apron-dress",
    "item:straight-hem-shenyi", "item:summer-katabira", "item:travel-robe",
    "item:wide-sleeved-scholar-robe", "item:womens-formal-uchikake",
    "item:womens-layered-town-kosode", "item:womens-quilted-winter-kosode",
    "item:womens-linen-chemise", "item:womens-long-cotton-chemise",
    "item:womens-plain-linen-undersmock", "item:womens-pleated-linen-undersmock",
    "item:womens-winter-undersmock", "item:womens-wool-underdress",
}
OVERLAY = {
    "item:barkcloth-shoulder-mantle", "item:canopy-rain-poncho",
    "item:ceremonial-chihaya", "item:feather-edged-ceremonial-mantle",
    "item:feather-edged-shoulder-mantle", "item:hooded-sea-coat",
    "item:pandanus-rain-cape", "item:short-sleeved-outer-coat",
    "item:sleeveless-caravan-vest", "item:sleeveless-riding-vest",
    "item:womens-court-nagabakama", "item:womens-formal-uchikake",
    "item:womens-maekake-work-apron", "item:wool-overtunic",
    "item:wrapped-work-apron", "item:pleated-work-hakama",
    "item:riding-hakama", "item:shrine-maiden-hakama",
    "item:tattsuke-field-hakama", "item:travelers-narrow-hakama",
}


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: missing frontmatter")
    return text, yaml.safe_load(parts[1])


def item_metadata(item):
    if not item.get("is_equippable", False):
        return {}
    item_id = item["id"]
    slot = item.get("slot")
    item_type = item.get("item_type")
    tags = set(item.get("item_tags") or [])
    name = item.get("name", "").lower()
    appearance = str(item.get("appearance", "")).lower()

    if item_type == "clothing":
        layer = "underwear" if "underwear" in tags else "clothing"
        if slot in {"legs", "waist"}:
            coverage = ["left_leg", "right_leg"]
        else:
            coverage = ["torso"]
            armless = any(word in f"{name} {appearance}" for word in (
                "sleeveless", "strap apron", "chest wrap", "support band",
                "underbodice", "loincloth",
            ))
            if not armless:
                coverage += ["left_arm", "right_arm"]
            if item_id in FULL_BODY:
                coverage += ["left_leg", "right_leg"]
            if "hooded" in name:
                coverage.insert(0, "head")
        metadata = {
            "equipment_type": "wearable", "layer": layer, "coverage": coverage,
        }
        if item_id in OVERLAY or "apron" in name:
            metadata["stacking"] = {"mode": "overlay"}
        return metadata

    if slot in {"main_hand", "off_hand", "two_hand"}:
        kind = "weapon" if item_type == "weapon" else "held"
        if item_id == "item:drakeward-shield":
            kind = "shield"
        return {
            "equipment_type": kind,
            "hands_required": 2 if slot == "two_hand" else 1,
            "allowed_hands": ["left", "right"],
        }
    if slot in {"trinket", "neck"}:
        return {"equipment_type": "accessory", "accessory_slot": slot}
    raise ValueError(f"{item_id}: equippable item has unsupported legacy slot {slot!r}")


def render_metadata(metadata):
    lines = []
    for key, value in metadata.items():
        if key in {"equipment_type", "layer", "hands_required", "accessory_slot"}:
            lines.append(f"{key}: {value}")
        elif key in {"coverage", "allowed_hands"}:
            lines.append(f"{key}:")
            lines.extend(f"- {entry}" for entry in value)
        elif key == "stacking":
            lines.extend(["stacking:", f"  mode: {value['mode']}"])
    return "\n".join(lines)


def migrate_item(path, apply):
    text, item = parse_frontmatter(path)
    changed = False
    if re.search(r"(?m)^slot:", text):
        text = re.sub(r"(?m)^slot:.*\n", "", text, count=1)
        changed = True
    if item.get("is_equippable", False) and "equipment_type" not in item:
        metadata = render_metadata(item_metadata(item))
        text = re.sub(
            r"(?m)^(is_equippable:\s*true\s*)$",
            lambda match: f"{match.group(1)}\n{metadata}",
            text,
            count=1,
        )
        changed = True
    if changed and apply:
        path.write_text(text, encoding="utf-8", newline="\n")
    return changed


def unique(*groups):
    return list(dict.fromkeys(item for group in groups for item in group if item))


def culture_for(character):
    heritage = str(character.get("heritage", "")).lower()
    if "tsukuyomi" in heritage or heritage == "jin":
        return "tsukuyomi" if "tsukuyomi" in heritage else "sangguo"
    if any(word in heritage for word in ("sangguo",)):
        return "sangguo"
    if any(word in heritage for word in ("al-khayzar", "al-khayzari")):
        return "al-khayzar"
    if any(word in heritage for word in ("hrafn", "northlander")):
        return "hrafnland"
    if any(word in heritage for word in ("valdr", "royal valdris")):
        return "valdris"
    if any(word in heritage for word in ("verdan", "river-folk", "tribal")):
        return "verdania"
    if any(word in heritage for word in ("archipel", "tide island")):
        return "tide"
    return None


def clothing_assignment(character):
    text = str(character.get("appearance", "")).lower()
    gender = str(character.get("gender", "")).lower()
    culture = culture_for(character)
    evidence = (
        "robe", "clothing", "clothes", "tunic", "kimono", "hakama", "dress",
        "skirt", "trouser", "wool", "cotton", "wrap", "vest", "coat", "apron",
        "silk", "leathers", "garb", "attire", "cloth", "shirt", "mantle", "cape",
    )
    if not any(word in text for word in evidence):
        return []

    top = bottom = None
    overlays = []
    if "elven work-tunic" in text:
        return ["item:elven-forest-tunic"]
    if "canvas trousers" in text and "linen shirt" in text:
        return ["item:linen-work-tunic", "item:divided-hose"]

    if culture == "tsukuyomi":
        if "shrine robe" in text or ("white top" in text and "red hakama" in text):
            top, bottom = "item:shrine-maiden-kosode", "item:shrine-maiden-hakama"
            if "chihaya" in text:
                overlays.append("item:ceremonial-chihaya")
        elif any(word in text for word in ("layered kimono", "elaborate", "autumn color")):
            top = "item:womens-layered-town-kosode" if gender == "female" else "item:merchants-silk-kosode"
        elif any(word in text for word in ("court robe", "court attire", "formal", "fine kimono")):
            top = "item:merchants-silk-kosode"
            if gender == "female" and "overrobe" in text:
                overlays.append("item:womens-formal-uchikake")
        elif any(word in text for word in ("travel", "courier")):
            top = "item:travel-robe"
            if "hakama" in text or "trouser" in text:
                bottom = "item:travelers-narrow-hakama"
        elif "riding" in text:
            top, bottom = "item:travel-robe", "item:riding-hakama"
        else:
            top = "item:hemp-work-kosode"
            if "field" in text and "hakama" in text:
                bottom = "item:tattsuke-field-hakama"
            elif "work hakama" in text:
                bottom = "item:pleated-work-hakama"
        if "apron" in text and gender == "female":
            overlays.append("item:womens-maekake-work-apron")

    elif culture == "sangguo":
        if any(word in text for word in ("academy", "scholar", "librarian", "physician")):
            top = "item:wide-sleeved-scholar-robe"
        elif "riding" in text:
            top, bottom = "item:cross-collar-ru-jacket", "item:reinforced-riding-trousers"
            overlays.append("item:sleeveless-riding-vest")
        elif any(word in text for word in ("robe", "formal", "court", "silk")):
            top = "item:straight-hem-shenyi"
        else:
            top, bottom = "item:short-shan-work-shirt", "item:bound-cuff-field-trousers"
        if "skirt" in text:
            top, bottom = "item:cross-collar-ru-jacket", "item:pleated-qun-skirt"
        elif "trouser" in text and bottom is None:
            top, bottom = "item:cross-collar-ru-jacket", "item:loose-ku-trousers"

    elif culture == "al-khayzar":
        if "riding" in text:
            top, bottom = "item:loose-cotton-qamis", "item:desert-riding-trousers"
            overlays.append("item:sleeveless-caravan-vest")
        elif "loose desert cotton" in text:
            top, bottom = "item:loose-cotton-qamis", "item:loose-sirwal"
        elif any(word in text for word in ("formal", "fine robe", "gold-trimmed", "scholar", "dark robe")):
            top = "item:crossover-desert-robe"
            if "vest" in text:
                overlays.append("item:short-sleeved-outer-coat")
        elif "skirt" in text or "dress" in text:
            top, bottom = "item:loose-cotton-qamis", "item:long-gathered-skirt"
        else:
            top, bottom = "item:knee-length-pirahan", "item:bound-ankle-desert-trousers"
            if "vest" in text:
                overlays.append("item:sleeveless-caravan-vest")
        if "izar" in text:
            bottom = "item:wrapped-izar"

    elif culture == "hrafnland":
        if "dress" in text:
            top = "item:strap-apron-dress"
        elif any(word in text for word in ("sea coat", "sailor", "ship clothes")):
            top, bottom = "item:hooded-sea-coat", "item:gathered-ship-trousers"
        elif "tunic" in text:
            top = "item:fur-lined-winter-tunic" if any(word in text for word in ("fur", "winter")) else "item:linen-work-tunic"
            bottom = "item:wool-trousers" if "trouser" in text else None
        else:
            top, bottom = "item:wool-overtunic", "item:wool-trousers"
        if "skirt" in text:
            bottom = "item:long-wool-skirt"
        if "apron" in text and "leather apron" not in text:
            overlays.append("item:wrapped-work-apron")

    elif culture == "valdris":
        race = str(character.get("race", "")).lower()
        if "dwarf" in race and any(word in text for word in ("work", "tunic", "clothes", "shirt", "wool")):
            top, bottom = "item:dwarven-split-hem-tunic", "item:wool-trousers"
        elif "elf" in race and any(word in text for word in ("forest", "travel", "road")):
            top, bottom = "item:elven-forest-tunic", "item:elven-fitted-leggings"
        elif "dress" in text:
            top = "item:laced-kirtle"
        elif "riding" in text:
            top, bottom = "item:linen-work-tunic", "item:riding-breeches"
        else:
            top, bottom = "item:linen-work-tunic", "item:wool-trousers"
        if "skirt" in text:
            bottom = "item:long-work-skirt"

    elif culture == "verdania":
        if any(word in text for word in ("ceremonial feather", "feather-cloth", "festival")):
            top, bottom = "item:feather-edged-shoulder-mantle", "item:leaf-fringe-festival-skirt"
        elif "river" in text or "water-gear" in text:
            top, bottom = "item:open-side-river-vest", "item:river-worker-split-wrap"
        else:
            top, bottom = "item:sleeveless-barkcloth-tunic", "item:softbark-wrap-skirt"
        if "rain poncho" in text:
            overlays.append("item:canopy-rain-poncho")
        if ("skirt" in text or "loincloth" in text) and not any(
            word in text for word in ("tunic", "vest", "shirt", "clothes", "garments", "robes")
        ):
            top = None
        if "loincloth" in text:
            bottom = "item:braided-fiber-loincloth"

    elif culture == "tide":
        if any(word in text for word in ("ceremonial", "dance-cloth", "feathered")):
            top, bottom = "item:feather-edged-ceremonial-mantle", "item:leaf-fiber-dance-skirt"
        elif any(word in text for word in ("sailing", "paddling", "canoe clothes")):
            top, bottom = "item:open-sided-island-tunic", "item:split-paddling-wrap"
        else:
            top = "item:open-sided-island-tunic"
            bottom = "item:pau-wrap-skirt" if gender == "female" else "item:rectangular-waist-wrap"
        if "sarong" in text:
            bottom = "item:island-sarong"
        if "rain cape" in text:
            overlays.append("item:pandanus-rain-cape")
    return unique([top, bottom], overlays)


def special_assignment(character):
    char_id = character.get("id")
    appearance = str(character.get("appearance", "")).lower()
    role = str(character.get("role", "")).lower()
    biography = str(character.get("biography", "")).lower()
    text = " ".join((appearance, role, biography))
    held = []
    accessories = []

    if "blowpipe" in appearance:
        held.append("item:sleep-blowpipe")
    if "iron body cultivation manual" in text:
        held.append("item:chi-manual")
    if "astrolabe" in appearance:
        held.append("item:desert-astrolabe")
    if "spirit-rattle" in appearance or "spirit rattle" in appearance:
        held.append("item:spirit-rattle")
    if "river-stone oracle" in text:
        held.append("item:river-stone-oracle")
    if "prophecy bones" in text:
        held.append("item:volva-bones")
    if "shrine bell of silence" in text:
        held.append("item:yokai-bell")
    if "kitsune's message scroll" in text:
        held.append("item:kitsune-scroll")
    if "dwarven master-key" in text or "dwarven master key" in text:
        held.append("item:dwarven-master-key")
    if "starlight lantern" in text:
        held.append("item:starlight-lantern")
    if "frost-giant's horn" in text or "frost giant's horn" in text:
        held.append("item:frost-giant-horn")
    if "current-marking tattoo needle" in text or (
        "tattoo" in role and "needle" in appearance
    ):
        held.append("item:current-needle")
    if "wayfinder" in role and "staff" in appearance:
        held.append("item:wayfinder-staff")
    if "wayfinder" in role and "compass" in appearance:
        held.append("item:star-compass")
    if any(phrase in appearance for phrase in ("contract lamp", "family lamp", "binding lamp")):
        held.append("item:djinn-lamp")
    if "raikiri" in appearance:
        held.append("item:raikiri")
    if "drakeward shield" in appearance:
        held.append("item:drakeward-shield")

    if char_id == "character:arakawa-kenta" or "ofuda talisman" in appearance:
        accessories.append("item:ofuda")
    if "qilin's blessing token" in text:
        accessories.append("item:qilin-token")
    if "jade seal" in appearance and "warlord" in role:
        accessories.append("item:warlord-jade-seal")
    return unique(held), unique(accessories)


def render_list(name, refs, indent=2):
    pad = " " * indent
    if not refs:
        return [f"{pad}{name}: []"]
    return [f"{pad}{name}:"] + [f"{pad}- {item_ref}" for item_ref in refs]


def equipment_block(character):
    clothing = clothing_assignment(character)
    held, accessories = special_assignment(character)
    left = right = None
    if held:
        if held[0] in {"item:sleep-blowpipe", "item:chi-manual"}:
            left = right = held[0]
        else:
            right = held[0]
            if len(held) > 1:
                left = held[1]
    lines = ["equipment:"]
    lines += render_list("underwear", [])
    lines += render_list("clothing", clothing)
    lines += render_list("armor", [])
    lines += [
        "  hands:",
        f"    left: {left if left else 'null'}",
        f"    right: {right if right else 'null'}",
    ]
    lines += render_list("accessories", accessories)
    lines.append("  ammo: null")
    return "\n".join(lines)


def apply_character_patch(path, block, root):
    relative = path.relative_to(root).as_posix()
    patch = (
        "*** Begin Patch\n"
        f"*** Update File: {relative}\n"
        "@@\n"
        "-visual:\n"
        + "\n".join(f"+{line}" for line in block.splitlines())
        + "\n+visual:\n"
        "*** End Patch"
    )
    codex = shutil.which("codex")
    if not codex:
        raise RuntimeError("codex patch executable not found")
    result = subprocess.run(
        [codex, "--codex-run-as-apply-patch", patch],
        cwd=root,
        text=True,
        capture_output=True,
    )
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)


def migrate_character(path, apply, root):
    text, character = parse_frontmatter(path)
    if "equipment" in character:
        return False, character
    block = equipment_block(character)
    if not re.search(r"(?m)^visual:", text):
        raise ValueError(f"{path}: no visual field found for insertion")
    if apply:
        apply_character_patch(path, block, root)
    return True, character


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dir", default=".", help="Gaia repository root")
    parser.add_argument("--apply", action="store_true", help="write changes")
    args = parser.parse_args()
    # Keep the mapped-drive path. Resolving it to UNC changes write semantics on
    # this repository even though reads continue to work.
    root = Path(args.dir).absolute()
    item_changes = sum(
        migrate_item(path, args.apply)
        for path in sorted((root / "records" / "items").glob("*.md"))
    )
    character_changes = 0
    no_clothing_match = []
    skipped = []
    for path in sorted((root / "records" / "characters").glob("*.md")):
        try:
            changed, character = migrate_character(path, args.apply, root)
        except RuntimeError as exc:
            skipped.append((path.relative_to(root).as_posix(), str(exc).strip()))
            _, character = parse_frontmatter(path)
            changed = False
        character_changes += changed
        if not clothing_assignment(character):
            no_clothing_match.append(character.get("id"))
    mode = "Applied" if args.apply else "Would apply"
    print(f"{mode} item metadata changes: {item_changes}")
    print(f"{mode} character equipment blocks: {character_changes}")
    print(f"Characters without a supported clothing assignment: {len(no_clothing_match)}")
    for char_id in no_clothing_match:
        print(f"  {char_id}")
    print(f"Skipped character files: {len(skipped)}")
    for path, error in skipped:
        print(f"  {path}: {error}")


if __name__ == "__main__":
    main()
