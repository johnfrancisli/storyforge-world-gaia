# Gaia World Index & Navigation Portal

Welcome to the central directory of **Gaia**. This index provides direct navigation across all seven nations, border regions, canonical records, and systems.

---

## The Seven Nations

| Nation | Magic & Theme | Lore | Characters | Locations | Factions |
|---|---|---|---|---|---|
| **Tsukuyomi Shogunate** | Shrine Magic, Ofuda, Kami & Yokai | [lore:nations](lore/nations.md) | [Characters (57)](records/characters/tsukuyomi/) | [Locations (32)](records/locations/tsukuyomi/) | [Orgs (9)](records/organizations/tsukuyomi/) |
| **Kingdom of Valdris** | Dragon-Bonded Oaths, Knights, Keeps | [lore:nations](lore/nations.md) | [Characters (56)](records/characters/valdris/) | [Locations (38)](records/locations/valdris/) | [Orgs (9)](records/organizations/valdris/) |
| **Sangguo** | Chi Cultivation, Spirit-Pacts, Three Kingdoms | [lore:nations](lore/nations.md) | [Characters (61)](records/characters/sangguo/) | [Locations (34)](records/locations/sangguo/) | [Orgs (9)](records/organizations/sangguo/) |
| **Verdania** | Shamanic Spirit-Pacts, Canopy Cities | [lore:nations](lore/nations.md) | [Characters (54)](records/characters/verdania/) | [Locations (29)](records/locations/verdania/) | [Orgs (8)](records/organizations/verdania/) |
| **Hrafnland** | Runic Seidr, Fjords, Longships, Völur | [lore:nations](lore/nations.md) | [Characters (58)](records/characters/hrafnland/) | [Locations (28)](records/locations/hrafnland/) | [Orgs (7)](records/organizations/hrafnland/) |
| **Al-Khayzar** | Djinn-Binding, Oases, Bazaars, Pact of the Lamp | [lore:nations](lore/nations.md) | [Characters (58)](records/characters/al-khayzar/) | [Locations (31)](records/locations/al-khayzar/) | [Orgs (9)](records/organizations/al-khayzar/) |
| **The Tide Archipelago** | Wayfinding Song-Magic, Voyagers, Reefs | [lore:nations](lore/nations.md) | [Characters (57)](records/characters/tide-archipelago/) | [Locations (37)](records/locations/tide-archipelago/) | [Orgs (7)](records/organizations/tide-archipelago/) |

---

## Contested Frontiers & Other Realms

- **Border & Contested Regions**: [Locations (19)](records/locations/borders/) · [Orgs (4)](records/organizations/borders/)
  - **The Silk Pass**: Trade gateway between Sangguo and Al-Khayzar.
  - **The Verdmarch**: Contested border forest between Valdris and Verdania.
  - **The Moon Strait**: International waters between Valdris and Hrafnland.
  - **The Basalt Skerries**: Storm-swept shoals between Hrafnland and Valdris.
- **The Heavenly Realm & Other Peoples**: [Locations (1)](records/locations/other/) · [Characters (17)](records/characters/other/)
  - Mazoku, Sylvan, Heavenly Realm, and independent wayfarers.

---

## Catalog & Global Records

- **Items & Equipment (159)**:
  - [Clothing & Wearables (121)](records/items/clothing/) — Undergarments, daily attire, formal wear, and robes.
  - [Weapons & Armor (3)](records/items/weapons-and-armor/) — Weapons, shields, and battle armor.
  - [Tools & Adventuring Gear (11)](records/items/tools-and-gear/) — Astrolabes, carving sets, lockpicks, and manuals.
  - [Relics & Mementos (15)](records/items/relics-and-mementos/) — Dragon relics, ceremonial artifacts, and keepsake tokens.
  - [Accessories & Miscellaneous (9)](records/items/accessories/) — Jewelry, documents, talismans, and resources.
- **Relationships (134)**: [records/relationships/](records/relationships/) — Pairwise directional bonds, kinship, and stage histories.
- **Active Threads (37)**: [records/threads/](records/threads/) — Quests, political tensions, mysteries, and faction conflicts.
- **Structured Lore (23)**: [records/lore/](records/lore/) — Canonical beliefs per nation, spirit hierarchies, festivals, and race baselines.
- **Campaign Experiences (15)**: [records/experiences/](records/experiences/) — Key historical incidents, memories, and chapter milestones.

---

## World Documentation & Tooling

- **Authoring & Specifications (docs/)**:
  - [WORLD-KIT.md](docs/WORLD-KIT.md) — The complete Storyforge World Kit specification.
  - [GET-STARTED.md](docs/GET-STARTED.md) — Five-minute quickstart guide for world builders.
  - [EQUIPMENT-SYSTEM.md](docs/EQUIPMENT-SYSTEM.md) — Three-layer wearable rules, hand occupancy, and slot stacking.
  - [PROMPTING.md](docs/PROMPTING.md) — Danbooru-first visual prompt engineering conventions for ComfyUI.
  - [RELATIONSHIP-PROPOSALS.md](docs/RELATIONSHIP-PROPOSALS.md) — In-progress relationship proposals and kin tracking.
- **Verification Scripts (	ools/)**:
  - python tools/validate_equipment.py — Validates all character equipment, layers, and item occupancy.
  - python tools/test_equipment.py — Runs the equipment domain test suite.
  - python tools/validate_wiki_links.py — Validates wiki-link syntax, entity references, and YAML raw IDs.
  - python tools/test_wiki_links.py — Runs the wiki-link validation test suite.
