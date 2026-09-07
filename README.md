# Gaia

*Not yet written. This world is scaffolded and waiting for its first stage.*

A self-contained [Storyforge](https://github.com/) world: everything the engine
needs to run it, and everything a person needs to author it, in one folder you
can clone.

## Start here

**[`GET-STARTED.md`](GET-STARTED.md)** — the five-minute version. One block to
paste into a chat with any capable AI, which then interviews you about the
world and writes it down as you answer.

**[`WORLD-KIT.md`](WORLD-KIT.md)** — the full brief: what the engine guarantees
and will not let a world override, the prose-before-records rule, and the
stage-by-stage build order the AI follows.

## What is in here

| | |
|---|---|
| `world.json` | Identity, settings and records. Every block carries a `_help` key. |
| `lore/` | Prose — premise, voice, promises. No schema, and most of a world belongs here. |
| `rules/` | Optional. Markdown that changes how this world *plays*, not just how it reads. |
| `assets/` | Images, audio and video, referenced by world-relative path. |
| `campaigns/` | Play data. Deliberately not versioned — it is downstream of this world, not part of it. |

## The two rules worth knowing before editing anything

**Write prose until the engine has to compute over it.** A record costs a
schema, a place in the context budget and a visibility decision. A paragraph
costs nothing and reads better. Promote a paragraph to a record when something
must point at it, be counted, appear in a panel, or be hidden from the player —
not before.

**Use wiki links to reference canonical records in prose.** When you mention
an existing record in Markdown, use `[[type:stable-id]]` or
`[[type:stable-id|display text]]`. The target comes before the optional
display text. See [`WORLD-KIT.md`](WORLD-KIT.md) for the full convention.

**`world.id` never changes.** The engine keys canon on it, and campaigns record
which commit of this repository they were started from. Rename Gaia freely; do
not touch its id, or every campaign playing it is orphaned.

## Why this is versioned

Playing this world does not modify it. A campaign takes a **copy** at the commit
it started from, and plays that — so nothing that happens in a story can rewrite
what is written here.

When this world moves forward, live campaigns can take the changes: the engine
compares three things per record — this repository now, the campaign's copy now,
and the commit the copy was taken from — and only asks the player about records
where both sides changed. Everything else lands quietly.

That is what a world's git history is *for* here. Commit as you go.

## Checking it

From the engine repository:

```bash
python rpg/tools/world.py check <slug>
```

Cheap and safe to re-run. It catches the failure that otherwise looks exactly
like success: a rules file named for a slot that does not exist, sitting there
never applying.

Large binaries under `assets/` are tracked with Git LFS from the first commit —
retrofitting LFS rewrites history, which is not something to ask of a repository
that has already been pushed.
