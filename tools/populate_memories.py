#!/usr/bin/env python3
"""
tools/populate_memories.py — Populate catastrophic memories and enrich backgrounds across Gaia.

Ensures every character in Gaia has at least one canonical catastrophic memory,
eliminating single-person memories and enriching biographies with lived experiences
of major regional disasters and crises.
"""

import os
import re
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHAR_DIR = REPO_ROOT / "records" / "characters"

# Event definitions with canonical experience IDs and descriptive phrases
EVENTS = {
    "green-flame": {
        "id": "campaign-event/the-green-flame-at-the-grand-bazaar",
        "exp_link": "[[experience:the-green-flame-at-the-grand-bazaar|the Green Flame at the Grand Bazaar]]",
        "templates": [
            "The memory of {exp_link} remains vividly etched in their thoughts, when jade djinn fire tore through the market stalls and proved how perilously thin the boundary of control truly is.",
            "Having witnessed the terrifying aftermath of {exp_link}, they carry an enduring vigilance against the volatile forces simmering beneath the city's trade pacts.",
            "Their life was marked by the chaos of {exp_link}, a catastrophic blaze that disrupted trade routes and served as a stark reminder of the cost of broken bindings.",
        ]
    },
    "broken-astrolabe": {
        "id": "campaign-event/the-night-of-the-broken-astrolabe",
        "exp_link": "[[experience:the-night-of-the-broken-astrolabe|the night of the broken astrolabe]]",
        "templates": [
            "They retain a sharp recollection of {exp_link}, when the academy's great brass instrument shattered and the celestial navigation charts were thrown into disarray.",
            "The sudden crisis of {exp_link} left a lasting mark on their understanding of the stars, reminding them that even ancient calculations can unravel.",
        ]
    },
    "frost-slip": {
        "id": "campaign-event/the-frost-slip-shattering",
        "exp_link": "[[experience:the-frost-slip-shattering|the frost-slip shattering]]",
        "templates": [
            "The thunderous roar of {exp_link} still echoes in their memory, recalling the day the glacier wall collapsed into the fjord, crushing ships and flooding the lower quays.",
            "They carry the grim memory of surviving {exp_link}, an icy disaster that reshaped the harbor lines and tested the endurance of every hearth in the settlement.",
            "The catastrophic surge from {exp_link} remains a grim touchstone in their life, cementing their respect for the deadly unpredictability of the northern ice.",
        ]
    },
    "fog-mother": {
        "id": "campaign-event/the-fog-mothers-warning",
        "exp_link": "[[experience:the-fog-mothers-warning|the Fog Mother's warning]]",
        "templates": [
            "They will never forget the chilling silence of {exp_link}, when unnatural seidr mist crept off the freezing sea and the voices of the drowned drifted over the waves.",
            "The eerie omens during {exp_link} left a permanent impression on their spirit, instilling a deep wariness of the ancient powers lingering in the deep fjords.",
        ]
    },
    "canal-collapse": {
        "id": "campaign-event/the-canal-collapse-at-sanyuan",
        "exp_link": "[[experience:the-canal-collapse-at-sanyuan|the canal collapse at Sanyuan]]",
        "templates": [
            "The terrifying silt breach during {exp_link} remains etched in their mind, when rushing floodwaters smashed cargo fleets and brought the region to the brink of famine.",
            "They carry vivid memories of the desperate labor following {exp_link}, watching the vital waterways choked with mud and realizing how fragile the states' grain supply truly was.",
            "The disaster of {exp_link} left an indelible mark on their outlook, demonstrating firsthand how quickly neglected foundations can turn into catastrophe.",
        ]
    },
    "tea-conclave": {
        "id": "campaign-event/the-steaming-cup-at-the-tea-conclave",
        "exp_link": "[[experience:the-steaming-cup-at-the-tea-conclave|the steaming cup at the tea conclave]]",
        "templates": [
            "The deadly intrigue of {exp_link} taught them how close the three rival states teeter on the razor edge of war, leaving them forever watchful of courtly hospitality.",
            "The shock of {exp_link} hardened their instincts, proving that poison and political desperation are never far from diplomatic smiles.",
        ]
    },
    "motu-lotu": {
        "id": "campaign-event/the-drowning-of-motu-lotu",
        "exp_link": "[[experience:the-drowning-of-motu-lotu|the drowning of Motu Lotu]]",
        "templates": [
            "The heartbreaking tragedy of {exp_link} is permanently stamped on their memory, having witnessed the rising ocean surge swallow an entire inhabited atoll under the starlight.",
            "They carry the heavy burden of remembering {exp_link}, when forty families fled into the night as the reef crumbled beneath unprecedented tidal waves.",
            "The terrifying evacuation during {exp_link} remains a defining moment of their life, reinforcing their commitment to safeguarding the voyagers against the creeping sea.",
        ]
    },
    "dive-quarrel": {
        "id": "campaign-event/the-great-dive-quarrel",
        "exp_link": "[[experience:the-great-dive-quarrel|the great dive quarrel]]",
        "templates": [
            "The bloodshed and bitter recriminations of {exp_link} left a lasting scar, warning them of the violent desperation that erupts when precious deep-water beds are contested.",
            "They still remember the fury of {exp_link}, an ordeal that severed old island alliances and cast a shadow over the pearl harvests.",
        ]
    },
    "ward-bell": {
        "id": "campaign-event/the-night-the-ward-bell-cracked",
        "exp_link": "[[experience:the-night-the-ward-bell-cracked|the night the ward bell cracked]]",
        "templates": [
            "The sudden spiritual dread of {exp_link} remains unforgettable, recalling the moment the mountain barrier faltered and the restless yokai crept closer to human thresholds.",
            "They vividly recall the eerie silence of {exp_link}, when shrine mirrors clouded with breach signs and the protective boundaries of the realm began to fray.",
            "The hairline fracture during {exp_link} signaled a profound shift in their life, sharpening their awareness of the fragile spiritual balance keeping the settlement safe.",
        ]
    },
    "tea-poison": {
        "id": "campaign-event/the-tea-poison-at-the-moon-viewing",
        "exp_link": "[[experience:the-tea-poison-at-the-moon-viewing|the tea poison at the moon-viewing]]",
        "templates": [
            "The terror and suspicion following {exp_link} left a sharp impression, proving that even the most sacred clan banquets can harbor venomous treachery.",
            "The scandal of {exp_link} deepened their guarded nature, having seen high samurai and shrine elders throw accusations in the shadow of an attempted murder.",
        ]
    },
    "dragon-silence": {
        "id": "campaign-event/the-dragon-silence-at-sunhelm",
        "exp_link": "[[experience:the-dragon-silence-at-sunhelm|the Dragon Silence at Sunhelm]]",
        "templates": [
            "The lingering shock of {exp_link} remains a defining sorrow of their generation, an eerie quietude that settled across the high aeries when the great wyrms ceased answering the binding calls.",
            "They carry the sober memory of {exp_link}, an unheralded crisis that fractured knightly convictions and shook the very foundations of the kingdom's ancient order.",
            "The kingdom-wide disquiet of {exp_link} profoundly shaped their worldview, teaching them that even the most sacred oaths can fade into cold silence.",
        ]
    },
    "truce-breaking": {
        "id": "campaign-event/the-truce-breaking-at-greyfen",
        "exp_link": "[[experience:the-truce-breaking-at-greyfen|the truce-breaking at Greyfen]]",
        "templates": [
            "The sudden violence of {exp_link} remains fresh in their thoughts, when armed clashes on the misty docks proved how swiftly regional peace can crumble into open hostility.",
            "Having endured the tension of {exp_link}, they maintain a cynical eye toward treaties that rely on the good faith of armed factions.",
        ]
    },
    "serpent-gate": {
        "id": "campaign-event/the-serpent-gate-whisper",
        "exp_link": "[[experience:the-serpent-gate-whisper|the serpent gate whisper]]",
        "templates": [
            "The unsettling reverberations of {exp_link} still trouble their thoughts, when the ancient stone carvings groaned and corrupted jungle spirits began to stir in the deep canopy.",
            "They vividly recall the dread during {exp_link}, an ominous awakening that spoiled river waters and warned that the old temple seals were decaying.",
            "The eerie spiritual tremors of {exp_link} left an enduring mark, strengthening their vigilance against the wild forces stirring beyond the stilt platforms.",
        ]
    },
    "jaguar-moon": {
        "id": "campaign-event/the-rogue-hunt-of-the-jaguar-moon",
        "exp_link": "[[experience:the-rogue-hunt-of-the-jaguar-moon|the rogue hunt of the Jaguar Moon]]",
        "templates": [
            "The bloody nightmare of {exp_link} proved to them how lethal the rainforest becomes when ancient taboos are shattered and warped beasts breach the canopy defenses.",
            "The panic of {exp_link} remains a stark warning in their memory, recalling the desperate defense when shadow panthers struck the outer trade posts.",
        ]
    },
}


def select_event_key(nation, role, text):
    text_lower = text.lower()
    role_lower = role.lower()

    if nation == "al-khayzar":
        if any(w in role_lower or w in text_lower for w in ["astrolab", "astronom", "astrolog", "celestial", "scribe", "scholar", "cartograph"]):
            return "broken-astrolabe"
        return "green-flame"

    elif nation == "hrafnland":
        if any(w in role_lower or w in text_lower for w in ["skald", "völva", "volva", "seer", "rune", "priest", "seidr", "mystic"]):
            return "fog-mother"
        return "frost-slip"

    elif nation == "sangguo":
        if any(w in role_lower or w in text_lower for w in ["warlord", "general", "minister", "strategist", "diplomat", "assassin", "magistrate", "envoy", "noble"]):
            return "tea-conclave"
        return "canal-collapse"

    elif nation == "tide-archipelago":
        if any(w in role_lower or w in text_lower for w in ["pearl", "diver", "coral", "shell", "deep-water", "harvest"]):
            return "dive-quarrel"
        return "motu-lotu"

    elif nation == "tsukuyomi":
        if any(w in role_lower or w in text_lower for w in ["daimyo", "shogun", "noble", "court", "samurai", "tea master", "courtesan", "geisha", "chancellor"]):
            return "tea-poison"
        return "ward-bell"

    elif nation == "valdris":
        if any(w in role_lower or w in text_lower for w in ["greyfen", "mercenary", "smuggler", "border", "toll", "harbor", "trader"]):
            return "truce-breaking"
        return "dragon-silence"

    elif nation == "verdania":
        if any(w in role_lower or w in text_lower for w in ["hunter", "canopy runner", "trapper", "jaguar", "beast", "tracker"]):
            return "jaguar-moon"
        return "serpent-gate"

    else:  # other
        if any(w in role_lower or w in text_lower for w in ["elf", "sylvan", "fletcher"]):
            return "dragon-silence"
        elif any(w in role_lower or w in text_lower for w in ["canopy", "jungle", "river"]):
            return "serpent-gate"
        elif any(w in role_lower or w in text_lower for w in ["water", "sea", "siren"]):
            return "motu-lotu"
        elif any(w in role_lower or w in text_lower for w in ["warrior", "orc", "mazoku"]):
            return "truce-breaking"
        elif any(w in role_lower or w in text_lower for w in ["fox", "spirit", "whisper"]):
            return "tea-poison"
        return "dragon-silence"


def append_to_biography(content, sentence):
    m = re.search(r"(\nbiography:\s*)(.*?)(\n[a-z_]+:)", content, re.DOTALL)
    if not m:
        return content
    prefix = m.group(1)
    body = m.group(2)
    suffix = m.group(3)

    body_stripped = body.strip()
    if body_stripped.startswith("\x27") and body_stripped.endswith("\x27"):
        inner = body_stripped[1:-1]
        escaped_sentence = sentence.replace("\x27", "\x27\x27")
        new_body = "\x27" + inner + " " + escaped_sentence + "\x27"
    else:
        new_body = body.rstrip() + "\n  " + sentence

    return content[:m.start()] + prefix + new_body + suffix + content[m.end():]


def process_character_file(filepath, template_idx):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False, "Not valid frontmatter"

    fm = parts[1]
    data = yaml.safe_load(fm)
    if not data or not isinstance(data, dict):
        return False, "Failed to parse YAML"

    char_id = data.get("id", "")
    nation = Path(filepath).parent.name
    role = data.get("role", "")
    existing_memories = data.get("memories", [])

    event_key = select_event_key(nation, role, content)
    event_info = EVENTS[event_key]
    event_id = event_info["id"]

    modified = False

    # 1. Update memories if empty
    if not existing_memories:
        content = re.sub(r"\nmemories:\s*\[\s*\]", f"\nmemories:\n- {event_id}", content, count=1)
        modified = True

    # 2. Enrich biography if experience is not mentioned
    exp_slug = event_id.split("/")[-1]
    bio_text = str(data.get("biography", ""))
    if exp_slug not in bio_text and "[[experience:" not in bio_text:
        templates = event_info["templates"]
        sentence_tpl = templates[template_idx % len(templates)]
        sentence = sentence_tpl.format(exp_link=event_info["exp_link"])
        content = append_to_biography(content, sentence)
        modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True, event_id

    return False, "Already populated"


def main():
    print("Populating memories and enriching character backgrounds...")
    total_files = 0
    updated_files = 0

    idx = 0
    for root, _, files in os.walk(CHAR_DIR):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            # Skip the-guide and the-traveler (already have turning wheel)
            if f in ["the-guide.md", "the-traveler.md"]:
                continue
            total_files += 1
            path = os.path.join(root, f)
            changed, msg = process_character_file(path, idx)
            if changed:
                updated_files += 1
                idx += 1

    print(f"Done. Processed {total_files} characters. Updated: {updated_files}")


if __name__ == "__main__":
    main()
