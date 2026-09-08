# Gaia Equipment System

## Purpose

Gaia uses one character equipment structure for worn items, held items,
accessories, and ammunition. Character records store only raw stable item IDs.
All names, descriptions, occupancy, requirements, and modifiers remain on the
canonical item records.

This document adapts the original unified-equipment proposal to the repository
that actually exists. Gaia is currently a Markdown/YAML content repository with
Python validation; it has no application UI, API, combat runtime, TypeScript
schema package, or established inventory quantity model.

## Reviewed decisions

- Preserve Gaia's existing item stable IDs. The proposed equipment and weapon
  prefixes would create a competing reference convention.
- Replace the old item slot field. It mixed worn regions, hand occupancy, and
  accessory locations in one field.
- Keep the existing item_type taxonomy for lore/catalog classification and add
  equipment_type for equip behavior.
- Use layer plus coverage only for wearables.
- Use hands_required plus allowed_hands only for held items.
- Treat a shield as held equipment even though its catalog item_type is armor.
- Default wearable/accessory stacking to exclusive. Explicit outer garments,
  aprons, mantles, and hakama use stacking mode overlay where the catalog
  establishes deliberate layering.
- Keep inventory separate from equipped state. No inventory field is added
  until Gaia has an authoritative ownership/quantity model.
- Keep base stats unchanged. Modifiers are calculated from unique equipped
  references, so a two-handed item is never counted twice.
- Preserve the existing optional armor and weapon training shapes. Equipment
  requirements are checked if a future item declares them; no training values
  are invented during this content migration.

## Canonical schemas

Every character has the following shape:

~~~yaml
equipment:
  underwear: []
  clothing: []
  armor: []
  hands:
    left: null
    right: null
  accessories: []
  ammo: null
~~~

Wearable item:

~~~yaml
id: item:example-tunic
item_type: clothing
is_equippable: true
equipment_type: wearable
layer: clothing
coverage:
- torso
- left_arm
- right_arm
~~~

Held item:

~~~yaml
id: item:example-greatsword
item_type: weapon
is_equippable: true
equipment_type: weapon
hands_required: 2
allowed_hands:
- left
- right
~~~

Accessory:

~~~yaml
id: item:example-token
is_equippable: true
equipment_type: accessory
accessory_slot: neck
~~~

Ammunition, when canonical ammo records are added:

~~~yaml
equipment:
  ammo:
    item: item:example-arrow
    quantity: 18
~~~

## Occupancy rules

Wearable layers are underwear, clothing, and armor. Valid body regions are
head, torso, left_arm, right_arm, left_hand, right_hand, waist, left_leg,
right_leg, left_foot, and right_foot.

Two exclusive wearables conflict when their coverage intersects on the same
layer. Coverage may overlap across different layers. An explicit overlay item
can share covered regions on its layer. Worn left_hand or right_hand coverage
is independent of the corresponding held-item hand.

One-handed items occupy one allowed hand. Two-handed items occupy both hands by
repeating the same stable ID in left and right; shared rules deduplicate the
reference for modifiers and clear both hands when it is unequipped.

Accessory conflicts are based on accessory_slot and stacking behavior. The
model can later support multiple rings or similar items without changing the
wearable layers.

## Migration plan and execution

1. Audit all character/item records, validators, tests, and the absence of
   application runtime code.
2. Classify every equippable catalog item by behavior and occupancy.
3. Remove all legacy slot fields after their replacement metadata exists.
4. Add the complete equipment structure to every character.
5. Assign only catalog items supported by existing appearance, role, or
   biography text. Leave unsupported categories empty instead of inventing IDs.
6. Validate definitions, references, wearable conflicts, held occupancy,
   accessory conflicts, ammo shape/compatibility, and optional training
   requirements.
7. Test layer overlap, same-layer rejection, full-body conflict, asymmetric
   armor, worn-hand versus held-hand independence, sword/shield use,
   two-handed occupancy/unequip, overlay garments, and modifier deduplication.

The migration is idempotent:

~~~text
python migrate_equipment.py --dir . --apply
python validate_equipment.py --dir .
python test_equipment.py
~~~

### Execution status

- All 140 item records have occupancy metadata and no legacy slot fields.
- All 387 character records have the canonical equipment block.
- Of those migrated characters, 296 have supported clothing references and 91
  deliberately remain empty because their described garments or gear have no
  safe catalog match.
- Nine supported special held items/accessories are assigned from explicit
  source evidence.
- The completed migration dry-run reports no pending item or character changes,
  and repository equipment validation reports zero errors.

## Conservative classification boundaries

The catalog currently contains clothing, underwear, two weapons, one shield,
held tools/relics/documents, and three accessories. It does not contain
canonical wearable armor, ordinary swords/axes/bows/knives, footwear, belts,
packs, hats, jewelry, generic cloaks, ammunition, or most trade tools described
in character prose.

Those unsupported descriptions are not silently mapped to a merely similar
item. Their character fields remain empty until the matching canonical item
records exist. The same rule applies to underwear: culturally plausible
underwear is not assigned unless source text establishes it.

## Validation ownership

The equipment.py module is the shared domain layer. It owns conflict checks,
training/requirement checks, mutation helpers, equipped-reference
deduplication, and modifier aggregation.

The validate_equipment.py module is the repository scanner. It verifies every
item and character frontmatter record against the shared rules.

The test_equipment.py module covers the architecture's required behavior. A
future application should call the shared domain rules or port them as one
authoritative module rather than reimplementing conflict checks in UI
components.
