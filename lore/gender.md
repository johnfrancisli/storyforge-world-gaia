# Gender in Gaia

> **DRAFT — written to be argued with, not agreed with.**
>
> Almost nothing about gender was established anywhere in Gaia's lore, so most
> of what follows is invented to give you something to react to. Every claim
> here is a guess unless you keep it. Rewrite freely; the only part worth
> preserving is the shape — that `gender:` on a character record has to resolve
> to something this file names.

## What the field means

Every character record carries a `gender:` field. It is not a biological claim
and it is not a pronoun — it is **the social role a person occupies in their own
culture**, which is what the narrator needs in order to write a room correctly.

A character may hold different standing in a different nation. Gaia has no
single gender order, and a world with seven cultures this distinct should not
pretend otherwise.

## The common terms

Most of Gaia, most of the time, recognises:

- **Woman** — `gender: woman`
- **Man** — `gender: man`

These carry different weight in different places. A woman in [[location:hrafnland|Hrafnland]] who owns
a ship commands it; a woman in Valdris who owns land often holds it through a
male relative's name. Neither is the default and neither is the exception.

## Where the world does not stop there

**Tsukuyomi** recognises a third standing that has no clean translation. Those
who serve a shrine may set aside their prior standing entirely, and are
addressed by their office rather than by gender. The spirit-touched are
frequently among them. Record as `gender: shrine-bound`.

**[[location:tide-archipelago|The Tide Archipelago]]** treats gender as something a person may be recognised
into rather than born with. A navigator's standing follows the voyage, not the
body. Record as `gender: navigator-kind` when it applies — most Archipelago
characters simply use woman or man.

**[[location:verdania|Verdania]]**'s canopy cities have no fixed term at all. The jungle-facing
communities describe people by what they tend, not by what they are, and a
character raised there may hold no gender in the sense other nations mean.
Record as `gender: untold`.

**[[location:al-khayzar|Al-Khayzar]]** distinguishes those under a djinn contract, whose standing is
suspended for its duration. This is a legal condition rather than a gender, but
it displaces one, and characters bound this way are addressed neither as women
nor as men. Record as `gender: contract-held`.

## Races that complicate it

**Dragon-kin (Ryujin)** are said to change over a long life, and the older ones
are addressed by lineage rather than gender. **Demon-folk (Mazoku)** are
described by outsiders in terms that do not survive contact with how Mazoku
describe themselves — which is a thing the world should be able to be wrong
about, in the mouths of characters who are wrong about it.

Elves, dwarves, cat-folk, beast-kin and river-folk broadly follow the customs of
wherever they live, rather than carrying their own.

## The values a record may use

Until this file says otherwise:

```
woman · man · shrine-bound · navigator-kind · untold · contract-held
```

A character whose gender has not been decided leaves the field empty. **Empty is
information** — it says nobody has decided yet, which is true of most of Gaia's
cast right now and better than a guess somebody has to undo.

## What this is not

This file does not describe attraction, partnership, or family structure. Those
belong in the nations' own lore, where they can differ properly, rather than
being flattened into one page about gender.
