# Gaia Repository Agent Instructions

## Wiki-link entity references

When authoring or editing Markdown prose in this repository, use wiki-style
links to refer to existing canonical records. The syntax is:

```
[[type:stable-id]]
[[type:stable-id|display text]]
```

The reference target comes first, the optional display text second.

### Rules

1. **Double square brackets are reserved for resolvable Storyforge entity
   references.** Do not use `[[...]]` for anything else in Markdown prose.
2. **The target uses the entity's stable typed ID, not its visible name.**
   `[[character:aerindra]]`, not `[[Aerindra]]`.
3. **The target always comes before the display text.**
   `[[character:aerindra|the pale-haired fletcher]]`, not
   `[[the pale-haired fletcher|character:aerindra]]`.
4. **Names can change; stable IDs must not.** Never change a stable ID merely
   because a record was renamed.
5. **`[[type:id]]` displays the record's current canonical name.** Use the
   short form when the prose should track the name automatically.
6. **`[[type:id|text]]` preserves the supplied contextual display text.** Use
   the piped form when the surrounding prose requires an alias or contextual
   wording.
7. **Plain mentions remain ordinary prose** and do not create a resolvable
   reference. Only wrap a mention in `[[...]]` when it should be linkable.
8. **A wiki link creates a mention/reference edge, not automatically a
   canonical relationship.** Actual relationships must continue to use
   Storyforge's structured relationship records.
9. **Structured JSON/YAML fields that already expect raw IDs must continue
   using raw IDs.** Never put wiki-link markup inside fields like
   `participants`, `locations`, or `affiliations`.

   Correct:

   ```json
   {
     "participants": ["character:aerindra"],
     "locations": ["location:harus-shrine"]
   }
   ```

   Wrong:

   ```json
   {
     "participants": ["[[character:aerindra|Aerindra]]"]
   }
   ```

10. **Wiki links belong only in Markdown or prose fields** unless the schema
    explicitly says otherwise.

### Authoring instruction

When referring to an existing canonical record in authoring Markdown, use
`[[type:stable-id]]` or `[[type:stable-id|contextual display text]]`. The
stable reference must appear before the optional display text. Resolve
existing records before creating links; never invent an ID for a record that
has not been created. Use plain text for incidental people and things that
are not canonical records. Wiki links represent references, not relationships.

### Additional guidance

- **Reuse an existing record ID** whenever the entity already exists.
- **Never resolve entities by visible name alone** when a stable ID is
  available.
- **Never change a stable ID** merely because a record was renamed.
- **Do not create links for generic or incidental nouns.** "The innkeeper"
  is plain text unless there is a `character:` record for that person.
- **Do not expose raw wiki-link markup in final player-facing narration.**
  Render it as its display text or canonical name.
- **Preserve wiki links when editing internal lore** unless the referenced
  record is intentionally removed.
- **Report unresolved references** rather than silently converting them to
  plain text.

### Valid entity types

| Type prefix | Example |
|---|---|
| `character` | `[[character:aerindra]]` |
| `location` | `[[location:harus-shrine]]` |
| `organization` | `[[organization:dragon-order]]` |
| `org` | `[[org:briar-wardens]]` (abbreviation used in existing records) |
| `thread` | `[[thread:broken-road]]` |
| `item` | `[[item:raikiri]]` |
| `relationship` | `[[relationship:two-blacksmiths-of-valdris]]` |
| `lore` | `[[lore:reincarnation-in-gaia]]` |

## Typed character relationships

- Author family facts only on canonical records under `records/relationships/`; never add reciprocal relationship fields to character files.
- Put both endpoints in `participants`, using raw stable character IDs, and write one directed `kinship` fact. Do not author an inverse duplicate.
- Supported predicates are `parent_of`, `adoptive_parent_of`, `guardian_of`, `sibling_of`, `half_sibling_of`, `spouse_of`, `former_spouse_of`, `betrothed_to`, `grandparent_of`, `aunt_or_uncle_of`, `cousin_of`, and `chosen_family_of`.
- Every fact needs `visibility: public`, `participants`, or `gm_only`. Use the narrowest audience supported by canon.
- Enrich an existing pair's relationship record instead of creating a duplicate. Create a new pairwise record only for an explicit, unambiguous claim whose two canonical character IDs already exist.
- Leave unnamed relatives in prose. Put uncertain inferences in `RELATIONSHIP-PROPOSALS.md`; disconnected characters are valid and require no filler relationships.
- Relationship envelope `links` and character backlinks are derived by Storyforge. Do not maintain them manually.
- Developed relationships should include a concise `summary`, a free-text `current_stage`, directional `perspectives`, and an ordered `history`. Each perspective uses `subject`, `object`, a `disposition` from `-100` to `100`, a visible explanation, and `visibility: public`, `subject`, `participants`, or `gm_only`.
- Directional perspectives may disagree. Never replace them with one shared score merely for convenience; retain a legacy top-level `disposition` only when preserving an older record.
- History events use stable record-local IDs and may include `occurred_at`, `stage_before`, `stage_after`, and directional `perspective_changes` with `before` and `after`. Record only events supported by canon; do not manufacture milestones to make a log look complete.

### Future syntax (not yet implemented)

Section anchors may be supported in the future:

```
[[location:crossford#market|Crossford market]]
```

The portion before `#` is the stable record ID; the portion after is a
section or sub-anchor. Do not rely on this syntax until it is officially
supported.

---

## Mandatory visual-prompt guidance

Before creating, populating, reviewing, or editing any `visual.prompt` value under `records/`, read and follow this entire section first.

These rules apply to the content stored in `visual.prompt`. Requirements such as “output only the prompt” do not prohibit normal repository edits, validation, or concise progress and completion messages.

Every visual record under `records/` uses this base schema:

```yaml
visual:
  prompt: ''
image:
  url: '' # primary landscape/background image
  focalPoint:
    x: 0.5
    y: 0.5
  seed: null
```

Character records extend `image` with a neutral transparent cutout variation:

```yaml
image:
  url: '' # primary landscape/background image
  focalPoint:
    x: 0.5
    y: 0.5
  seed: null
  portrait: # secondary profile image; never used as the scene background
    url: ''
    focalPoint:
      x: 0.5
      y: 0.1
    seed: null
  variations:
    - name: neutral
      backgroundRemovedUrl: ''
```

### Storage and source-reading requirements

- Save the completed positive prompt in the record's `visual.prompt` field
  (`visual` > `prompt`). Do not place it in a separate prompt file, a biography
  section, a note, or another field.
- Keep `image` as a top-level sibling of `visual`, not nested inside it.
- Store the primary landscape/background image in `image.url`. Character
  profile portraits belong in `image.portrait.url`; they are secondary and
  must not replace the landscape background. Use a plain absolute URL or a
  world-relative `assets/images/...` path, never Markdown link syntax.
- Use `image.focalPoint: {x: 0.5, y: 0.5}` for a landscape by default. Use
  `image.portrait.focalPoint: {x: 0.5, y: 0.1}` for a profile portrait unless
  an existing image requires a deliberately different crop.
- Store the exact generation seed in the matching `image.seed` or
  `image.portrait.seed` field. Use `null` until an image is generated; never
  invent or silently replace the seed associated with an existing image.
- Preserve the entire existing `image` object when editing unrelated fields.
  Its background, portrait, focal points, seeds, galleries, and variations are
  generation metadata that may not be reconstructable.
- Character cutouts belong in `image.variations`. Every character starts with
  one entry named `neutral`; do not recreate the legacy top-level
  `portrait_variations` field.
- Store a plain absolute URL to the transparent PNG in
  `image.variations[].backgroundRemovedUrl`. Leave it empty until the
  background-removed asset exists. This cutout is composited over scene
  backgrounds during dialogue, so it must retain transparency.
- Preserve existing named variations and their URLs. Never replace a real cutout
  URL with an empty placeholder while editing another field.
- Before creating or revising a character's `visual.prompt`, read the character's
  entire record, including the full biography and all other prose and structured
  fields. Do not build the prompt from only the summary, appearance field, or the
  section nearest `visual.prompt`.
- Read biography, appearance prose, and `gm_notes` to find explicit canonical
  visual facts, current-state facts, and references that must be resolved. They
  are not authority for inferred physical evidence: do not turn an occupation,
  history, personality, wealth, or habit into scars, muscles, dirt, jewelry,
  posture, expression, or other prompt tokens unless a canonical character,
  item, location, or current-scene field separately establishes that visible fact.
- Treat canonical physical identity as mandatory, not optional flavor. When the
  character record supplies them, preserve the visible age category, species,
  body/build and proportions, skin/fur/scale colour, face, eye colour and shape,
  hair colour/length/texture/style, facial hair, horns, ears, tails, wings,
  markings, scars, and other species-specific features in the prompt.
- Preserve an explicitly authored adult chest or breast-size descriptor as part
  of body proportions. Use neutral anatomical tags such as `broad chest`,
  `small breasts`, or `large breasts`; do not embellish or eroticize them. Never
  add or preserve breast-size tags for a child character.
- Do not substitute a more generic feature for a supplied one. `dark hair` does
  not replace `long dark teal braids`; `pale skin` does not replace `blue-green
  skin`; a race name does not replace its visible morphology.
- Do not invent a missing identity trait. Fill a gap only from an exact,
  authoritative race or heritage baseline that explicitly supplies that visual
  category; never choose one option from a documented range of possibilities.
  If hair, eyes, build, or non-human morphology remains unspecified after that
  lookup, leave it unspecified and report the missing data for author review.
- For a non-human character, never rely on the race label alone. Resolve an
  exact matching `character_visual_reference` or
  `character_visual_references` entry from `records/lore/`, then include its
  prompt baseline and invariant morphology. The character's own `visual`
  fields always override the population baseline.
- Do not infer ancestry from a name, culture, role, or approximate string. A
  `Half-Elf` does not inherit an `Elf` reference unless the lore explicitly
  lists both under `applies_to`.

Character age is a top-level factual field, not part of `visual`. It may inform
a visual age category but should not normally appear numerically in an image
prompt.

### Race and ancestry visual-reference schema

Race lore used by prompt generation must include a compact, explicit visual
reference. A lore record may define one block:

```yaml
character_visual_reference:
  applies_to: [Mizuhito]
  prompt: amphibious humanoid, blue-green skin, webbed fingers and toes
  invariant_traits:
    - amphibious humanoid proportions
    - webbed fingers and toes
  variable_traits:
    - skin ranges through blue-green and teal tones
  avoid:
    - ordinary human hands and feet
```

Or one central race document may define multiple entries under
`character_visual_references`. `prompt` is a short positive baseline suitable
for direct composition. `invariant_traits` explains what must remain true,
`variable_traits` documents individual variation and must not be imposed on
everyone, and `avoid` records common wrong renderings for review and future
negative-prompt support. Keep political history and metaphysics in normal lore
prose; only visible anatomy belongs in the prompt baseline.

### One Obsession / ComfyUI visual prompt generator

You convert Gaia RPG records and current scene data into efficient positive image prompts for the One Obsession checkpoint in ComfyUI.

Your job is NOT to summarize the character, rewrite the scene, explain the lore, or creatively interpret biography.

Your job is to describe:

**WHAT SHOULD BE VISIBLE IN THIS IMAGE RIGHT NOW.**

Think like a camera, not a novelist.

The output is combined with a separate GLOBAL STYLE prompt.

Therefore:

* output scene-specific visual content only
* use concise Danbooru-style tags and short literal visual phrases
* do not add global quality tags
* do not add a negative prompt
* do not repeat global art-style instructions
* do not add narrative explanation
* output one comma-separated positive prompt
* do not explain choices inside `visual.prompt`

#### Mandatory execution workflow

Follow these steps in order. Do not begin drafting the final prompt until all
required references have been resolved.

1. **Select the target and image mode.** Identify the record being generated
   and choose exactly one mode: primary/background character image, portrait,
   neutral character cutout, current-scene image, item/memento, location, or
   map. The mode determines composition and which details can be visible.
2. **Read canonical inputs.** Read the complete subject record and the complete
   current scene when one exists. Treat the existing `visual.prompt` only as
   disposable generated output; never use it as evidence or copy tokens from it.
3. **Resolve identity.** Extract explicit individual visual fields. Convert age
   and exact measurements to useful visible categories. For every non-human character, resolve the exact
   `race` match in `records/lore/races-and-peoples-of-gaia.md`, then collect its
   positive `prompt` concepts and applicable `invariant_traits`.
4. **Fill only genuine gaps.** Use a resolved heritage/population baseline only
   for identity details the individual record leaves unspecified. Never average
   alternatives, override an authored individual trait, or infer ancestry from a
   name, role, culture, or approximate race string.
5. **Resolve visible wardrobe and objects.** Apply explicit scene overrides,
   then follow relevant `equipment` references to their item records. Determine
   which outer layers, accessories, held objects, or carried items the selected
   pose and frame actually reveal. Ignore covered underwear and hidden inventory.
6. **Resolve place and temporary state.** Follow the scene location, then
   `current_state.location`, to the canonical location record. With no current
   location, use an explicitly associated canonical home or workplace; only then
   may a resolved regional fallback palette be used. Collect only
   supported present-frame action, pose, expression, gaze, hairstyle, clothing
   overrides, injuries, dirt, wetness, transformations, weather, time, and light.
7. **Create an internal source ledger.** Before composing, group candidate
   details as individual canon, race invariant, heritage fallback, resolved item,
   current scene, resolved location, or image-mode rule. This ledger is for
   validation only and is never stored in `visual.prompt`.
8. **Lock composition before small details.** Choose one coherent action, pose,
   framing, viewpoint, and gaze for the selected mode. Do not alter composition
   merely to expose a minor scar, tattoo, fingernail, or garment layer.
9. **Apply the camera test.** Remove anything the selected camera could not see,
   anything merely habitual, and every biography-based inference. Keep explicit
   identity traits unless the composition truly makes a small feature invisible.
10. **Literalize and order.** Convert retained facts to concise Danbooru-first
    tags or short literal phrases, bind every attribute to its object, remove
    causes and subjective prose, and order the tokens according to the applicable
    character, item, location, or map rules below.
11. **Run a token-by-token audit.** Verify that every phrase has one ledger
    source, all race invariants and scene overrides are honored, referenced items
    were opened, traits remain attached to the correct character, composition is
    non-conflicting, and no style, quality, negative-prompt, or unsupported token
    remains. Report unresolved references, missing identity data, or canonical
    conflicts instead of guessing.
12. **Save without collateral changes.** Store only the final comma-separated
    positive prompt in `visual.prompt`. Preserve the complete sibling `image`
    object and all existing URLs, focal points, seeds, galleries, portraits, and
    variations unless the task explicitly changes them.

---


### 1. GENERATED PROMPT IS NOT CANON


`visual.prompt` is generated output.

It is NOT a source of truth.

When regenerating or revising a prompt:

**NEVER read the existing `visual.prompt` as evidence for what the character,
item, location, or map looks like.**

Reconstruct the prompt from canonical fields and referenced records.

This prevents an old invented detail from becoming permanent canon.

For example, if an older prompt contains:

```text
embroidered borders
```

but no canonical clothing record establishes embroidery:

REMOVE IT.

Do not preserve it merely because it appeared in the previous prompt.

---


### 2. SOURCE AUTHORITY


Resolve each visual category from its authoritative source.

Do not treat biography, appearance prose, equipment, race lore, and the existing prompt as equally authoritative.

#### Permanent individual appearance

Primary source:

```yaml
visual:
  body_build:
  skin:
  face:
  eyes:
  hair:
  distinctive_features:
```

These describe the individual character.

---

#### Racial anatomy

Canonical source:

```text
records/lore/races-and-peoples-of-gaia.md
```

Use the exact matching entry under:

```yaml
character_visual_references:
```

Match `race` against `applies_to` exactly.

Do not approximate race names.

Do not use general fantasy knowledge instead.

---

#### Heritage / national appearance

Use the appropriate population information from Gaia race/heritage lore.

Heritage supplies human-coded population tendencies such as:

* facial appearance
* complexion range
* common hair tendencies
* common eye tendencies
* ordinary height/build ranges

Use these only to fill genuinely unspecified information.

Individual authored traits override population tendencies.

---

#### Clothing and equipment

Primary source:

```yaml
equipment:
```

Follow references to the actual item records.

Never guess appearance from an item ID or item name.

---

#### Temporary state

Primary source:

the CURRENT SCENE.

This includes:

* current clothing overrides
* current hairstyle
* dirt
* blood
* wetness
* injuries
* expression
* pose
* action
* gaze
* held objects
* temporary transformations

Current scene state overrides habitual/default presentation.

---

#### Environment

Primary source:

1. explicit current scene location
2. `current_state.location`
3. resolved location record
4. canonical home or workplace explicitly associated with the character
5. regional fallback palette in this guide, only for standalone primary art

Resolve referenced locations rather than inventing generic scenery.

An exact scene or location record always overrides a regional fallback. Never
select a region from a name, occupation, race stereotype, or approximate match.

---


### 3. RACE LOOKUP IS MANDATORY


When a character has:

```yaml
race: Elf
```

look up the exact matching entry in:

```text
records/lore/races-and-peoples-of-gaia.md
```

For example:

```yaml
name: Elves
applies_to:
  - Elf
prompt: humanoid elf, pronounced pointed ears
invariant_traits:
  - humanlike proportions with clearly pointed ears
variable_traits:
  - build, skin tone, hair, eyes, and clothing follow the individual and culture
avoid:
  - ordinary rounded human ears
```

The useful positive racial information is therefore approximately:

```text
elf, pronounced pointed ears
```

Do NOT invent:

```text
pale elf
blonde elf
luminous skin
delicate elf
ethereal elf
slender elf
European elf
```

unless individual or heritage canon establishes those properties.

---


### 4. RACE REFERENCE FIELD BEHAVIOR


Each race reference has four different purposes.

#### `prompt`

Short positive model conditioning.

Use relevant concrete concepts from it.

Deduplicate against character information.

---

#### `invariant_traits`

Traits that should remain visibly true for that race when applicable.

Examples:

```text
pointed ears
webbed fingers
short adult stature
cat ears
slit pupils
```

Do not silently remove invariant morphology.

If an individual character record directly contradicts an invariant racial trait and no disguise, transformation, injury, or canonical exception explains it:

**report the conflict instead of guessing.**

---

#### `variable_traits`

Possibilities, NOT automatic prompt tags.

Example:

```yaml
variable_traits:
  - build, skin tone, hair, eyes, and clothing follow the individual and culture
```

This does NOT authorize inventing any of them.

Resolve them from:

```text
character → heritage → current scene
```

---

#### `avoid`

Validation information.

Do NOT place `avoid` phrases in the positive prompt.

Use them to check for likely incorrect rendering.

Example:

```yaml
avoid:
  - ordinary rounded human ears
```

means the positive prompt should adequately establish pointed ears.

It does NOT mean output:

```text
no rounded ears
```

---


### 5. CHARACTER OVERRIDES POPULATION BASELINE


Population baselines fill gaps.

They do not rewrite characters.

Example:

```yaml
race: Elf
heritage: Al-Khayzari

visual:
  skin: pale fair
  eyes: dark brown
  hair: black, long, elaborately styled
```

Even if Al-Khayzari population lore includes:

```text
olive skin
golden beige skin
bronze skin
warm brown skin
deep brown skin
```

Zahra remains:

```text
pale skin
dark brown eyes
long black hair
```

Do not average or blend population possibilities.

BAD:

```text
pale olive bronze skin
```

GOOD:

```text
pale skin
```

---


### 6. HERITAGE AND RACE ARE DIFFERENT LAYERS


Race primarily supplies inherited nonhuman anatomy.

Heritage supplies the character's broader human-coded population appearance.

For:

```yaml
race: Elf
heritage: Al-Khayzari
```

think:

```text
Al-Khayzari woman
+
elven racial anatomy
```

not:

```text
generic fantasy elf
+
desert costume
```

For an Al-Khayzari Elf with otherwise unspecified facial appearance, a concise visual anchor such as:

```text
West Asian facial features
```

may be appropriate.

Do not use heritage to replace individually authored skin, hair, eye, or body traits.

Resolve the face from explicit individual morphology first. When it is genuinely
unspecified, an exact canonical heritage may supply a restrained population
anchor: Tsukuyomi may use `Japanese facial features`; Sangguo may use `Chinese
facial features` or a more exact supported subpopulation; Hrafnland may use
`Scandinavian facial features`; and Al-Khayzari may use `West Asian facial
features`. Tide Archipelago, Verdanian, and Valdris characters require the most
specific supported population record rather than an invented blend of broad
alternatives. Avoid vague or culturally confused phrases such as `elven
features`, `beautiful elf face`, or `traditional Japanese facial features`;
race supplies concrete nonhuman morphology, while individual or heritage canon
supplies the face.

---


### 7. THE CAMERA TEST


Before including ANY phrase, ask:

**Could a camera see this in this image?**

If not:

REMOVE IT.

BAD:

```text
intelligent
independent
wealthy
secretive
experienced
hardworking
cautious with trust
in love with a djinn
```

None of these directly describe pixels.

Do not translate them into invented physical features.

BAD:

```text
intelligent → sharp intelligent eyes
hardworking → calloused hands
gardener → dirt on face
secretive → guarded expression
wealthy → ornate jewelry
```

Unless another canonical source explicitly establishes those visible details:

REMOVE THEM.

---


### 8. DESCRIBE WHAT, NOT WHY


Never explain why an appearance exists.

BAD:

```text
green-stained fingertips from handling herbs
```

GOOD:

```text
green-stained fingertips
```

BAD:

```text
scar from an old battle
```

GOOD:

```text
scar across cheek
```

BAD:

```text
strong arms from years of farm work
```

GOOD:

```text
defined arms
```

BAD:

```text
burn mark from touching the lamp too long
```

GOOD:

```text
faint burn mark on right palm
```

The cause belongs in biography.

The result belongs in the image prompt only when visible.

---


### 9. REMOVE HABIT LANGUAGE


Do not put habitual wording into prompts.

Remove:

```text
always
usually
normally
often
typically
constantly
perpetually
known for
has a habit of
```

BAD:

```text
always has leaves caught in her hair
```

If this exact image should visibly contain one:

```text
leaf in hair
```

Otherwise:

omit it.

BAD:

```text
usually touches the lamp while thinking
```

If the current scene says she is doing this:

```text
touching lamp
```

Otherwise:

omit it.

The prompt describes one frame, not recurring behavior.

---


### 10. SIMPLE LITERAL WORDING


Prefer short, concrete descriptions.

Do not make source wording more poetic.

BAD:

```text
warm bronze-brown sun-kissed skin
sun-warmed tan skin
```

GOOD:

```text
brown skin
light beige skin
```

or, when canon is more specific:

```text
reddish-brown skin
tan skin
```

BAD:

```text
deep luminous violet eyes
```

GOOD:

```text
violet eyes
```

BAD:

```text
luxurious flowing raven-black hair
```

GOOD:

```text
long black hair
```

BAD:

```text
soft natural earthy face
```

GOOD:

use actual visible facial features, or omit.

Do not add decorative adjectives merely to improve prose.

---


### 11. NO ADJECTIVE INFLATION


Avoid automatically adding:

```text
beautiful
gorgeous
stunning
perfect
elegant
ethereal
luminous
radiant
earthy
natural
graceful
striking
exotic
rich
luxurious
breathtaking
```

unless that word conveys a necessary concrete visual property.

Do not convert:

```text
pale fair
```

into:

```text
soft luminous porcelain complexion
```

Prefer:

```text
pale skin
```

---


### 12. STRUCTURED FIELD LITERALIZATION


Structured character fields may contain both physical information and interpretation.

Extract only the visible information.

#### BODY

SOURCE:

```text
tall and graceful, small breasts
```

USE:

```text
tall, small breasts
```

DROP:

```text
graceful
```

---

#### EYES

SOURCE:

```text
dark brown, intelligent and guarded
```

USE:

```text
dark brown eyes
```

DROP:

```text
intelligent
guarded
```

---

#### HAIR

SOURCE:

```text
black, long, elaborately styled
```

USE:

```text
long black hair, elaborate hairstyle
```

Do not output:

```text
black, long, elaborately styled hair
```

Bind adjectives clearly to the object they modify.

---

#### SKIN

SOURCE:

```text
pale fair
```

USE:

```text
pale skin
```

---

#### FACE

SOURCE:

```text
symmetrical, elegant elven features, pointed ears
```

First resolve the race reference.

If Elf canon already supplies:

```text
pronounced pointed ears
```

do not duplicate it.

Drop weak subjective descriptors such as:

```text
symmetrical
elegant elven features
```

unless they represent genuinely specific individual morphology.

#### Height and visible age

Never place a raw fantasy age or exact real-world height in the prompt unless
the number itself is visually relevant. Convert age to `young adult`, `adult`,
`mature`, `middle-aged`, or `elderly` as canon requires. Convert measurements to
useful categories such as `short stature`, `average height`, or `tall` only when
height can read in the selected composition. Height is most useful in full-body,
multi-character, or clearly scaled environmental images.

---


### 13. DO NOT DERIVE PHYSICAL FEATURES FROM BIOGRAPHY


Biography and `gm_notes` explain who a character is.

They do not automatically supply visual prompt tokens.

Do NOT infer:

```text
gardener → leaf in hair
gardener → green fingertips
gardener → dirty clothes

blacksmith → soot on face
blacksmith → muscular arms

soldier → scars
soldier → weathered face

scholar → glasses

traveler → muddy boots
traveler → worn clothes

wealthy → jewelry

noble → perfect posture
```

These details must come from explicit character, item, scene, or location data.

Do not manufacture evidence of someone's occupation or history.

---


### 14. APPEARANCE PROSE IS SECONDARY


Top-level:

```yaml
appearance:
```

may contain useful canonical information, but it often mixes:

* physical appearance
* clothes
* behavior
* personality
* social interpretation

Separate these before prompting.

Example:

```text
Elegant and self-possessed in gold-trimmed robes with the al-Dhahab sigil,
she carries herself with the ease of someone who has never needed to please
anyone. She has a habit of touching the family lamp at her belt when thinking.
```

Potentially usable:

```text
gold trim
al-Dhahab sigil
```

but equipped clothing records are more authoritative for the actual garment.

Do not automatically use:

```text
elegant
self-possessed
independent
habitually touching lamp
```

---


### 15. EQUIPMENT REFERENCES MUST BE RESOLVED


Before finalizing a character image prompt, inspect relevant equipped item references.

Example:

```yaml
equipment:
  clothing:
    - item:crossover-desert-robe
  hands:
    right: item:djinn-lamp
```

You MUST read:

```text
item:crossover-desert-robe
item:djinn-lamp
```

before describing them.

Never guess from the ID.

BAD:

```text
crossover desert robe
embroidered borders
brass djinn lamp
```

unless those exact properties are supported by the item records.

The actual item record determines:

* material
* color
* shape
* construction
* trim
* visible components
* wear
* ornamentation

---


### 16. CLOTHING RESOLUTION PRIORITY


Resolve visible clothing in this order:

1. explicit CURRENT SCENE clothing
2. currently equipped `equipment.clothing`
3. currently equipped armor
4. explicit canonical default outfit
5. conservative fallback only when absolutely necessary

Do not choose clothing simply because it fits the occupation.

BAD:

```text
ranger → green cloak and leather armor
```

GOOD:

open the ranger's equipped item references.

---


### 17. UNDERWEAR IS NOT AUTOMATICALLY VISUAL


Equipment under:

```yaml
equipment:
  underwear:
```

is simulation/inventory data unless established as visible.

Do NOT include or resolve underwear for normal clothed images.

Example:

```yaml
underwear:
  - item:womens-long-cotton-chemise
  - item:womens-cotton-underdrawers
clothing:
  - item:crossover-desert-robe
```

For a normal clothed image:

resolve the robe.

Do not prompt:

```text
chemise
underdrawers
underwear
```

unless the current image explicitly exposes them or the underwear itself is the subject.

The prompt is not a complete inventory list.

---


### 18. VISIBLE CLOTHING LAYERS ONLY


Even when an equipped garment exists, include it only if the camera can see it.

Example layers:

```text
undershirt
tunic
cloak
```

If the cloak and tunic completely cover the undershirt:

omit the undershirt.

If the neckline exposes part of it:

it may be included.

Describe visible pixels, not hidden clothing stacks.

---


### 19. EQUIPPED DOES NOT ALWAYS MEAN VISIBLE


Characters may carry many items.

Do not dump all equipment into the prompt.

Include items only when they are:

* worn and visible
* held
* actively used
* carried visibly
* explicitly placed in the scene

Do not describe absent inventory with negative positive-prompt tokens such as
`holding nothing`, `empty hands`, `no weapon`, `no hat`, or `no jewelry`.
Simply omit what is absent.

Example:

```yaml
hands:
  right: item:djinn-lamp
```

means the lamp is likely visually relevant.

Resolve the lamp record.

Then use something like:

```text
holding <resolved lamp description> in right hand
```

if the hand and lamp are visible in the composition.

---


### 20. DISTINCTIVE FEATURES REQUIRE VISIBILITY


Canonical distinctive features remain canonical but are not mandatory in every image.

Example:

```yaml
distinctive_features:
  - gold-tower sigil tattoo inside left wrist
  - faint burn mark on right palm
```

Include the wrist tattoo only when the inside of the left wrist can reasonably be seen.

Include the palm mark only when the right palm is actually exposed.

Holding an object does NOT automatically make the palm visible.

Do not distort the pose merely to show every character-sheet detail.

Every micro-detail must pass both tests: the selected camera can resolve it,
and it materially improves identity or the requested scene. Warning words such
as `faint`, `barely visible`, `tiny`, `subtle`, `minute`, `nearly invisible`,
or `minor discoloration` normally indicate that the detail should be removed
from full-body and cowboy-shot prompts. A micro-detail may survive when the
framing clearly exposes it, it is identity-critical, or the user requests it.
The prompt is not a forensic inventory.

---


### 21. CHOOSE IMAGE MODE FIRST


Before constructing the prompt, determine the requested image mode.

Possible modes include:

```text
PRIMARY / BACKGROUND CHARACTER IMAGE
PORTRAIT IMAGE
NEUTRAL CHARACTER CUTOUT
CURRENT SCENE IMAGE
```

Composition rules differ by mode.

Never copy a portrait composition wholesale into a background image.
Do not reuse one identical prompt for primary, portrait, cutout, and scene
generation; preserve identity while rebuilding mode-specific composition.

---


### 22. PRIMARY / BACKGROUND CHARACTER IMAGE


Stored in:

```yaml
image:
  url:
```

The primary image should normally show the character existing inside their world.

Prefer:

```text
full body
cowboy shot
```

or another approximately three-quarter-body composition.

Default priority:

1. full body when outfit, stance, environment, or equipment matters
2. cowboy shot / three-quarter body when stronger face visibility is useful
3. upper body only when the scene specifically calls for it
4. close-up only for intentionally close emotional scenes

Do NOT default background images to:

```text
portrait
upper body
close-up
looking at viewer
```

---


### 23. BACKGROUND IMAGE GAZE


Do not automatically add:

```text
looking at viewer
```

to primary/background images.

Gaze should follow the scene.

Examples:

Reading:

```text
looking down at book
```

Examining lamp:

```text
looking at lamp
```

Speaking to another character:

```text
looking at other character
```

Walking:

```text
looking ahead
```

If gaze is irrelevant:

omit it.

Background images should feel like a moment occurring in the world rather than a character posing for identification.

---


### 24. PORTRAIT IMAGE


Stored in:

```yaml
image:
  portrait:
    url:
```

Portraits are for character identification.

Prefer:

```text
portrait
upper body
```

or:

```text
chest-up
```

The face should be clear.

When no scene-specific expression is required, acceptable defaults include:

```text
looking at viewer
neutral expression
```

`looking at viewer` is therefore acceptable as a PORTRAIT default.

It is not a BACKGROUND default.

---


### 25. NEUTRAL CHARACTER CUTOUT


A neutral character cutout is meant for compositing.

Prefer:

```text
full body
standing
neutral pose
neutral expression
```

Use visible canonical clothing.

Avoid:

* scene-specific action
* dramatic perspective
* strong environment interaction
* furniture obscuring the body
* unnecessary props

The final background-removed asset must retain a clean readable silhouette.

---


### 26. CURRENT SCENE OVERRIDES DEFAULT PRESENTATION


If the current scene specifies:

```text
hair loose
blue festival robe
wet clothing
kneeling
angry expression
looking at another character
```

those override habitual/default presentation.

Example:

Character normally:

```text
hair tied back
```

Current scene:

```text
hair loose after waking
```

Prompt:

```text
loose hair
```

Do not include both.

---


### 27. FRAME BEFORE MICRO-DETAILS


Choose:

1. action
2. pose
3. framing
4. viewpoint

before adding tiny details.

Then ask whether the camera could actually resolve them.

For:

```text
full body
```

usually omit:

```text
tiny finger scar
small nail detail
faint palm mark
tiny earring engraving
```

unless unusually important and visible.

For:

```text
close-up
```

those may matter.

Never change the composition merely to expose every micro-detail.

Use the action actually occurring. Do not add `dynamic action pose`, `heroic
pose`, `cinematic pose`, `dramatic pose`, or `battle stance` unless the scene
requires it. For ordinary scenes prefer believable actions such as standing,
walking, sitting, kneeling, leaning against a wall, working at a table, holding
a cup, reading, or looking over a shoulder.

Choose one coherent framing strategy. Useful terms include `full body`,
`cowboy shot`, `upper body`, `close-up`, `wide shot`, `three-quarter view`,
`from side`, `from behind`, `high angle`, and `low angle`. Remove combinations
such as `close-up, full body`, `portrait, wide environmental shot`, or `neutral
pose, dynamic action pose`.

---


### 28. DANBOORU-FIRST, NOT DANBOORU-ONLY


Prefer recognized concise tags where they express the concept accurately.

Example:

```text
1girl, solo, adult woman, elf, pointed ears, dark brown eyes, long black hair
```

Use short natural-language phrases when a specific visual detail cannot be expressed clearly through tags.

Example:

```text
gold-tower tattoo inside left wrist
```

Do not force awkward fake tags.

Do not use narrative sentences.

Do not automatically include an original RPG character name. Omit names such
as `Aerindra`, `Zahra`, `Kenji`, or `Thalor` unless the name is a recognized
character, LoRA trigger, embedding, or other deliberate model keyword.
Describe the actual appearance instead.

Avoid redundant subject tags: use `1girl, solo`, not `1girl, solo, female
focus`; use `1boy, solo`, not `1boy, solo, male focus`. Focus tags are useful
only when multiple subjects make the focus ambiguous.

---


### 29. OCCUPATION LABELS ARE OPTIONAL


Role/class names can encourage stereotypical inventions.

Prefer concrete visible evidence.

LESS USEFUL:

```text
herbalist
```

BETTER:

```text
herb basket, pruning shears, herb garden
```

LESS USEFUL:

```text
blacksmith
```

BETTER:

```text
leather work apron, hammer, iron anvil, forge
```

A role tag may remain when it genuinely improves conditioning, but actual clothing, equipment, action, and environment are more important.

---


### 30. COLORS MUST ATTACH TO OBJECTS


BAD:

```text
brown, gold, black, pale
```

GOOD:

```text
brown eyes, gold trim, black hair, pale skin
```

Do not leave visual attributes unattached.

---


### 31. SPECIFICITY WITHOUT SYNONYM STACKING


BAD:

```text
slender, slim, thin, lean, graceful body
```

GOOD:

```text
slender build
```

BAD:

```text
beautiful face, gorgeous face, attractive face, perfect face
```

GOOD:

use actual facial morphology, or omit.

One useful concept is better than four near-synonyms.

---


### 32. ENVIRONMENT MUST BE CONCRETE


When environment matters, resolve the actual location.

BAD:

```text
fantasy environment
detailed setting
environmental context
```

GOOD:

```text
stone courtyard, arched colonnade, tiled fountain, date palms
```

Use details supported by the location record.

Do not invent major landmarks.

#### Never output in-world fantasy place names

Image generation models (such as ComfyUI checkpoints) have no knowledge of
in-world fantasy geography. Names such as `Verdania`, `Zaffar`, `Valdris`,
`Tsukuyomi`, or `Sangguo` produce unpredictable artifacts or are ignored. Always
translate location lore into generic, recognizable physical tags.

BAD:

```text
verdania forest background
zaffar stone courtyard
crossford market
```

GOOD:

```text
forest background
stone courtyard
busy market square
```

A primary/background character image should normally contain a real, supported
environment. No current scene does not mean no background; use an isolated
character composition only when explicitly requested.

#### Environment fallback hierarchy

Use the first available source:

1. explicit current-scene environment
2. resolved `current_state.location`
3. resolved canonical home or workplace explicitly associated with the character
4. one regional fallback palette below

The regional palettes are last-resort world context, not new canon. Choose one
coherent environment type—urban, village, rural, forest, mountain, river,
coastal, or desert—and use about three to six compatible elements. Do not mix
unrelated environments or dump a whole palette into one prompt. Character
context may select among supported environment types but may not invent wear,
marks, clothing, equipment, or other traits on the character.

#### Regional fallback palettes

- **Tsukuyomi:** temperate Japanese settlements, farming country, fishing
  communities, forested hills, or mountains. Draw from wooden Japanese houses,
  plaster walls, dark timber beams, tiled roofs, narrow village streets, stone
  paths, wooden bridges, rice fields, irrigation channels, vegetable plots,
  cedar forest, bamboo grove, wooded hills, mountain paths, riverbanks, fishing
  harbours, wooden docks, or coastal villages. Suitable conditions include soft
  morning daylight, overcast daylight, mist, late-afternoon sunlight, or light
  rain. Do not add cherry blossoms, Mount Fuji, torii, shrines, pagodas, or
  samurai unless canon supports them.
- **Sangguo:** settled historical Chinese riverlands, canals, rice agriculture,
  mountain regions, or inland frontiers. Draw from Chinese timber buildings,
  tiled roofs, stone courtyards, market streets, canals, stone canal walls,
  arched bridges, riverbanks, rice paddies, irrigation channels, wooden docks,
  bamboo, misty mountains, highland trails, rocky slopes, or pine-covered hills.
  Suitable conditions include misty morning, humid or overcast daylight, soft
  afternoon light, or mountain fog. Do not add an imperial palace, Great Wall,
  dragons, lantern festivals, or ornate temples unless supported.
- **Hrafnland:** cold northern coasts, fjords, rocky mountains, conifer forests,
  or windy settlements. Draw from timber longhouses, wooden villages, steep
  roofs, stone foundations, fjord shorelines, rocky coasts, wooden piers, dark
  seawater, pine or spruce forest, snow-dusted mountains, rocky valleys,
  grass-covered slopes, cold rivers, or stone trails. Suitable conditions
  include cold overcast daylight, low northern sunlight, mist, light snow, wind,
  or grey coastal daylight. Do not add Viking ships, horned helmets, blizzards,
  or a fully frozen landscape unless supported; Hrafnland is not always snowy.
- **Al-Khayzar:** desert-edge cities, oases, caravan routes, mountain settlements,
  or coastal trade cities. Urban elements may include sandstone or pale-stone
  walls, arches, shaded courtyards, stone-paved streets, covered markets, fabric
  awnings, wooden shutters, flat roofs, carved screens, or courtyard fountains.
  Other supported choices include rocky desert, scrub, date palms, oasis pools,
  irrigation channels, dry hills, caravan roads, brown cliffs, stone harbours,
  wooden docks, blue coastal water, distant merchant vessels, or seaside markets.
  Use bright dry daylight, shaded-courtyard light, warm late-afternoon sunlight,
  or golden evening light as appropriate. Do not default to camels, pyramids,
  belly dancers, endless dunes, or ornate palaces.
- **Tide Archipelago:** tropical islands, coastal settlements, seafaring
  communities, or lush interiors. Draw from tropical shorelines, clear coastal
  water, wooden piers, outrigger-style boats, island harbours, raised wooden
  houses, palms, dense tropical vegetation, volcanic rock, sandy paths, coral or
  rocky beaches, green hills, or distant islands. Suitable conditions include
  bright tropical daylight, humid overcast daylight, coastal sunset, passing
  tropical clouds, or light sea mist. Do not add flower leis, grass skirts,
  surfboards, or resort scenery unless supported.
- **Verdania:** tropical rivers, rainforest, river cities, humid lowlands, or
  estuaries. Draw from broad rivers, dense canopy, massive trees, roots, ferns,
  vines, mossy stones, muddy banks, canoes, forest trails, riverfront settlements,
  wooden docks, timber river buildings, raised walkways, open-air markets,
  canals, wooden bridges, hanging vines, dense understory, or humid forest mist.
  Suitable conditions include humid or diffused daylight, dappled sunlight,
  tropical overcast, light rain, or morning mist. Do not add tribal costume,
  feather headdresses, body paint, tattoos, or ritual markings without explicit
  support, and do not assume every Verdanian location is deep jungle.
- **Valdris:** broad medieval towns, cities, farmland, forests, mountains, or
  trade roads. Draw from stone-and-timber or half-timber buildings, stone streets,
  market squares, wooden storefronts, arches, city walls, stone bridges, public
  fountains, merchant stalls, farmland, wheat fields, pasture, hedgerows, dirt
  roads, stone farmhouses, fences, deciduous forest, rolling hills, river valleys,
  rocky highlands, pine forest, mountain passes, or distant peaks. Suitable
  conditions include temperate or overcast daylight, morning or late-afternoon
  light, light fog, or light rain. Do not make every scene English, Gothic,
  castle-centered, or uniformly pale.

---


### 33. LIGHTING FOLLOWS THE SCENE


Use lighting only when supported by:

* time of day
* weather
* indoor light source
* current location
* scene instruction

Examples:

```text
morning light
overcast daylight
candlelight
firelight
moonlight
sunlight through window
```

Do not automatically add:

```text
cinematic lighting
dramatic lighting
soft lighting
rim lighting
```

merely because they sound attractive.

Do not add generic `soft lighting` merely because no lighting was supplied.
Use lighting supported by the resolved environment or its regional fallback.

---


### 34. NO GLOBAL QUALITY LANGUAGE


The GLOBAL STYLE prompt handles quality and artistic style.

Do not add:

```text
masterpiece
best quality
amazing quality
very aesthetic
absurdres
highres
8k
high resolution
professional artwork
award-winning
beautifully rendered
highly detailed
```

Do not repeat the art medium.

---

### Additional prompt controls and subject types

#### Prompt weighting

Normally use unweighted tags. Use ComfyUI weighting only when an
identity-critical feature repeatedly fails or the source explicitly marks it as
critical. Prefer weights from `1.05` to `1.20`, and use up to about `1.30` only
when genuinely necessary. Do not weight large portions of a prompt or add
parentheses merely for sophistication.

#### Multiple characters

Establish the subject count, gender mix, relative positions, each character's
identity and visible clothing/equipment, interaction, and gaze. Keep every trait
attached to its character with relational phrases such as `blonde elf woman on
left` and `dark-haired human man on right`; do not provide an unordered pile of
hair, eye, and clothing tags that can bleed between subjects. Do not introduce
extra people unless the scene requires them.

#### Item and memento prompts

For an object image, do not insert character tags. Store only item-specific
content in `visual.prompt`, prioritizing object type, shape, material,
construction, craftsmanship, texture, wear, damage, engraving, color, and
distinctive components. Do not add people, character-count tags, mannequins,
wearers, hangers, scenery, borders, frames, pedestals, global style, or quality
terms. The item generator separately supplies centered isolated presentation,
full-object framing, white background, borderless treatment, no-human handling,
and ghost-mannequin volume for wearables. An item-specific camera angle may
remain only when necessary to reveal its construction.

Example:

```text
elven hunting knife, narrow leaf-shaped steel blade, carved ashwood handle, silver wire wrapping, worn leather sheath, chip near blade tip, engraved vine motif
```

#### Location prompts

Focus entirely on the environment and do not add characters unless required by
the source scene. Prioritize architecture, geography, terrain, vegetation,
materials, weather, lighting, scale, foreground, midground, background, and
visible environmental activity. Use one coherent framing such as a wide
establishing shot.

Example:

```text
mountain monastery, pale stone buildings built into cliffside, narrow stairways, cedar roofs, pine forest below, distant snow-covered peaks, low clouds, morning mist, wide establishing shot
```

#### Map prompts

Describe actual geography using concepts such as `fantasy map`, `top-down view`,
`illustrated terrain`, mountain ranges, rivers, forests, roads, villages,
fortresses, coastlines, islands, farmland, and valleys. Do not automatically add
parchment, aged paper, scrolls, compass roses, decorative borders, ornamental
frames, or text labels. Request labels only when specifically necessary because
image models are unreliable at precise map typography.

---


### 35. CHARACTER PROMPT ORDER


Build character prompts roughly in this order:

1. subject count
2. gender
3. visible age category
4. race
5. invariant racial morphology
6. heritage facial/population anchor only when needed
7. body/build
8. skin
9. face
10. eyes
11. hair
12. character-specific anatomy/markings
13. visible resolved clothing
14. visible resolved equipment
15. current action
16. pose
17. expression
18. gaze
19. framing
20. immediate surroundings
21. larger environment
22. supported lighting/weather
23. clearly visible, useful identity details

The order is a guideline.

Do not duplicate traits simply because they appear in more than one source.

---


### 36. MINIMUM SUFFICIENT PROMPT


Use the smallest prompt that clearly establishes:

```text
WHO
WHAT THEY LOOK LIKE
WHAT THEY ARE WEARING
WHAT THEY ARE DOING
WHERE THEY ARE
HOW THE IMAGE IS FRAMED
```

Then stop.

Do not use every fact available.

More words are not automatically better.

One Obsession should receive clear visual conditioning rather than an illustrated biography.

#### Final stored-value format

Store exactly one comma-separated positive prompt in `visual.prompt`. The value
must contain no paragraphs, Markdown, explanatory text, `Prompt:` label,
quotation marks added as prompt content, negative prompt, or quality boilerplate.

---


### 37. NO UNSOURCED TOKENS


Every descriptive phrase must be traceable to:

1. canonical character fields
2. exact racial reference
3. heritage/population fallback
4. resolved equipped item
5. current scene
6. resolved location
7. regional fallback palette, only when the location hierarchy reaches it
8. explicit image-mode composition rule

If you cannot identify why a phrase is present:

REMOVE IT.

Examples requiring a real source:

```text
embroidered borders
brass lamp
gold earrings
dusty boots
leaf in hair
weathered hands
soft lighting
```

Plausible is not enough.

---


### 38. SOURCE CONFLICTS


If two canonical sources materially disagree:

DO NOT silently choose one.

Examples:

* race machine-readable reference contradicts race prose
* item visual fields contradict character appearance
* current equipped item contradicts an authored current outfit
* character race contradicts invariant morphology

Prefer an explicit current-scene override when the contradiction is clearly temporary.

Otherwise report the canonical conflict for author review.

Do not invent a compromise.

---


### 39. FINAL LITERALIZATION PASS


Before saving the prompt, inspect every comma-separated phrase.

For each phrase ask:

#### Is this visible?

If no → REMOVE.

#### Is this current?

If it describes a habit instead of this image → REMOVE or convert to the explicit current state.

#### Does it explain why something exists?

If yes → remove the explanation.

#### Did it come from biography interpretation?

If yes → REMOVE unless separately canonical.

#### Did I resolve the referenced clothing/item?

If no → RESOLVE IT FIRST.

#### Is it hidden beneath other clothing?

If yes → REMOVE.

#### Is it outside the selected camera frame?

If yes → REMOVE.

#### Is it visually useful at this scale?

If it is faint, tiny, subtle, or unlikely to affect the generated pixels →
REMOVE unless it is identity-critical or specifically requested.

#### Did I add decorative adjectives?

If yes → SIMPLIFY.

#### Is another phrase saying the same thing?

If yes → DEDUPLICATE.

#### Does it conflict with race morphology?

If yes → RESOLVE THE SOURCE CONFLICT.

#### Does gaze match image mode?

Background → scene-natural gaze.

Portrait → looking at viewer may be default.

#### Is the environment concrete and source-backed?

Replace vague terms such as `environmental context`, `fantasy setting`,
`regional background`, or `nearby surfaces` with supported drawable objects.

#### Is the token redundant or describing an absence?

Remove duplicate subject/focus concepts and positive-prompt negatives such as
`female focus` after `1girl, solo`, `holding nothing`, or `no weapon`.

---


### 40. ZAHRA EXAMPLE


Character:

```yaml
race: Elf
heritage: Al-Khayzari
gender: Female
age: 30

equipment:
  underwear:
    - item:womens-long-cotton-chemise
    - item:womens-cotton-underdrawers
  clothing:
    - item:crossover-desert-robe
  hands:
    right: item:djinn-lamp

visual:
  body_build: tall and graceful, small breasts
  skin: pale fair
  hair: black, long, elaborately styled
  eyes: dark brown, intelligent and guarded
  face: symmetrical, elegant elven features, pointed ears
```

#### STEP 1 — Literal individual traits

Extract:

```text
adult woman
tall
small breasts
pale skin
dark brown eyes
long black hair
elaborate hairstyle
```

Drop:

```text
graceful
intelligent
guarded
symmetrical
elegant
```

---

#### STEP 2 — Resolve race

Exact match:

```yaml
race: Elf
```

against:

```yaml
applies_to:
  - Elf
```

Race adds:

```text
elf
pronounced pointed ears
```

Do not invent other elven traits.

---

#### STEP 3 — Resolve heritage

Al-Khayzari provides the appropriate West Asian population baseline.

Zahra already specifies skin, eyes, and hair.

Do not override them.

If no individual facial morphology is otherwise specified beyond vague `elegant elven features`, a concise fallback may be:

```text
West Asian facial features
```

---

#### STEP 4 — Resolve clothing

Open:

```text
item:crossover-desert-robe
```

Use the item's actual visible description.

Do not guess from the item name.

---

#### STEP 5 — Resolve held item

Open:

```text
item:djinn-lamp
```

Use its actual visible description.

Do not assume:

```text
brass
ornate
engraved
gold
```

unless the item record says so.

---

#### STEP 6 — Ignore hidden underwear

Do NOT add:

```text
chemise
underdrawers
underwear
```

for a normally clothed image.

---

#### STEP 7 — Resolve location

If generating the primary/background image and:

```yaml
current_state:
  location: location:zaffar
```

resolve:

```text
location:zaffar
```

and use concrete visible environment details.

---

#### STEP 8 — Choose PRIMARY composition

Prefer:

```text
full body
```

or:

```text
cowboy shot
```

Do not automatically add:

```text
portrait
upper body
looking at viewer
```

---

#### SAFE PRIMARY IMAGE STRUCTURE

After references are resolved:

```text
1girl, solo, adult woman, elf, pronounced pointed ears, West Asian facial features, tall, small breasts, pale skin, dark brown eyes, long black hair, elaborate hairstyle, <resolved robe>, holding <resolved djinn lamp> in right hand, full body, <current action>, <natural scene gaze>, <resolved Zaffar environment>
```

If approximately three-quarter framing works better:

```text
1girl, solo, adult woman, elf, pronounced pointed ears, West Asian facial features, tall, small breasts, pale skin, dark brown eyes, long black hair, elaborate hairstyle, <resolved robe>, holding <resolved djinn lamp> in right hand, cowboy shot, three-quarter view, <current action>, <natural scene gaze>, <resolved environment>
```

Do not add unsupported details.

---

#### SAFE PORTRAIT STRUCTURE

```text
1girl, solo, adult woman, elf, pronounced pointed ears, West Asian facial features, pale skin, dark brown eyes, long black hair, elaborate hairstyle, <visible upper portion of resolved robe>, portrait, upper body, looking at viewer, neutral expression
```

The portrait and primary image share CHARACTER IDENTITY.

They do not share COMPOSITION.

---


### 41. CORE PROMPTING FORMULA


Always follow:

```text
CANONICAL CHARACTER
+
EXACT RACE ANATOMY
+
HERITAGE FALLBACK ONLY FOR GAPS
+
RESOLVED VISIBLE CLOTHING/EQUIPMENT
+
CURRENT SCENE
+
CORRECT IMAGE MODE
+
VISIBILITY FILTER
```

Never follow:

```text
BIOGRAPHY
→ INTERPRETATION
→ STEREOTYPE
→ EMBELLISHMENT
```

Final principle:

**Describe the picture, not the lore behind the picture.**
