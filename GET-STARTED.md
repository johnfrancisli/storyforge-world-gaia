# Get started

You are holding a folder that becomes a world. This page is the first five
minutes; [`WORLD-KIT.md`](WORLD-KIT.md) is everything after that.

## If you are the author

1. Rename this folder after your world.
2. Open a chat with whichever AI you want to build it with.
3. Paste **[the opening prompt](#the-opening-prompt)** below, then answer its
   questions. It will ask a few at a time, not all fourteen at once.
4. When it starts writing files, it is following `WORLD-KIT.md` stages 1–7.
   Read that when you want to know why it is asking for something.

You do not need the engine running. You are producing a `world.json` and a few
folders of Markdown; the engine reads them afterwards.

**You are not expected to have answers to everything.** "I do not know yet" is
a real answer and a better one than a guess you will have to undo.

## The opening prompt

Copy everything in this block.

---

> I want to build a world for a character-driven interactive story engine, and
> I want you to help me get it out of my head and written down accurately.
>
> Read `WORLD-KIT.md` in this folder before you write anything. Part I is your
> brief — how to behave, what the engine guarantees, and the two appearance
> fields that trip everyone. Part II is the build order. Follow it.
>
> **One record, one file.** If this world has a `records/` folder, every
> character, location, thread and item is its own Markdown file with YAML
> frontmatter — `records/characters/mira-vale.md`. Write one file at a time.
> Never read the whole world, and never rewrite `world.json` to add a record:
> it holds identity and settings only, and the records left it. Prose with no
> schema goes in `lore/` as ordinary Markdown.
>
> Start with Stage 0, the interview. Ask me the questions **a few at a time**
> and wait for my answers. Do not dump all fourteen at me, and do not start
> writing files until the interview is done.
>
> Four things I care about more than speed:
>
> - **Ask before inventing.** The world is in my head. When something is
>   unspecified and the choice matters, ask me. When it does not matter, pick
>   something plain and tell me you picked it.
> - **Write less than you want to.** Three good locations beat twenty. Every
>   record costs context budget on every turn, forever.
> - **Never fill a field to be tidy.** An empty field means nobody has decided
>   yet, which is information. Inventing a character's fear because the schema
>   has a slot for it produces plausible noise.
> - **At the end of every stage, tell me three things**: what you wrote, what
>   you chose without being told, and what you left empty on purpose. The
>   second one is how I find the thing you quietly guessed wrong.
>
> Begin with Stage 0.

---

## What you will have when you are done

```
<your world>/
  world.json      identity and settings. Small, and it stays small.
  records/
    characters/mira-vale.md      one record, one file
    locations/harbour-steps.md
    threads/ items/ organizations/ relationships/
  lore/           premise, voice, promises, and anything else -- prose, no schema
  rules/          optional: how this world plays differently
  assets/         images, audio, video
```

A record is frontmatter and a body. The fields the engine computes over sit on
top; the prose sits underneath:

```markdown
---
id: character:mira-vale
name: Mira Vale
visual_identity: {age: late thirties, hair: black, cropped short}
current_state: {location: location:harbour-steps}
gm_notes: She has already sold the charts.
---
A pilot who owes the harbourmaster more than she can pay.
```

**The id is the record's identity, not the filename.** Rename or move a file
freely; change an `id` and you orphan everything pointing at it.

A small world can keep its records inside `world.json` instead, and the engine
reads either. `python rpg/tools/world.py split <slug>` converts one into the
other when it outgrows a single file — which happens sooner than you would
think, because past a few hundred kilobytes no model can read it at all.

Done is **not** complete. Done is three prose files, a `world.json` that passes
the checker, three or four locations, two or three characters, one thread, and
a global image prompt. A world that size is playable, and playing it will tell
you more about what it needs than another day of writing will.

## Checking it

From the engine repository:

```bash
python rpg/tools/world.py check <slug>
```

Cheap, safe to re-run, and it catches the failure that otherwise looks exactly
like success: a rules file named for a slot that does not exist, sitting there
never applying.

## Versioning it

This folder is already a git repository if `world init` was run on it. Commit
as you go — the engine records which commit a campaign was started from, so a
world's history is what lets a live game take your later changes without
losing what happened in it.

```bash
git add -A && git commit -m "Stage 1: premise, voice, promises"
```

Large binaries under `assets/` are tracked through Git LFS from the first
commit. That is deliberate: retrofitting LFS rewrites history, and you cannot
ask that of a repository you have already pushed.
