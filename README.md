# Gaia

> **"Seven nations. Seven magics. One world worth living in."**

A complete, self-contained world built for **[Storyforge](https://github.com/)**—an AI-driven, character-driven interactive storytelling and roleplaying game engine.

---

## Setting & Premise Overview

Gaia is an expansive dark fantasy world of seven great nations, each inspired by distinct historical and mythological cultures and grounded in its own unique tradition of magic.

The world is shaped by adult realism, political intrigue, and personal tragedy. Frayed truces, succession crises, illicit affairs, ambition, and moral ambiguity are depicted plainly without melodrama or gratuitous shock value. There are no prophecies, no "chosen ones," and no single hero who can save the world.

### The Seven Nations & Their Magics

| Nation | Cultural Touchstone | Magic System & Flavor | Key Themes & Flashpoints |
|---|---|---|---|
| **Tsukuyomi Shogunate** | Feudal Japan / Shogunate | **Shrine Magic:** Ritual spirit-wards, ofuda talismans, kannushi and miko ceremonies. Scaled by devotion and precision. | Yokai and humans living in proximity. Aging Shogun, unspoken succession, and tension between regional samurai clans. |
| **Valdris** | High Medieval Europe | **Dragon-Bonded Oaths:** Knights swear lifelong pacts to dragons for fire resistance, longevity, and enhanced strength. | The oldest kingdom in Gaia. White stone towers and mountain keeps. Dragons have ceased answering new oaths for a generation; royal bastards and legitimate heirs vie for power. |
| **Sangguo** | Ancient China / Three Kingdoms | **Chi Cultivation & Spirit-Pacts:** Martial discipline, inner energy manipulation, and advisory pacts with qilin and ancestor spirits. | Warlord states (Jin, Chu, Wei) held in an expiring three-year truce. Intrigues in the Jade Pavilion and covert preparations for war. |
| **Verdania** | Amazonian South America | **Shamanic Spirit-Pacts:** Living relational bonds with ancient spirits of river, tree, stone, and beast. | Canopy cities, river trade, and temple cities overgrown by jungle. Reverence, negotiation, and balance with the wild. |
| **Hrafnland** | Norse / Viking | **Runic Seidr:** Power carved into wood, bone, and stone, paired with prophetic visions practiced by the völur. | Fjords, longships, and jarls meeting annually at the Althing. Frost giants dwelling in the deep mountains. |
| **Al-Khayzar** | Persian & Arabian Nights | **Djinn-Binding:** Transactional, ironclad supernatural contracts with desert fire-spirits. | Desert city-states, spice bazaars, and oasis routes preserved under the sacred Pact of the Lamp. |
| **The Tide Archipelago** | Polynesian & SE Asian Voyagers | **Wayfinding Song-Magic:** Communal oral songs that carry power across open water to steer currents, calm storms, and communicate. | Island atolls and master outrigger navigators under existential threat as rising sea levels swallow coastlines. |

### Global Setting Constants

* **Reincarnation:** Extremely rare souls arrive carrying memories of another world ("god-touched" or "cursed"). They simply happen without grand explanations.
* **The Old Roads:** Ancient spirit-paths that once connected every corner of Gaia. Though mostly broken, surviving fragments turn a month's journey into an afternoon.
* **Tone & Narrative Voice:** Second-person, unflinching, close, and unhurried. Concrete nouns and plain verbs. Magic is part of daily life rather than an abstract academic treatise.

---

## Repository Structure

Gaia follows Storyforge’s **prose-before-records** architecture: write freeform prose in `lore/` until the engine must compute over, count, or display structured data in `records/`.

```
gaia/
├── world.json                 # World manifest: identity, narration voice, art styling, presets
├── lore/                      # Freeform markdown worldbuilding (no rigid schema)
│   ├── premise.md             # Core setting premise and boundaries
│   ├── nations.md             # Detailed profiles of the seven nations
│   ├── races.md               # Racial cultures, morphology, and visual references
│   ├── geopolitics.md         # Faction politics and treaties
│   ├── religion.md            # Faiths, pantheons, and spiritual pacts
│   ├── magic.md               # Overview of the seven magical traditions
│   ├── gender.md              # Social, cultural, and gender customs
│   └── voice.md               # Narration voice & register guidance
├── records/                   # 1,000+ canonical structured records (YAML frontmatter + Markdown body)
│   ├── characters/            # 380+ character sheets (attributes, equipment, visual prompts)
│   ├── locations/             # 240+ locations (settlements, regions, shrines, landmarks)
│   ├── items/                 # 140+ catalog items with occupancy and layer metadata
│   ├── relationships/         # 120+ directed character relationship records
│   ├── organizations/         # 60+ guilds, clans, orders, and factions
│   ├── threads/               # Active plot threads, tensions, and quest hooks
│   └── lore/                  # Structured canonical lore entities
├── nation_locations/          # Regional location JSON datasets
├── rules/                     # Engine rule modules (e.g. narration rules)
├── assets/                    # Media assets (images, maps)
├── equipment.py               # Shared domain logic for equipment occupancy & rules
├── validate_equipment.py      # Equipment validator script
├── test_equipment.py          # Equipment test suite
├── validate_wiki_links.py     # Wiki-link validation script
└── test_wiki_links.py         # Wiki-link test suite
```

---

## Core Systems & Authoring Conventions

Detailed specifications for contributors and AI agents are documented in **[`AGENTS.md`](AGENTS.md)** and **[`WORLD-KIT.md`](WORLD-KIT.md)**.

### 1. Wiki-Link Entity References
Refer to existing canonical records in Markdown prose using:
* `[[type:stable-id]]` (e.g., `[[character:ashikara-renjiro]]`)
* `[[type:stable-id|display text]]` (e.g., `[[character:ashikara-renjiro|Prince Renjiro]]`)

**Rules:**
* The target always comes before the optional display text.
* Never invent IDs for uncreated entities; use plain text for incidental mentions.
* Structured YAML ID fields (e.g., `affiliations`, `participants`, `locations`) must use raw IDs only, never wiki-links.

### 2. Unified Equipment System ([`EQUIPMENT-SYSTEM.md`](EQUIPMENT-SYSTEM.md))
Character equipment follows a layered schema:
* **Wearables:** Organized into `underwear`, `clothing`, and `armor` with body region coverage.
* **Held Items:** Hand occupancy (`left`, `right`) with two-handed items occupying both slots and deduplicated modifiers.
* **Accessories & Ammunition:** Dedicated slots (`accessories: []`, `ammo: null`).
* **Domain & Validation:** Handled by `equipment.py` and validated across all items and characters by `validate_equipment.py`.

### 3. Visual Prompt Generation (One Obsession / ComfyUI)
Image prompts in `visual.prompt` follow Danbooru-first tag conventions:
* Focus strictly on scene-specific, physically visible traits (gender, age category, species morphology, build, hair, eyes, distinctive scars, attire, lighting).
* Never include quality buzzwords (`masterpiece`, `best quality`), negative prompts, or style descriptors (these are applied globally via `world.json`).
* Respect character physical fidelity and race morphology baselines defined in `lore/races.md`.

### 4. Typed Relationships (`records/relationships/`)
* Family, romantic, and political bonds are stored exclusively in pairwise files under `records/relationships/`, not as reciprocal fields in character files.
* Records define directional perspectives (`disposition: -100 to 100`), verified kinship facts, and chronological history events.

---

## Tooling & Validation

To verify the integrity of the world's data, run the local test suites:

```bash
# Validate equipment occupancy, layer conflicts, and character loadouts
python validate_equipment.py --dir .
python test_equipment.py

# Validate wiki-link references and syntax
python validate_wiki_links.py
python test_wiki_links.py
```

---

## Essential Rules

1. **Write prose before records:** Do not create a record when a paragraph in `lore/` suffices. Records add context budget overhead and schema commitments.
2. **`world.id` never changes:** The Storyforge engine keys campaigns to the immutable `world.id` defined in `world.json`.
3. **Commit as you go:** Live campaigns track their state against specific git commits of this repository.
