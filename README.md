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
├── world.json                 # World manifest: identity, calendar, tones, settings
├── README.md                  # World overview & guide
├── AGENTS.md                  # Rules and instructions for AI agents
├── records/                   # 1,100+ canonical structured records (YAML frontmatter + Markdown)
│   ├── characters/            # 418 characters organized by nation / origin
│   │   ├── al-khayzar/        # 58 characters
│   │   ├── hrafnland/         # 58 characters
│   │   ├── sangguo/           # 61 characters
│   │   ├── tide-archipelago/  # 57 characters
│   │   ├── tsukuyomi/         # 57 characters
│   │   ├── valdris/           # 56 characters
│   │   ├── verdania/          # 54 characters
│   │   └── other/             # 17 characters (Mazoku, Sylvan, Heavenly Realm)
│   ├── locations/             # 249 locations organized by nation / region
│   │   ├── al-khayzar/        # 31 locations
│   │   ├── borders/           # 19 locations (Silk Pass, Verdmarch, Moon Strait, Skerries)
│   │   ├── hrafnland/         # 28 locations
│   │   ├── sangguo/           # 34 locations
│   │   ├── tide-archipelago/  # 37 locations
│   │   ├── tsukuyomi/         # 32 locations
│   │   ├── valdris/           # 38 locations
│   │   ├── verdania/          # 29 locations
│   │   └── other/             # 1 location (Heavenly Realm)
│   ├── items/                 # 159 catalog items organized by category
│   │   ├── clothing/          # 121 wearable garments & undergarments
│   │   ├── weapons-and-armor/ # 3 weapons & armors
│   │   ├── tools-and-gear/    # 11 tools & adventuring items
│   │   ├── relics-and-mementos/ # 15 relics & mementos
│   │   └── accessories/       # 9 accessories & documents
│   ├── organizations/         # 62 factions & guilds organized by nation / region
│   ├── relationships/         # 134 directed pairwise character relationship records
│   ├── threads/               # 37 active plot threads (quests, tensions, conflicts)
│   ├── lore/                  # 23 structured lore records (beliefs, magic, races baseline)
│   └── experiences/           # 15 campaign events and historical memories
├── lore/                      # Freeform markdown worldbuilding (recursively read by engine)
│   ├── premise.md             # Core setting premise and boundaries
│   ├── nations.md             # Detailed profiles of the seven nations
│   ├── races.md               # Racial cultures, morphology, and visual references
│   ├── geopolitics.md         # Faction politics and treaties
│   ├── religion.md            # Faiths, pantheons, and spiritual pacts
│   ├── heavenly-realm.md      # The higher realm
│   ├── promises.md            # Narrative promises
│   └── voice.md               # Narration voice & register guidance
├── docs/                      # World specifications & reference documents
│   ├── WORLD-KIT.md           # Storyforge World Kit specification
│   ├── GET-STARTED.md         # Authoring quickstart guide
│   ├── EQUIPMENT-SYSTEM.md    # Unified equipment and layering specification
│   ├── PROMPTING.md           # Visual prompt engineering guide
│   └── RELATIONSHIP-PROPOSALS.md # Working relationship proposals
├── tools/                     # Domain logic, verification & test suites
│   ├── equipment.py           # Shared domain logic for equipment rules
│   ├── validate_equipment.py  # Equipment validator script
│   ├── test_equipment.py      # Equipment test suite
│   ├── validate_wiki_links.py # Wiki-link validation script
│   ├── test_wiki_links.py     # Wiki-link test suite
│   ├── migrate_equipment.py   # Equipment migration utility
│   └── check_chars.py         # Character stats auditor
├── rules/                     # Engine rule modules (e.g. narration rules)
├── assets/                    # Media assets (images, audio, video)
└── archive/                   # Archived scaffolding and legacy datasets
    └── nation_locations/      # Legacy location JSON imports (superseded by records)
```

---

## Core Systems & Authoring Conventions

Detailed specifications for contributors and AI agents are documented in **[`AGENTS.md`](AGENTS.md)** and **[`docs/WORLD-KIT.md`](docs/WORLD-KIT.md)**.

### 1. Wiki-Link Entity References
Refer to existing canonical records in Markdown prose using:
* `[[type:stable-id]]` (e.g., `[[character:ashikara-renjiro]]`)
* `[[type:stable-id|display text]]` (e.g., `[[character:ashikara-renjiro|Prince Renjiro]]`)

**Rules:**
* The target always comes before the optional display text.
* Never invent IDs for uncreated entities; use plain text for incidental mentions.
* Structured YAML ID fields (e.g., `affiliations`, `participants`, `locations`) must use raw IDs only, never wiki-links.

### 2. Unified Equipment System ([`docs/EQUIPMENT-SYSTEM.md`](docs/EQUIPMENT-SYSTEM.md))
Character equipment follows a layered schema:
* **Wearables:** Organized into `underwear`, `clothing`, and `armor` with body region coverage.
* **Held Items:** Hand occupancy (`left`, `right`) with two-handed items occupying both slots and deduplicated modifiers.
* **Accessories & Ammunition:** Dedicated slots (`accessories: []`, `ammo: null`).
* **Domain & Validation:** Handled by `tools/equipment.py` and validated across all items and characters by `tools/validate_equipment.py`.

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

To verify the integrity of the world's data, run the local test suites from the repository root:

```bash
# Validate equipment occupancy, layer conflicts, and character loadouts
python tools/validate_equipment.py
python tools/test_equipment.py

# Validate wiki-link references and syntax
python tools/validate_wiki_links.py
python tools/test_wiki_links.py
```

---

## Essential Rules

1. **Write prose before records:** Do not create a record when a paragraph in `lore/` suffices. Records add context budget overhead and schema commitments.
2. **`world.id` never changes:** The Storyforge engine keys campaigns to the immutable `world.id` defined in `world.json`.
3. **Commit as you go:** Live campaigns track their state against specific git commits of this repository.
