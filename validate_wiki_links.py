#!/usr/bin/env python3
"""
validate_wiki_links.py — Validate wiki-link entity references in Storyforge Markdown.

Scans all Markdown files under the project (excluding fenced code blocks and
inline code) for wiki-style links of the form:

    [[type:stable-id]]
    [[type:stable-id|display text]]

Reports:
  - Unknown entity types
  - Malformed wiki links (missing brackets, empty targets)
  - References to nonexistent IDs
  - Reversed links that appear to use [[display name|type:id]]
  - Wiki-link markup inside structured YAML/JSON fields that require raw IDs

Usage:
    python3 validate_wiki_links.py [--dir <project-root>]
"""
import os
import re
import sys
import json
import yaml
import argparse
from pathlib import Path

VALID_TYPES = {
    'character', 'location', 'organization', 'thread',
    'item', 'relationship', 'lore',
    'org',  # abbreviation used in existing records
    'experience', 'campaign-event', 'event',
}

# Fields in record YAML frontmatter that expect raw IDs, not wiki-link markup.
RAW_ID_FIELDS = {
    'participants', 'locations', 'organizations',
    'affiliations', 'current_state', 'home',
    'parent_location_id', 'seat', 'holdings',
    'purview', 'current_quest', 'current_location',
    'memories', 'momentos',
    'related_characters', 'related_locations',
    'related_organizations', 'related_factions',
    'related_threads', 'related_lore',
}

# Wiki-link pattern: [[type:id]] or [[type:id|display text]]
WIKI_LINK_RE = re.compile(
    r'\[\['
    r'([^\]]*?)'           # target (before optional |) — allow empty
    r'(?:\|([^\]]*))?'     # optional display text (after |)
    r'\]\]'
)


def strip_code_blocks(text):
    """Remove fenced code blocks and inline code from text, replacing with spaces."""
    text = re.sub(r'```[s]*\n.*?```', lambda m: ' ' * len(m.group(0)), text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', lambda m: ' ' * len(m.group(0)), text)
    return text


def extract_all_ids(project_dir):
    """Collect all valid record IDs from the records/ directory."""
    valid_ids = set()
    records_dir = os.path.join(project_dir, 'records')
    if not os.path.isdir(records_dir):
        return valid_ids

    for root, dirs, files in os.walk(records_dir):
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='replace') as fh:
                    content = fh.read()
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        data = yaml.safe_load(parts[1])
                        if data and isinstance(data, dict):
                            rec_id = data.get('id')
                            if rec_id and isinstance(rec_id, str):
                                valid_ids.add(rec_id)
                                if rec_id.startswith('experience:'):
                                    slug = rec_id[11:]
                                    valid_ids.add(f'campaign-event/{slug}')
                                    valid_ids.add(f'campaign-event:{slug}')
                                elif rec_id.startswith('campaign-event/'):
                                    slug = rec_id[15:]
                                    valid_ids.add(f'experience:{slug}')
            except Exception:
                pass

    # Also collect IDs from world.json entries
    world_json = os.path.join(project_dir, 'world.json')
    if os.path.isfile(world_json):
        try:
            with open(world_json, 'r', encoding='utf-8', errors='replace') as fh:
                world = json.load(fh)
            for key in ['locations', 'organizations', 'characters', 'threads', 'items', 'relationships', 'lore']:
                block = world.get(key, {})
                if isinstance(block, dict):
                    entries = block.get('entries', [])
                    if isinstance(entries, list):
                        for entry in entries:
                            if isinstance(entry, dict) and entry.get('id'):
                                valid_ids.add(entry['id'])
        except Exception:
            pass

    return valid_ids


def check_reversed(target, display_text=None):
    """Check if a link appears reversed (display name in target, type:id in display).

    A reversed link looks like [[display name|type:id]] where the display text
    contains a valid type:id pattern.
    """
    if display_text:
        dt = display_text.strip()
        if ':' in dt and dt.split(':')[0].strip() in VALID_TYPES:
            return True
    if '|' in target:
        left, right = target.split('|', 1)
        right = right.strip()
        if ':' in right and right.split(':')[0].strip() in VALID_TYPES:
            return True
    return False


def validate_yaml_frontmatter(filepath, content, issues):
    """Check that wiki-link markup doesn't appear in raw-ID fields."""
    if not content.startswith('---'):
        return

    parts = content.split('---', 2)
    if len(parts) < 3:
        return

    yaml_text = parts[1]

    for match in WIKI_LINK_RE.finditer(yaml_text):
        target = match.group(1).strip()

        pos = match.start()
        before = yaml_text[:pos]
        field_match = None
        for line_match in re.finditer(r'^(\w+):', before, re.MULTILINE):
            field_match = line_match
        field_name = field_match.group(1) if field_match else 'unknown'

        if field_name in RAW_ID_FIELDS:
            issues.append({
                'file': filepath,
                'type': 'wiki_link_in_structured_field',
                'severity': 'error',
                'message': f'Wiki-link markup found in structured field "{field_name}" which expects raw IDs',
                'match': match.group(0),
                'suggestion': f'Use a raw ID like "character:aerindra" instead of "{match.group(0)}"',
            })


def validate_markdown_wiki_links(filepath, content, valid_ids, issues):
    """Find and validate wiki links in Markdown prose (excluding code blocks)."""
    prose = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            prose = parts[2]

    clean_prose = strip_code_blocks(prose)

    for match in WIKI_LINK_RE.finditer(clean_prose):
        raw_target = match.group(1)
        display_text = match.group(2)
        target = raw_target.strip()

        if not target or (display_text is None and not target):
            issues.append({
                'file': filepath,
                'type': 'empty_target',
                'severity': 'error',
                'message': 'Wiki link has an empty target',
                'match': match.group(0),
                'suggestion': 'Provide a valid type:id target',
            })
            continue

        if target.startswith('|'):
            issues.append({
                'file': filepath,
                'type': 'empty_target',
                'severity': 'error',
                'message': 'Wiki link has an empty target',
                'match': match.group(0),
                'suggestion': 'Provide a valid type:id target before the pipe',
            })
            continue

        if check_reversed(target, display_text):
            issues.append({
                'file': filepath,
                'type': 'reversed_link',
                'severity': 'error',
                'message': f'Wiki link appears reversed (display name before type:id): "{target}"',
                'match': match.group(0),
                'suggestion': 'Use [[type:id|display text]] — target first, display text second',
            })
            continue

        if ':' not in target:
            issues.append({
                'file': filepath,
                'type': 'missing_type_prefix',
                'severity': 'error',
                'message': f'Wiki link target "{target}" has no type prefix (expected type:id)',
                'match': match.group(0),
                'suggestion': f'Use a type prefix like character:{target}',
            })
            continue

        type_prefix = target.split(':')[0].strip()
        entity_id = target.split(':', 1)[1].strip()

        if type_prefix not in VALID_TYPES:
            issues.append({
                'file': filepath,
                'type': 'unknown_entity_type',
                'severity': 'error',
                'message': f'Unknown entity type "{type_prefix}" in wiki link',
                'match': match.group(0),
                'suggestion': f'Valid types: {", ".join(sorted(VALID_TYPES))}',
            })
            continue

        if not entity_id:
            issues.append({
                'file': filepath,
                'type': 'empty_id',
                'severity': 'error',
                'message': f'Wiki link has type "{type_prefix}" but no ID',
                'match': match.group(0),
                'suggestion': f'Provide an ID like [[{type_prefix}:some-id]]',
            })
            continue

        full_id = f'{type_prefix}:{entity_id}'
        if valid_ids and full_id not in valid_ids:
            issues.append({
                'file': filepath,
                'type': 'unresolved_reference',
                'severity': 'warning',
                'message': f'Reference to nonexistent ID "{full_id}"',
                'match': match.group(0),
                'suggestion': f'Create a record with id "{full_id}" or remove the link',
            })


def validate_file(filepath, valid_ids, issues):
    """Validate a single Markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
    except Exception as e:
        issues.append({
            'file': filepath,
            'type': 'read_error',
            'severity': 'error',
            'message': f'Could not read file: {e}',
            'match': '',
            'suggestion': '',
        })
        return

    validate_yaml_frontmatter(filepath, content, issues)
    validate_markdown_wiki_links(filepath, content, valid_ids, issues)


def main():
    parser = argparse.ArgumentParser(description='Validate wiki-link entity references')
    parser.add_argument('--dir', default='.', help='Project root directory')
    args = parser.parse_args()

    project_dir = os.path.abspath(args.dir)
    valid_ids = extract_all_ids(project_dir)

    issues = []
    md_files = []
    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    for filepath in sorted(md_files):
        validate_file(filepath, valid_ids, issues)

    errors = [i for i in issues if i['severity'] == 'error']
    warnings = [i for i in issues if i['severity'] == 'warning']

    if not issues:
        print(f'OK — {len(md_files)} files scanned, no wiki-link issues found.')
        sys.exit(0)

    if errors:
        print(f'ERRORS ({len(errors)}):')
        for i in errors:
            rel = os.path.relpath(i['file'], project_dir)
            print(f'  {rel}: {i["message"]}')
            if i['match']:
                print(f'    link: {i["match"]}')
            if i['suggestion']:
                print(f'    fix:  {i["suggestion"]}')
        print()

    if warnings:
        print(f'WARNINGS ({len(warnings)}):')
        for i in warnings:
            rel = os.path.relpath(i['file'], project_dir)
            print(f'  {rel}: {i["message"]}')
            if i['match']:
                print(f'    link: {i["match"]}')
            if i['suggestion']:
                print(f'    fix:  {i["suggestion"]}')
        print()

    print(f'Total: {len(errors)} error(s), {len(warnings)} warning(s) across {len(md_files)} files.')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
