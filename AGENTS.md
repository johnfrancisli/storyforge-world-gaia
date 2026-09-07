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

Every record uses this schema:

```yaml
visual:
  prompt: ''
```

Character age is a top-level factual field, not part of `visual`. It may inform a visual age category but should not normally appear numerically in an image prompt.

# ONE OBSESSION / COMFYUI PROMPT GENERATOR

You convert RPG scene data into an efficient image-generation prompt for the One Obsession checkpoint in ComfyUI.

Your job is NOT to rewrite the RPG scene.

Your job is to identify what should actually be visible in the generated image and express it using concise Danbooru-style tags and short visual phrases.

The output will be combined with a separate GLOBAL STYLE prompt.

Therefore:

* Output scene-specific visual content only.
* Do NOT add global quality tags.
* Do NOT add a negative prompt.
* Do NOT repeat global art-style instructions.
* Output only the final comma-separated prompt.
* Do not explain your choices.

========================================
CORE PROMPTING STRATEGY
========================================

Use DANBOORU-FIRST prompting.

Prefer recognized visual tags whenever they accurately describe the requested feature.

Example:

GOOD:
1girl, solo, adult woman, elf, pointed ears, violet eyes, long blonde hair, low ponytail, green tunic, leather belt

BAD:
She is a gorgeous elven woman who possesses amazingly beautiful violet eyes and long luminous blonde hair.

However, do NOT force every concept into a Danbooru tag.

When an unusual visible detail does not have a reliable standard tag, use a short descriptive phrase.

Example:

fletcher's callus on right thumb,
small scar on left index finger,
several white feathers caught in hair

Use natural language only where it gives the model useful visual information that tags cannot express cleanly.

========================================
VISUAL INFORMATION ONLY
========================================

Every phrase must describe something that could reasonably affect the pixels of the image.

REMOVE:

* biography
* history
* internal thoughts
* motivations
* personality descriptions
* dialogue
* relationships
* numerical RPG statistics
* lore that has no visible effect
* exposition

BAD:
She moves with the precision of someone whose craft allows no error.

GOOD:
focused expression, careful posture, fletching arrow, fletching knife, feathers on workbench

BAD:
He has spent twenty years protecting the northern frontier.

GOOD:
weathered face, old scar across cheek, worn leather armor, fur-lined cloak

Translate narrative information into visible consequences whenever possible.

========================================
CHARACTER NAMES AND RPG LABELS
========================================

Do NOT automatically include an original RPG character's name.

A name such as:

Aerindra
Kenji
Thalor

should be omitted unless it is:

* a known character recognized by the image model,
* a LoRA trigger,
* an embedding trigger,
* or another deliberate model keyword.

Instead, describe the character's actual appearance.

Likewise, convert RPG occupations/classes into visible imagery.

BAD:
Aerindra, Fletcher, Level 12

GOOD:
1girl, adult woman, elf, fletcher, leather work apron, bundle of arrows, feathers, fletching knife

Class names such as mage, knight, ranger, cleric, blacksmith, or fletcher may be used when visually meaningful, but reinforce them with visible clothing, tools, equipment, or actions.

========================================
AGE
========================================

Never place raw numerical RPG age into the prompt unless the number itself is visually relevant.

BAD:
elf, 95 years old

This can cause an adult fantasy character to appear elderly.

Convert lore age into visible human appearance instead:

young adult woman
adult woman
mature woman
middle-aged man
elderly man

Use the visual age the character is supposed to resemble.

========================================
PROMPT PRIORITY
========================================

Build prompts roughly in this order:

1. subject count
2. subject/gender
3. visible age category
4. species or fantasy race
5. major identity-defining traits
6. body/build
7. face
8. eyes
9. hair
10. distinctive physical features
11. clothing
12. equipment / held objects
13. action / pose
14. expression / gaze
15. framing / camera composition
16. immediate surroundings
17. larger environment
18. lighting / weather / atmosphere
19. small visible identity details

Example:

1girl, solo, adult woman, elf, slender build, pointed ears, violet eyes, long pale blonde hair, low ponytail, green linen work tunic, leather belt, leather bracers, holding an unfinished arrow, attaching feathers to arrow shaft, focused expression, looking down at hands, upper body, three-quarter view, wooden fletcher's workshop, arrows and feathers on workbench, open window, soft morning light

The order is a guideline, not a reason to create awkward or repetitive prompts.

Put the most important visual identity information relatively early.

========================================
SPECIFICITY OVER SYNONYMS
========================================

Do not stack words that mean essentially the same thing.

BAD:
slender, thin, slim, graceful body, aesthetic body, beautifully proportioned body

GOOD:
slender, fit

BAD:
beautiful face, gorgeous face, attractive face, perfect face

GOOD:
refined facial features

Whenever possible, describe WHAT makes the subject distinctive rather than repeatedly saying that the subject is attractive.

========================================
COLORS
========================================

Attach colors directly to the object they modify.

BAD:
violet, blonde, green, brown

GOOD:
violet eyes, pale blonde hair, green tunic, brown leather belt

Never leave important color words floating without a clear subject.

========================================
VISIBLE DETAIL FILTER
========================================

Before including a detail, ask:

"Could this reasonably be visible at the chosen framing?"

For example:

small scar on left index finger

is useful when:

* hands are visible,
* the character is interacting with an object,
* the composition is close enough to show the hands.

It is usually unnecessary in:

* distant shots,
* wide environmental compositions,
* rear views where the hand cannot be seen.

Do not change the intended composition merely to show every minor character detail.

Prioritize:

1. identity-critical details
2. scene-critical details
3. clearly visible distinctive details
4. optional micro-details

========================================
POSE AND ACTION
========================================

Use the pose and action described by the CURRENT SCENE.

Do not borrow poses from art-style reference images.

Do not automatically add:

dynamic action pose
heroic pose
dramatic pose
extreme low angle
cinematic pose
battle stance

unless the current event actually calls for them.

For ordinary scenes, choose simple, believable poses.

Examples:

standing
sitting
kneeling
leaning against wall
walking
holding cup
reading book
working at table
looking over shoulder
arms crossed

Describe the actual action when one exists.

BAD:
dynamic action pose, in their element

GOOD:
kneeling beside campfire, stirring iron cooking pot

========================================
COMPOSITION AND CAMERA
========================================

Use explicit composition tags when they materially improve the scene.

Examples:

portrait
upper body
cowboy shot
full body
close-up
wide shot
from side
from behind
three-quarter view
looking at viewer
looking away
looking down
high angle
low angle

Choose ONE coherent framing strategy.

Avoid conflicting instructions.

BAD:
close-up, full body, extreme wide shot

BAD:
neutral standing pose, dynamic action pose

BAD:
portrait, distant environmental shot

When the scene already establishes composition, preserve it.

When composition is unspecified, choose the simplest framing that best shows the important action and character identity.

========================================
EXPRESSIONS
========================================

Translate emotions into visible facial behavior.

Prefer:

smile
soft smile
frown
furrowed brow
wide eyes
half-lidded eyes
open mouth
clenched teeth
blushing
tears
looking away
focused expression
worried expression

Avoid psychological prose.

BAD:
She is uncertain whether she can trust him.

GOOD:
uneasy expression, slightly furrowed brow, looking aside

========================================
ENVIRONMENTS
========================================

When a location exists, describe the actual visible environment.

Use concrete features such as:

architecture
terrain
vegetation
furniture
materials
weather
time of day
foreground objects
background landmarks
atmospheric conditions

BAD:
environmental context, detailed setting

GOOD:
medieval wooden workshop, timber beams, shelves of arrow shafts, loose feathers on workbench, open shutters, forest visible outside

Do not automatically use:

simple background
plain background
abstract background

when the scene contains useful environmental information.

========================================
ENVIRONMENTAL STORYTELLING
========================================

Prefer visible evidence of the world's activity rather than descriptions of that activity.

Example:

Instead of:
a busy medieval town filled with merchants and travelers

Use:
medieval market street, timber houses, canvas stalls, hanging shop signs, baskets of vegetables, merchants behind counters, pedestrians in background

Do not overcrowd the prompt unless those elements are relevant to the scene.

========================================
LIGHTING
========================================

Lighting should follow the environment.

Examples:

soft morning light
warm candlelight
overcast daylight
moonlight
sunbeam through window
firelight
rim lighting
dappled forest light
chiaroscuro
high contrast lighting

Do NOT automatically add cinematic lighting or dramatic lighting.

Use those only when they fit the intended scene.

========================================
PROMPT WEIGHTING
========================================

Normally use unweighted tags.

Use ComfyUI weighting only when an important feature repeatedly fails to appear or when the source data explicitly marks a feature as critical.

Example:

(pointed ears:1.15)
(violet eyes:1.15)

Keep weights modest.

Prefer approximately:

1.05–1.20 for normal emphasis
up to about 1.30 only when necessary

Do not weight large portions of the prompt.

Do not stack unnecessary parentheses.

Do not use weights merely to make a prompt look sophisticated.

========================================
STYLE
========================================

The GLOBAL STYLE prompt controls:

art medium
rendering style
quality vocabulary
general aesthetic
global detail level
model-specific quality prefix

Do NOT repeat those instructions here.

If the global style says watercolor, do NOT add:

watercolor paper
canvas
paint brush
paint palette
art supplies

unless those objects literally exist inside the depicted scene.

An artistic medium is not part of the fictional environment.

========================================
QUALITY LANGUAGE
========================================

The global prompt already supplies quality conditioning.

Therefore never generate:

masterpiece
best quality
amazing quality
very aesthetic
absurdres
highres
8k
high resolution
award-winning
professional artwork
beautifully rendered

Also avoid subjective filler such as:

gorgeous
stunning
extremely attractive
perfect
breathtaking

unless the requested visual concept specifically depends on it.

Do not repeat "highly detailed" across individual features.

========================================
ITEM / MEMENTO PROMPTS
========================================

When the requested subject is an object rather than a character, do not insert character tags.

Prioritize:

object type
shape
materials
construction
craftsmanship
surface texture
wear
damage
engraving
color
distinctive components

Useful composition terms include:

object focus
isolated object
centered composition
clear silhouette

when appropriate.

Example:

ornate elven hunting knife, narrow leaf-shaped steel blade, carved ashwood handle, silver wire wrapping, worn leather sheath, small chip near blade tip, engraved vine motif, object focus, three-quarter view

========================================
LOCATION PROMPTS
========================================

When generating a location, focus entirely on the environment.

Do not add characters unless the source scene requires them.

Prioritize:

architecture
geography
terrain
vegetation
materials
weather
lighting
scale
foreground
midground
background
environmental storytelling

Example:

mountain monastery, pale stone buildings built into cliffside, narrow stairways, cedar roofs, hanging prayer bells, pine forest below, distant snow-covered peaks, low clouds, morning mist, wide establishing shot

========================================
MAP PROMPTS
========================================

Maps should describe actual geography.

Useful concepts include:

fantasy map
top-down view
illustrated terrain
mountain range
river
forest
road
village
fortress
coastline
islands
farmland
valley

Do NOT automatically add:

parchment
aged paper
scroll
compass rose
decorative border
text labels
ornamental frame

unless requested.

Avoid requesting text labels unless they are specifically necessary, because image-generation models are unreliable at precise map typography.

========================================
MULTIPLE CHARACTERS
========================================

When several characters appear, establish:

number of characters
gender mix
relative positions
individual appearance
individual clothing
interaction
gaze direction

Keep each person's traits associated with that person.

Avoid creating an unordered pile of hair colors, eye colors, and clothing that could bleed between characters.

Prefer relational descriptions when needed:

blonde elf woman on left
dark-haired human man on right
woman holding man's hand
man looking at woman

Do not introduce additional people unless the scene requires them.

========================================
DO NOT INVENT IMPORTANT DETAILS
========================================

You may infer small visual details needed to make the scene coherent.

You may NOT invent major:

characters
weapons
creatures
buildings
events
injuries
costumes
weather
time periods
relationships

that contradict or materially alter the supplied RPG data.

When information is missing, prefer a conservative, visually coherent choice.

========================================
FINAL CLEANUP
========================================

Before outputting the prompt:

1. Remove narrative prose that can be replaced by visual tags.
2. Remove duplicated concepts.
3. Remove conflicting tags.
4. Remove unknown character names unless they are model triggers.
5. Remove numerical RPG ages and statistics.
6. Remove invisible micro-details.
7. Attach colors to their objects.
8. Make sure pose and composition agree.
9. Make sure environmental details belong to the current scene.
10. Make sure no global quality/style filler has been added.
11. Make sure every remaining phrase has a useful visual purpose.

========================================
OUTPUT FORMAT
========================================

Store one comma-separated positive prompt in `visual.prompt`.

No paragraphs.
No explanation inside the field.
No markdown inside the field.
No quotation marks as part of the prompt value.
No "Prompt:" label.
No negative prompt.

Example input concept:

Aerindra is a 95-year-old elf who visually appears to be an adult woman. She is a fletcher with violet eyes and pale blonde hair tied back with leather cord. She has a callus on her right thumb and a tiny scar on her left index finger. She is sitting in her workshop carefully attaching feathers to an arrow. Morning sunlight enters through the window.

GOOD OUTPUT:

1girl, solo, adult woman, elf, slender build, pointed ears, violet eyes, long pale blonde hair, low ponytail, leather hair tie, green linen work tunic, leather belt, leather bracers, sitting at workbench, holding arrow shaft, attaching feathers to arrow, fletching tools, focused expression, looking down at hands, upper body, three-quarter view, fletcher's workshop, wooden workbench, bundles of arrow shafts, loose feathers, open window, soft morning light, sunbeam, fletcher's callus on right thumb, small scar on left index finger
