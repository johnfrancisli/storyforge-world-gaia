#!/usr/bin/env python3
"""Validate Gaia item occupancy metadata and character equipment references."""

import argparse
from pathlib import Path
import sys

import yaml

from equipment import validate_character_equipment, validate_item_definition


def load_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("missing YAML frontmatter")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data


def validate_repository(root):
    errors = []
    item_index = {}
    for path in sorted((root / "records" / "items").glob("*.md")):
        try:
            item = load_frontmatter(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        item_id = item.get("id")
        if item_id in item_index:
            errors.append(f"{path.relative_to(root)}: duplicate item ID {item_id}.")
        elif item_id:
            item_index[item_id] = item
        errors.extend(validate_item_definition(item))

    character_count = 0
    for path in sorted((root / "records" / "characters").glob("*.md")):
        character_count += 1
        try:
            character = load_frontmatter(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        errors.extend(validate_character_equipment(character, item_index))
    return errors, len(item_index), character_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dir", default=".", help="Gaia repository root")
    args = parser.parse_args()
    root = Path(args.dir).resolve()
    errors, item_count, character_count = validate_repository(root)
    for error in errors:
        print(f"ERROR: {error}")
    print(
        f"Validated {item_count} items and {character_count} characters: "
        f"{len(errors)} error(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
