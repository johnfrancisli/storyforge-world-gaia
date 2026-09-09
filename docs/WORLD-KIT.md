# The World Kit

Everything needed to build one world for this engine, in one file.

This folder is self-contained. Zip it, move it, rename it after your world, and
work inside it. Nothing here needs the engine running — you are producing a
`world.json` and a few folders of Markdown, and the engine reads them
afterwards.

| In this folder | What it is |
|---|---|
| `WORLD-KIT.md` | This file. The brief, the boundaries, and all eight stages. |
| `world.json` | The fill-in file. Every block has a `_help` key. |

## How to use it

1. Copy this folder to wherever you are building, and rename it after your
   world.
2. Paste [Part I — The brief](#part-i--the-brief-for-the-ai) to the AI you are
   working with, followed by your answers to
   [Stage 0](#stage-0--the-interview).
3. Work through stages 1–7 in order. Each is small, ends in a file, and says how
   to check it before moving on.
4. Run the checker whenever you like. It is cheap and safe to run repeatedly.
   See [Running the checker](#running-the-checker).

## The one rule worth reading first

**Write prose until the engine has to compute over it.** A record costs a
schema, a place in the context budget, and a visibility decision. A paragraph
costs nothing and reads better.

Promote a paragraph to a record when something must point at it, be counted,
appear in a panel, or be hidden from the player. Not before. See
[Prose before records](#prose-before-records).

## What you cannot change

Some things are the engine's and no world may alter them: how speech is
attributed, what a character is allowed to know, what can be seen and heard from
where, and that the player's character is never narrated for them.

You are not fighting these — they are what makes the rest trustworthy. See
[What you own, and what the engine owns](#what-you-own-and-what-the-engine-owns).

---

## Contents

**Part I — Before you write**
- [The brief for the AI](#part-i--the-brief-for-the-ai)
- [What you own, and what the engine owns](#what-you-own-and-what-the-engine-owns)
- [Prose before records](#prose-before-records)

**Part II — The build**
- [Stage 0 — The interview](#stage-0--the-interview)
- [Stage 1 — Foundation](#stage-1--foundation)
- [Stage 2 — Places](#stage-2--places)
- [Stage 3 — People](#stage-3--people)
- [Stage 4 — Threads](#stage-4--threads)
- [Stage 5 — Art](#stage-5--art)
- [Stage 6 — Rules](#stage-6--rules)
- [Stage 7 — Check, and what "done" means](#stage-7--check-and-what-done-means)

**Part III — Reference**
- [Wiki-link entity references](#wiki-link-entity-references)
- [Running the checker](#running-the-checker)
- [Keeping this folder in sync](#keeping-this-folder-in-sync)

---

# Part I — The brief for the AI

Paste this whole part to the model you are working with, followed by your
answers to [Stage 0](#stage-0--the-interview).

## What you are doing

You are helping build **one world** for a character-driven interactive story
engine. The output is a directory:

```
<slug>/
  world.json      identity and settings. Small, and it stays small.
  records/        one record, one file -- characters/, locations/, threads/, ...
  lore/           free prose, no schema. Most of a world belongs here.
  rules/          optional: .md files that change how this world plays
  assets/         images, audio, video
```

**One record, one file.** A character is `records/characters/mira-vale.md`:
YAML frontmatter for the fields the engine computes over, a body for the prose.
Write one file at a time and never read the whole world -- that is the point of
the layout, and past a few hundred kilobytes a single file cannot be read at
all. Never add a record to `world.json`; the records left it.

A world small enough to be one file may still keep its records inside
`world.json`, and the engine reads either. `world.py split` converts one into
the other.

You are not writing a novel and you are not writing a rulebook. You are writing
the smallest amount of material from which a game can start, in a form the
engine can read.

## How to behave

**Ask before inventing.** The author has a world in their head. Your job is to
get it out and write it down accurately, not to supply your own. When something
is unspecified and the choice matters, ask. When it is unspecified and the
choice does not matter, pick something plain and say you picked it.

**Work one stage at a time.** Follow stages 1–7 in order. Finish a stage, show
the author what you wrote, and wait. Do not run ahead to stage 4 because stage 2
suggested an idea.

**Write less than you want to.** The most common failure is a beautiful,
enormous world nobody can play. Every record you add costs context budget on
every turn forever. Three good locations beat twenty.

**Never fill a field to be tidy.** An empty field is information — it says
nobody has decided yet. Inventing a character's fear because the schema has a
`fears_or_limits` key produces a world of plausible noise.

**Prose first.** If something does not need to be linked to, counted, shown in
a panel, or hidden from the player, it belongs in `lore/*.md` as paragraphs,
not in `world.json` as a record.

## What the engine guarantees, and what that means for you

These are enforced in code. You cannot change them, and you should not try to
write around them:

- **Attribution.** Speech belongs to whoever said it. The narrator does not
  quote dialogue — each line is shown separately, in the speaker's own words.
- **Knowledge.** A character knows only what their context contains. An NPC
  making a factual claim must cite evidence for it or not make it.
- **Perception.** What a character can see and hear is computed from room
  geometry. Someone in the cellar cannot overhear the taproom.
- **Player agency.** The player's character is never narrated for. No prose
  decides what they feel, say or do.

The practical consequence: **write what people want and what they know, not
what they will do.** The engine will work out what they do from what you gave
them. A character with a clear desire and a clear limit will act on their own.
A character with a scripted plan will fight the engine and lose.

## What a world may change

A world can change how it *plays*, not only how it reads, by putting Markdown
files in `rules/`. Each file replaces one **slot** — a named block of
instruction the engine sends to a model at a known moment.

Run `python rpg/tools/world.py slots` for the current list. Today: `narration`.

A slot's text is added to a frame the engine owns; it comes after that frame
and cannot override it. So a rules file can change length, register, structure
and emphasis. It cannot grant knowledge, reassign speech, or narrate the player.

Leave `rules/` empty unless the author wants this world to play differently.
Defaults are good.

## The two fields that decide what art looks like

This trips everyone. A character has **two** appearance fields and they feed
different things:

- **`visual_identity`** — an object of short tag groups (`hair`, `eyes`,
  `distinctive_features`, …). These go into the canonical portrait **verbatim
  and in a fixed order**, and they are what keeps a face consistent across
  every later image. Put *unchanging* things here.
- **`appearance`** — prose. This reaches the model that composes scene images,
  as one line of a character block. Put what someone sees on meeting them.

Do not duplicate one into the other, and do not put today's mood, clothing or
emotion in `visual_identity` — it is an anchor, not a costume.

See [Stage 5 — Art](#stage-5--art) before writing either.

## Output rules

- **Ids are permanent.** `location:harbour-steps`, `character:mira-vale`.
  Lowercase, hyphenated, prefixed by type. Nothing may point at an id that does
  not exist, and renaming one later breaks every reference.
- **Wiki-link entity references in prose.** When you mention an existing
  canonical record inside Markdown prose, use a wiki-style link so the engine
  can resolve it, build backlinks, and load connected context. The syntax is:

  ```
  [[type:stable-id]]              short form — displays the record's canonical name
  [[type:stable-id|display text]]  piped form — displays your contextual text
  ```

  The reference target **must** come before the optional display text.

  Examples:

  ```markdown
  [[character:aerindra]] resolves to "Aerindra Glintleaf"
  [[character:aerindra|the pale-haired fletcher]] displays the contextual text
  [[location:harus-shrine|Haru's shrine]]
  [[org:briar-wardens|the Wardens of the Briar]]
  [[thread:broken-road|the broken Old Roads]]
  ```

  **Do not** use these forms:

  ```markdown
  [character:aerindra|Aerindra]            single brackets — not a wiki link
  [[Aerindra|character:aerindra]]           reversed — target must come first
  [Aerindra](character:aerindra)            Markdown link — not resolvable
  ```

  Rules:

  1. Double square brackets `[[...]]` are reserved for resolvable entity
     references. Do not use them for anything else in Markdown.
  2. The target uses the entity's stable typed ID (`character:aerindra`), not
     its visible name.
  3. The target always comes before the display text.
  4. Names can change; stable IDs must not. Never change an ID because a
     record was renamed.
  5. `[[type:id]]` displays the record's current canonical name.
  6. `[[type:id|text]]` preserves the supplied display text.
  7. Plain mentions remain ordinary prose — only wrap a mention in `[[...]]`
     when it should be a resolvable reference.
  8. A wiki link creates a mention/reference edge, **not** a structured
     relationship. Use relationship records for actual bonds.
  9. Structured JSON/YAML fields that expect raw IDs (`participants`,
     `locations`, `affiliations`) must continue using raw IDs — never put
     wiki-link markup inside them.
  10. Wiki links belong only in Markdown or prose fields unless the schema
      explicitly says otherwise.
  11. Do not create links for generic or incidental nouns. "The innkeeper"
      is plain text unless a `character:` record exists for that person.
  12. Do not expose raw wiki-link markup in player-facing narration; render
      it as its display text or canonical name.
  13. Preserve wiki links when editing internal lore unless the referenced
      record is intentionally removed.
  14. Report unresolved references rather than silently converting them to
      plain text.

  Valid entity type prefixes: `character`, `location`, `organization`, `org`
  (abbreviation used in existing records), `thread`, `item`, `relationship`,
  `lore`.

  Future syntax (not yet implemented): section anchors like
  `[[location:crossford#market|Crossford market]]`. The portion before `#`
  is the stable record ID; the portion after is a sub-anchor. Do not rely on
  this until it is officially supported.

- **`gm_notes` is private.** It never reaches the narrator or any NPC. What a
  character is hiding goes there, never in `summary`.
- **Leave `_help`, `_layer` and `_status` keys alone.** They are guidance and
  are stripped on import.
- **Replace every `PLACEHOLDER`.** The checker warns about any you miss.

## When you are done with a stage

Say what you wrote, what you chose without being told, and what you left empty
on purpose. That last one matters most — it is how the author finds the thing
you quietly guessed.

---

# What you own, and what the engine owns

Read this before changing anything. It answers one question: **is this mine to
change, or does it belong to the machine?**

There are three layers.

| Layer | What it is | Can you change it? |
|---|---|---|
| **Engine** | How the machine works at all | No. Changing it breaks things for every world. |
| **Kit** | Sensible defaults you inherit | Yes, and your change affects only your world. |
| **World** | Your story | Yes. This is the part that is yours. |

## The test

When you are unsure which layer something is in, ask:

> **Would a noir detective campaign with no magic need this changed?**

- **No, and changing it would break the machine** → Engine. Leave it.
- **No, but a different game might want a different one** → Kit. Override it if
  you like; you are replacing a default, not fighting the engine.
- **Yes** → World. It is yours, and no default should have opinions about it.

## Worked example: how a picture gets made

Every part of an image prompt has a different owner. This is the clearest case,
so it is worth reading even if you never touch art.

**Engine — not yours.**
- The size each kind of picture is rendered at. Scenes are 1216×832, records
  896×1152, portraits 832×1216. These are the image model's native sizes; a
  different number does not give you a different style, it gives you worse
  hands.
- The framing words added so a subject survives being cropped square or wide.
- The shape of the request sent to the image appliance.

**Kit — yours to override, sensible if you do not.**
- The default negative prompt: what no picture should contain.
- The starting-point style presets in the Settings tab.
- What each *kind* of record adds — "single object study, isolated item" for an
  item, "readable face, neutral full body pose" for a character.

**World — yours.**
- The global image prompt. Every picture in your world carries it. This is your
  world's look and nothing else should decide it.
- Your negative prompt: what your world never shows.
- Which image profile to use, from the list the engine supports.
- Every portrait, every pinned piece of art, every character's appearance.

The pattern to notice: **the engine owns the mechanics of making a picture, the
Kit gives you a decent look to start from, and the world owns what it looks
like.** The same shape applies everywhere else.

## Worked example: how a turn gets narrated

**Engine.** The stages a turn runs through. That speech is attributed to whoever
said it. That an NPC can only claim things it has evidence for. That a character
in the cellar cannot hear the taproom. That records have context tiers and a
token budget. None of this is advice — it is enforced, and a world cannot opt
out any more than it can opt out of arithmetic.

**Kit.** The craft rules the narrator follows: keep the player's agency, end on
something live, show what people feel rather than naming it.

**World.** Your narrator's voice, if you want a named one. Your register, your
tense, the things your world never does. Your tone set. Your calendar. Your
terminology.

## Why this matters more than it sounds

The system we studied before building this does not separate these. Its ~100
instruction files sit in one folder organised by topic, mixing engine mechanics
with one campaign's voice, and when asked which was which its own GM had to
guess — and said so. The result is that starting a second world means reading
every file to work out what was general and what was somebody else's story.

Keeping the layers apart costs nothing at runtime. It is a filing decision made
once, and it is what makes your world portable and the next author's world
possible.

## Changing how your world *works*, not just what is in it

Everything above is about content and look. You can go further: a world can
change what the engine **says** at the moments that matter.

The engine runs the same steps for every world, and at certain points it asks a
model to do something — narrate a turn, decide what an NPC does, close a scene,
resolve a skill check. Each of those points is a **slot**, and each slot has a
default. Put a Markdown file in your world's `rules/` folder named after a slot
and yours is used instead.

```
rules/
  narration.md     how a turn should be written
```

**Only `narration` exists today.** The mechanism is general and more slots are
intended — an NPC actor, pacing, skill checks — but a file named for a slot the
engine does not have is an error, not a no-op. Run the `slots` command for the
list that is actually live, and trust that over any list written down, including
this one.

An empty `rules/` folder is a perfectly good world — you get the defaults. Fill
one file and that part of the game changes.

**What a slot cannot do.** Your text is added to a frame the engine builds; it
does not replace it. So no rules file can make a character know something they
have no reason to know, put words in the player's mouth, hear through a wall,
or detach speech from whoever said it. Those are not defaults being polite —
they are not in the prompt for your file to argue with.

That is the trade, and it is deliberate: you can change what the engine asks
for, not what it hands over.

## Where each layer lives

| Layer | Lives in |
|---|---|
| Engine | The engine's code. Not in this folder at all. |
| Kit | Engine defaults you inherit, in the engine's `rpg/kit/rules/`. |
| World | Your `world.json`, your `rules/` overrides, your `lore/` prose, and — once you are playing — your world's records in the app. |

Every block in `world.json` carries a `_layer` key saying which of these it
belongs to. If one does not, that is a bug in the kit. Say so.

---

# Prose before records

The central move, and the one thing worth learning before you start.

## The rule

**Write prose until the engine has to compute over it. Then promote it.**

A record costs something: a schema, a place in the context budget, a decision
about who can see it. Prose costs nothing and reads better. So prose is the
default, and a record is what you make when something needs to be *linked to*,
*counted*, *filtered*, or *shown in a panel*.

This is the same line the system we studied draws, arrived at independently:
its structured types are characters, locations, factions, calendars, creatures,
equipment, relationships, threads and events — while "laws, religions,
languages, technology, cosmology, trade routes, cultural exchange, and
pre-campaign history are primarily prose."

## The signals that it is time

Promote a piece of prose to a record when any of these becomes true:

- **Something else needs to point at it.** A faction that belongs to a religion
  needs the religion to have an id.
- **The engine must count or compare it.** Pressure that rises, a disposition
  that drifts, a clock that fills.
- **It must appear in the interface.** Panels render records, not paragraphs.
- **Visibility differs by reader.** The moment part of it is secret from the
  player but not from you, it needs the fields that carry that.
- **It is generated or edited during play**, rather than authored once.

If none of these is true, leave it as prose. A beautifully structured record
nobody links to is a schema you now have to maintain.

## A worked promotion

**Step 1 — prose.** `lore/religions.md`:

> The Ashfast keep no temples. They believe the dead are owed a debt the living
> cannot repay, and that any roof over a grave is an insult...

That is enough for a model to narrate an Ashfast priest convincingly, and for
you to write one. Nothing else is needed.

**Step 2 — pressure to promote.** Three things have happened:

1. Two factions now describe themselves by their relationship to the Ashfast.
2. You want a panel showing which holdings observe the rite.
3. There is something about their funerary practice the player should not know.

**Step 3 — the record.** The religion becomes an entry with an id, a summary,
links to the factions that reference it, and a GM-private field for the part
that is hidden. The prose does not disappear — it becomes the record's
`summary` and description, and `lore/religions.md` keeps whatever did not need
structure.

**What did not change:** the writing. Promotion is a filing act, not a rewrite.
If you find yourself rewriting the prose to fit the schema, the schema is
wrong or the promotion is premature.

## The reverse move

If a record has no links, never appears in a panel, and has nothing private in
it, it should probably go back to being prose. Records that exist because they
seemed tidy are the ones that rot.

---

# Part II — The build

---

# Stage 0 — The interview

Answer these before anything is written. Short answers are fine; "I do not know
yet" is a real answer and better than a guess you will have to undo.

The AI should ask these a few at a time rather than dumping all fourteen.

## The world

1. **Where and when are we?** One sentence. Not the history — the place.
2. **What is the one thing about this world a newcomer must be told?** If there
   is magic, technology, a catastrophe or a rule of nature that changes how
   people live, this is it.
3. **What is already going wrong?** A world with nothing under pressure has
   nothing to narrate.
4. **What is this world *not*?** The nearest thing it resembles, and how it
   differs. "Like a heist story, but nobody is competent."

## The feel

5. **Name three works this should feel like.** Books, films, games, anything.
   Feel, not plot.
6. **What should a player never see here?** Style refusals, not content
   warnings — "no prophecy", "nobody explains the magic", "no last-minute
   rescues".
7. **Is the narration warm or cold? Close or distant?** One sentence written in
   that voice is worth more than the adjectives.
8. **Does this world have a named narrator?** Usually no, and that is fine. If
   yes, who are they and what are they not allowed to know?

## The opening

9. **Where does the first turn happen?** A room, a road, a doorway. Concrete.
10. **Who else is there?** One or two people, not a crowd.
11. **What does the player want in the first five minutes?** Small and
    immediate. Not the campaign's goal.
12. **What happens if the player does nothing at all?** If the answer is
    "nothing", stage 4 has work to do.

## Scale — easy to skip, expensive to get wrong

13. **How far is far?** Is a week's travel routine, or an expedition?
14. **How many people are in the biggest place we will visit?** A village, a
    city, a station of forty.

These two govern how travel reads, how the calendar feels, and whether a
faction is a family or an army.

---

# Stage 1 — Foundation

Three Markdown files. When these are done you have a playable world; everything
after this is enrichment.

Write them into `lore/`, then fill the `world` and `voice` blocks of
`world.json` from them.

## `lore/premise.md`

Four short sections, prose not bullets.

- **What this world is** — two or three sentences a player would be told before
  their first turn.
- **What is already true** — the handful of facts the world rests on. Resist
  history; write the things that constrain the present.
- **What is already wrong** — something under pressure before the player
  arrives, with a sense of how soon it matters.
- **What this world is not** — the nearest familiar thing, and the difference.

Aim for 300–500 words. Past 800 you are writing setting material, not a premise.

## `lore/voice.md`

- **Register** — named in a sentence, then *demonstrated* in four sentences of
  an ordinary moment. The demonstration is the useful half.
- **Never in this world** — the style refusals from interview Q6.
- **The narrator** — leave empty for a clean unnamed narrator. If named, say who
  they are and what they cannot know. A narrator with a perspective is a
  character, and characters can be wrong.

## `lore/promises.md`

- **Promises** — what a player can rely on. Each is a constraint you accept:
  "your choices close doors permanently", "nobody is secretly a god", "if an NPC
  says they will be somewhere, they will be".
- **Refusals** — what this world will not do, whatever the fiction suggests.
- **Scale** — interview Q13 and Q14, written plainly.

## Then fill in `world.json`

| Block | From |
|---|---|
| `world.name`, `tagline`, `description` | `premise.md` |
| `world.genre` | Pick before the calendar and tones blocks — it seeds both |
| `world.theme` | One word: `grounded`, `cozy`, `light-novel`… |
| `voice.*` | `voice.md`, including the sample paragraph verbatim |

Leave `calendar` and `tones` alone for now. Both are seeded from `genre`, and
the defaults are usually right for a first pass. Come back to them when the
world has told you what its seasons and moods actually are.

## Check before moving on

- Can you describe the opening scene using only these three files? If not,
  something load-bearing is still in your head.
- Does `voice.md` contain an actual paragraph *in* the voice, rather than a
  description *of* it?
- Is `world.name` filled in? Everything else can wait; that one cannot.

---

# Stage 2 — Places

Three locations. Possibly four. Not twelve.

## What to write

Fill `locations.entries` in `world.json`.

- **One region** — the containing area, `parent_location_id: null`.
- **One or two settlements or interiors** inside it.
- **The opening location** — where the first turn happens. Concrete: light,
  sound, temperature, who else is present.

## Ids are permanent

`location:harbour-steps`. Lowercase, hyphenated, prefixed. Everything else
points at these, and renaming one later breaks every reference silently.

## The containment tree is not decoration

`parent_location_id` builds a real hierarchy, and that hierarchy is what makes
jurisdiction *enforceable* rather than remembered. Set it even when it seems
obvious. A patrol belonging to one polity has no business inside another, and
the tree is how anything can know that.

Fill `jurisdiction` with who rules here and how lightly. One line.

## Interiors, only when a scene needs them

`map_size_ft`, `rooms` and `portals` exist so the engine can compute who can see
and hear whom. Someone in the cellar cannot overhear the taproom — but only if
the rooms exist.

**Skip all of it on a first pass.** Add geometry to one interior when a scene
genuinely needs people unable to hear each other. A region never needs it.

## What belongs in `lore/` instead

Almost everything. History, trade, architecture, why the river moved. A location
record carries a `summary` someone can be dropped into and act from; the rest is
prose, which is cheaper and reads better.

Every record you add costs context budget on every turn, forever. Three good
locations beat twenty.

## Check before moving on

- Does every `summary` say what it is like to *be* there, rather than what
  happened there?
- Does the opening location name at least one thing a player could touch, open
  or walk through?
- Does every `parent_location_id` point at an id that exists?

---

# Stage 3 — People

Two or three characters. The player's own character is created with the
campaign, not here.

## What makes a character work in this engine

Every speaking NPC is run as **its own model call, with its own scoped
knowledge**, and it decides what it does. You are not writing behaviour. You are
writing the conditions from which behaviour follows.

### Who they are

- **`name`** — their actual name: given and family name where the culture has
  both. **`aliases`** — what people call them: a title, a nickname, the name a
  rival uses. The narrator prefers `name`; aliases are how a reference in play
  resolves to this person.
- **`race`** and **`gender`** — both must be values the world's own lore names.
  Write `lore/races.md` and `lore/gender.md` first and fill these from them,
  rather than reaching for a default that belongs to some other world. A
  character whose race or gender has not been decided leaves the field empty,
  which says so honestly.

### The four prose fields, which are not interchangeable

- **`summary`** — two sentences a stranger could observe. This reaches
  everything, so it is the one that must be right.
- **`biography`** — where they came from and how they got here.
- **`personality`** — how they carry themselves, and what they will not do.
- **`key_phrases`** — things only this person would say. The narrator writes
  dialogue from these, so three sharp ones beat a paragraph of description.

### Their statblock, and what a scene does to it

`stats` is the character **as written** — level, maximum hp, mana, stamina,
speed, defense, and the six attributes. It is canon, and it does not change
during play. `currency` sits beside it.

What changes is the *scene*. An actor in a fight carries its own `hp_current`
against that `hp` as a ceiling, so the same person can walk into one battle
whole and the next at a tenth of their strength — and neither fact reaches the
other, the character record, or any other campaign playing this world. That
separation is why a wounded companion in somebody's war scene never becomes
everyone's wounded companion.

Leave the block empty for anyone who will never be in a fight. Most of a world's
cast never rolls anything.

### Where they stand

`current_state.location` is where they are. **`purview`** is the places they are
responsible for without standing in — a tavern-keeper's cellar, a captain's
ship. A character can be found in one and answerable for several.

### What makes them act

So four fields carry most of the weight:

- **`summary`** — who they are, in two sentences a stranger could observe.
- **`desires`** — what they want and will act on. One or two, concrete enough to
  be pursued inside a scene.
- **`fears_or_limits`** — what stops them. Without this a character agrees with
  everything, because nothing costs them anything.
- **`gm_notes`** — what they are hiding. **Private**: it never reaches the
  narrator or any NPC. This is the difference between a character with an
  interior and a character with a description.

A character with a clear want and a clear limit will surprise you. A character
with a scripted plan will fight the engine and lose.

## The two art fields — read this twice

These feed **different things**, and confusing them is the most common mistake
in the whole kit.

### `visual_identity` — the anchor

An object of short tag groups. They reach the canonical portrait **verbatim, in
this order**:

```
age, body_build, height, skin, face, eyes, hair, distinctive_features, jewelry
```

Include only the keys you care about. Each value is a short tag group, not a
sentence:

```json
"visual_identity": {
  "age": "late thirties",
  "hair": "black, cropped short, greying at the temple",
  "eyes": "grey",
  "distinctive_features": "burn scar across the left hand"
}
```

**Only unchanging things belong here.** This is what keeps a face the same
across every image forever. Clothing, mood and today's injuries do not.

### `appearance` — the prose

One paragraph. It reaches the model that composes *scene* images, as one line of
a character block. Write what someone sees on meeting them: bearing, dress, how
they hold themselves.

Do not duplicate `visual_identity` into it.

### Together

`visual_identity` keeps them recognisable. `appearance` makes a scene image feel
like a person rather than a mugshot.

## Where they are

`current_state.location` puts a character somewhere, and it is **live**: when
the player is at that location, the engine tells the narrator and the planner
that this person is here. Walk into the town square and the people the world
says are in the town square are in the scene.

```json
"current_state": { "location": "location:town-square" }
```

Use the location's **id**. Its name works too, and matching is
case-insensitive, so a world authored with ids and a campaign seeded with prose
still line up — but ids are what stay correct when you rename a place.

`home` is the fallback for "where they are when nothing has moved them".
`current_state.location` wins when both are set.

**This is not the whole cast of a scene.** The engine still invents incidental
people — a porter, someone at the next table — as *scene actors*, which are
transient and do not become canon unless you promote them. Your placed
characters are the ones who are reliably there; everyone else is weather.

So place the two or three people who *belong* somewhere, and let the rest
happen. A square where you listed nine named residents is a square where
nothing can surprise you.

## Relationships

Write one, if two characters already have something between them. Keep the
halves separate:

- `public_status` — what a bystander would say about these two.
- `bond` — what is actually going on. GM-side.

## Check before moving on

- Does every character want something a scene could be *about*?
- Does every character have something that stops them?
- Is anything in `visual_identity` a costume, a mood, or an injury? Move it.
- Is anything secret sitting in `summary` instead of `gm_notes`?
- Would two of these characters have something to say to each other with the
  player absent? If not, the cast is a list rather than a situation.
- Does the opening location have at least one person placed in it? If nobody is
  there, the first turn has only scenery to work with.

---

# Stage 4 — Threads

One thread. Two at most.

A thread is **something unresolved that gets worse if ignored**. It is the
engine of the campaign, and the difference between a world that waits for the
player and one that is already moving.

## The field that matters most

`next_possible_moves` — two or three things that happen **if the player does
nothing**.

This is the most valuable field in the whole file. Everything else describes a
situation; this one gives it momentum. Write them as events with actors, not as
atmosphere:

- ✅ "The harbourmaster posts the seizure notice, and the crew hear it before
  Mira does."
- ✅ "Aden's debt comes due on the sixteenth."
- ❌ "Tension continues to rise."
- ❌ "Something bad might happen."

Revise these as the campaign moves. A thread whose next moves have all happened
is a thread that has resolved, whether or not anyone noticed.

## The rest of the thread

- **`summary`** — the situation the campaign opens inside.
- **`stakes`** — what is lost if this goes badly. Be specific about *whose* loss.
- **`pressure`** — how close it is to forcing itself. `rising`, `steady`,
  `critical`.
- **`participants`, `locations`, `organizations`** — ids of things already
  written. Do not invent new ones here; go back to stage 2 or 3 if the thread
  needs someone who does not exist.

## Factions, if you need one

An organization earns its place when a group wants something the player might
help or hinder. Give it:

- **`wants`** — the thing it is trying to get.
- **`seat`** and **`holdings`** — location ids, which is what ties it to the
  containment tree from stage 2.
- **`pressure`** — how close it is to acting.

Note: organization `pressure` is stored but nothing moves it on its own yet.
Thread `pressure` is live. Write both honestly; do not build a plot that depends
on faction pressure changing by itself.

## The test for a good thread

Answer interview Q12 again: **what happens if the player does nothing at all?**

If you can now answer it in one concrete sentence naming a person and a
consequence, the thread works. If the answer is still "nothing", you have
written a situation rather than a thread.

## Check before moving on

- Does every id in `participants`, `locations` and `organizations` exist?
- Does at least one `next_possible_move` name a specific person doing a specific
  thing?
- Would the world be different in a week if the player never arrived?

---

# Stage 5 — Art

How pictures get made here, and how to write for it.

## What you control, and what you do not

**Yours.** The world's global image prompt, its negative prompt, and every
character's appearance fields.

**Not yours.** The size and framing of each kind of image. The engine renders
scenes at **1216×832**, records at **896×1152**, and portraits at **832×1216**,
because those are the image model's native buckets — a different number does not
give you a different style, it gives you worse hands. It also adds framing words
so a subject survives being cropped. You cannot turn these off, and you do not
want to.

## The global image prompt

Set in `art.global_prompt`. It is appended to **every** image in the world, on
top of whatever the scene itself calls for.

Write it as a tag block, not a sentence. Cover four things:

1. **Medium** — "traditional ink and watercolour wash", "painterly oil",
   "35mm photograph"
2. **Palette** — the colours this world is made of
3. **Light** — where it comes from and how hard it is
4. **Finish** — line weight, texture, level of detail

A worked example, in the shape that works:

```
traditional ink and watercolor wash, highly detailed pen and ink linework,
muted earth palette with cold blue shadow, low raking daylight, visible paper
grain, restrained detail, no text, no watermark, no border
```

Length is fine. Contradictions are not — "flat colour" and "volumetric lighting"
in one prompt gives you neither.

## The global negative prompt

`art.negative_prompt`. Ruled out of every image. Leave it empty to inherit a
tested default.

**Do not ban something your positives ask for.** The clearest example: the
`character` per-type style and every canonical portrait ask for "simple
background". Putting `simple background` in your negative makes the two fight,
and the result is a coin flip. The shipped default has that term removed for
exactly this reason — if you write your own negative, check it against what the
per-type styles request first. You can see them in the Settings tab under
"What each kind of image adds".

## Character art — the two fields again

Covered in [Stage 3](#stage-3--people), repeated because it is where art goes
wrong:

| Field | Reaches | Write |
|---|---|---|
| `visual_identity` | The canonical portrait, **verbatim** | Short tag groups. Unchanging things only. |
| `appearance` | The scene-image composer, as prose | One paragraph: bearing, dress, how they hold themselves. |

The canonical portrait is generated once as a **full-body, neutral-pose,
simple-background** reference, and later images use it to keep the face
consistent. That is why `visual_identity` must not contain a costume or a mood:
you are describing the person, not the picture.

## Prompts you can paste

These are for an AI helping you author, not for the image model directly.

### Drafting the global image prompt

> Here is my world's premise and voice: [paste `lore/premise.md` and
> `lore/voice.md`].
>
> Write a global image prompt for it as a comma-separated tag block covering
> medium, palette, light and finish. No sentences. No contradictions — do not
> ask for both flat colour and volumetric light. End with: no text, no
> watermark, no border. Then explain each choice in one line so I can argue
> with it.

### Drafting a character's two fields

> Character: [summary, role, and anything about how they look].
>
> Give me two things, clearly separated.
>
> 1. `visual_identity` as a JSON object using only these keys where they apply:
>    age, body_build, height, skin, face, eyes, hair, distinctive_features,
>    jewelry. Each value is a short tag group, not a sentence. Include ONLY
>    permanent physical facts — no clothing, no mood, no current injuries.
> 2. `appearance` as one prose paragraph: bearing, dress, how they hold
>    themselves. Do not repeat what is in visual_identity.
>
> Then tell me anything you invented that I did not give you.

### Checking a world's art direction before generating

> Here is my global image prompt: [paste]. Here is my negative prompt: [paste].
>
> Tell me: any term appearing in both; any pair of positives that contradict;
> anything so specific it will fight every scene. Do not rewrite it — just
> list the problems.

## If you are making images yourself

You do not have to use the pipeline. A world can have hand-made portraits, and
the engine will use them. What matters is that the *anchor* fields still
describe the person accurately, because they also reach the scene composer and
the narrator's character block. A portrait you drew and a `visual_identity` that
disagrees with it will produce scenes that contradict your own art.

## Check before moving on

- Does the global prompt name a medium, a palette, a light and a finish?
- Does it contradict itself anywhere?
- Does the negative ban anything the per-type styles ask for?
- Does every character have `visual_identity` with only permanent facts in it?

---

# Stage 6 — Rules

**Skip this stage unless you want this world to play differently.** The
defaults are good, and an empty `rules/` folder is a perfectly good world.

## What a rules file is

The engine asks a model to do something at certain points in a turn. Each of
those points is a **slot**, and each slot has a default you can replace by
writing `rules/<slot>.md`.

Run this for the current list:

```bash
python rpg/tools/world.py slots
```

Today there is one: `narration` — how a turn is written, once events are
settled.

## What you are replacing

The default `narration` slot says roughly: write 2 to 4 short paragraphs, obey
the pace dial, end on a concrete situation. That is *manner*, and manner is
yours.

What you are **not** replacing is the frame around it. Your text is added after
a block the engine owns, and that block says the narrator is given only
validated, player-visible events; never invents a line of dialogue; never states
what a character privately thinks; and never decides what the player does.

Those are not defaults being polite. They are stated above your file, and the
things they protect — what the model is *given* — were decided before your text
existed. A rules file that says "narrate the player's feelings" does not win
that argument; it just wastes the tokens.

## Worth changing

- **Length and rhythm.** "Write one paragraph, never more" produces a
  completely different game from the default.
- **Tense and distance.** Present tense, tighter or wider focus.
- **What a turn must contain.** "Every turn names a sound." "Every turn shows
  one person's hands."
- **How a scene closes.** The strongest single rule we have seen anywhere:
  never end on a still frame — close on something live, an NPC acting on their
  own want, a clock moving, a consequence landing, a door standing open.

## Not worth changing

- Anything about what characters know. Enforced elsewhere; your file cannot
  reach it.
- Anything about who speaks. Speech is attributed structurally.
- Restating the frame. It is already there, above your text, every turn.

## How to write one

Short. The whole file is inserted into a prompt that also has to carry your
world's canon, and every line competes for the same budget. Under 150 words is a
good target; the shipped default is 93.

Direct instructions, not explanation. "Write one paragraph" beats "this world
favours brevity because its tone is terse".

## Check it worked

```bash
python rpg/tools/world.py check <slug>
```

A file named for a slot that does not exist is an **error**, not a warning —
`rules/naration.md` would otherwise sit there looking like it worked, forever.

After a turn, the engine records which file it used. A world override reports as
`world`; falling back reports as `kit`. An emptied file falls back and reports
`kit`, because a blanked file means "I meant to write this later", not "this
world has no narration rules".

---

# Stage 7 — Check, and what "done" means

## Run the checker

```bash
python rpg/tools/world.py check <slug>
```

It reports two kinds of thing.

It also reports **field drift** — records of one type that have stopped
carrying the same shape. Two kinds, and the first matters more:

- **`apperance` is not a field of this type (did you mean `appearance`?)** — a
  misspelled field is a paragraph nothing will ever read, and without this
  nothing says so.
- **`key_phrases` is missing from 20 of 37** — usually a field added to the
  template after those records were written.

Both are grouped by field rather than listed per record, because three hundred
lines about one missing key is not a report anybody reads.

**Errors** — fix before importing:

- A `rules/*.md` naming a slot that does not exist. This is the one that
  otherwise looks exactly like success: the file sits there and never applies.
- A reference to an id nothing defines. `character:mira-vale` in a thread when
  no such character exists.
- A missing or empty world name.
- Malformed JSON.

**Warnings** — fine while drafting:

- `PLACEHOLDER` text still in place. Expected early; a problem at import,
  because a world with PLACEHOLDER names *runs*, and looks like it worked.

## The human checks the tool cannot do

Read these out loud. The checker cannot.

**Can a first turn happen?** Take the opening location, the people in it, and
the thread. Narrate thirty seconds of it in your head. If you have to invent
something to do that, it is missing.

**Does anyone want anything?** Every character should want something a scene
could be about, and have something that stops them. A cast of agreeable people
produces agreeable, forgettable turns.

**Does the world move without the player?** Read `next_possible_moves` aloud.
If none of them names a person doing a thing, nothing is going to happen.

**Is anything secret in the wrong field?** Anything a player should not know
belongs in `gm_notes`. `summary` is shared.

**Does the art direction contradict itself?** See [Stage 5](#stage-5--art).

**Is anything a placeholder you stopped noticing?** The most common failure is
not an empty field — it is a field filled with something plausible and generic
that nobody ever went back to.

## What "done" means

Done is **not** complete. Done is:

- Three prose files in `lore/`
- A `world.json` that passes `check` with no errors
- Three or four locations, two or three characters, one thread
- A global image prompt
- Nothing invented that the author did not approve

A world this size is playable, and playing it will tell you more about what it
needs than another day of writing will. Everything else is added later, from
inside the story, when something turns out to be missing.

## Hand back

Tell the author:

1. What was written, by stage.
2. **What you chose without being told.** Names, ages, the colour of a door.
3. **What you left empty on purpose**, and why.

Point 2 is the one that matters. It is how the author finds the thing you
quietly guessed and got wrong.

---

# Part III — Reference

---

# Wiki-link entity references

## Canonical syntax

```
[[type:stable-id]]              short form — resolves to the record's canonical name
[[type:stable-id|display text]]  piped form — displays your contextual text
```

The target (a stable typed ID like `character:aerindra`) always comes before
the optional display text. This follows the convention used by MediaWiki,
Obsidian, and DokuWiki.

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

### What not to do

```markdown
[character:aerindra|Aerindra]            single brackets — not a wiki link
[[Aerindra|character:aerindra]]           reversed — target must come first
[Aerindra](character:aerindra)            Markdown link — not resolvable
```

Do not put wiki-link markup inside structured JSON/YAML fields that expect
raw IDs:

```json
// Wrong:
{ "participants": ["[[character:aerindra|Aerindra]]"] }

// Correct:
{ "participants": ["character:aerindra"] }
```

### AI authoring instruction

When referring to an existing canonical record in authoring Markdown, use
`[[type:stable-id]]` or `[[type:stable-id|contextual display text]]`. The
stable reference must appear before the optional display text. Resolve
existing records before creating links; never invent an ID for a record that
has not been created. Use plain text for incidental people and things that
are not canonical records. Wiki links represent references, not relationships.

- Reuse an existing record ID whenever the entity already exists.
- Never resolve entities by visible name alone when a stable ID is available.
- Never change a stable ID merely because a record was renamed.
- Do not create links for generic or incidental nouns.
- Do not expose raw wiki-link markup in final player-facing narration; render
  it as its display text or canonical name.
- Preserve wiki links when editing internal lore unless the referenced record
  is intentionally removed.
- Report unresolved references rather than silently converting them to plain
  text.

### Retrieval and connection semantics

Storyforge may index each wiki link as:

```
source document or record → referenced entity
```

This supports backlinks, validation, graph navigation, and selective context
loading.

The context loader should:

1. Resolve directly referenced entities.
2. Load the active entity's relevant relationship records.
3. Include compact summaries of one-hop connected entities.
4. Load full connected records only when required by the current scene.
5. Avoid recursively loading the entire connection graph.
6. Respect the prompt's token budget and visibility rules.

### Future syntax (not yet implemented)

Section anchors:

```
[[location:crossford#market|Crossford market]]
```

The portion before `#` is the stable record ID; the portion after is a section
or sub-anchor. Do not rely on this syntax until it is officially supported.

### Validation

The checker (`validate_wiki_links.py`) can detect:

- Unknown entity types (a prefix not in the valid set)
- Malformed wiki links (missing brackets, empty targets)
- References to nonexistent IDs
- Reversed links that appear to use `[[display name|type:id]]`
- Wiki-link markup inside structured fields that require raw IDs

Unresolved references produce a warning or error containing:

- Source file or record
- Referenced target
- Suggested correction, when determinable

Wiki-link-like text inside fenced code blocks and inline code is ignored by
the validator.

When using `|` inside Markdown tables, ensure wiki links are recognized as
complete inline tokens before interpreting table separators. If the current
Markdown parser cannot support this safely, escape the pipe as `\|` inside
the link.

---

# Running the checker

Authoring needs nothing but a text editor. The checker is the one part that
needs the engine repository, because it validates against the engine's live slot
registry rather than a list written down here.

```bash
python rpg/tools/world.py new <slug>              a blank world
python rpg/tools/world.py new <slug> --template   with the Kit rules copied in
python rpg/tools/world.py check <slug>            validate before importing
python rpg/tools/world.py slots                   what a world may override
```

Run these from the engine repository root.

## Where worlds live

`new` and `check` both resolve `<slug>` against a worlds directory, not against
your current folder. It defaults to `worlds/` beside the engine, and
`STORYFORGE_WORLDS_DIR` overrides it:

```bash
STORYFORGE_WORLDS_DIR=/path/to/my/worlds python rpg/tools/world.py check <slug>
```

So a kit folder you zipped and moved is not checked in place. Either point
`STORYFORGE_WORLDS_DIR` at wherever you are keeping it, or copy the finished
world into the engine's `worlds/` when you are ready.

`new` copies its `world.json` from the engine's own template, not from this
folder — see [Keeping this folder in sync](#keeping-this-folder-in-sync).

## What check will and will not catch

It reads `world.json` and `rules/`. It does not touch the database, does not
need the server running, and is safe to run repeatedly while drafting.

It is deliberately shallow. It catches dangling ids, unknown slot filenames,
malformed JSON, a missing world name, and leftover `PLACEHOLDER` text. It cannot
tell you whether a first turn can happen — that is the read-aloud list in
[Stage 7](#stage-7--check-and-what-done-means).

One quirk worth knowing: a world name that is *still* the literal placeholder
passes as a warning, not an error. Only an actually empty name is an error. That
is intentional so drafting is not blocked, but it means a world can pass `check`
and still import with a placeholder name.

## If the tool will not run

`world.py` imports the engine's `slots` module and nothing else, so it works on
a bare Python with no dependencies installed. If it fails, you are probably not
at the repository root.

The engine's web app is fussier. It pins `starlette>=0.36.3,<0.39.0`, and on a
newer starlette it fails at import with:

```
TypeError: Router.__init__() got an unexpected keyword argument 'on_startup'
```

That breaks the app and its HTTP tests, not the checker. The fix is the pinned
requirements:

```bash
pip install -r rpg/requirements-dev.txt
```

---

# Keeping this folder in sync

Two things in this kit are copies of something the engine also holds, and
neither is checked automatically.

**`world.json`.** This folder's copy is what makes the kit portable — you can
zip it and fill it in with no repository present. But
`python rpg/tools/world.py new` copies the engine's
`docs/world-template/world.json` instead. The two are identical today. If they
drift, an author following this kit starts from a different file than the tool
produces. When you change one, change both.

**The slot list.** Every list of slots written in prose — including the one in
[Stage 6](#stage-6--rules) and the note in
[What you own](#what-you-own-and-what-the-engine-owns) — is a snapshot. The
engine's registry is the truth:

```bash
python rpg/tools/world.py slots
```

Today it prints one slot, `narration`. If this document and that command
disagree, the command is right.
