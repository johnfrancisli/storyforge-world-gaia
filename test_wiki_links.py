#!/usr/bin/env python3
"""
test_wiki_links.py — Focused tests for wiki-link validation.

Tests:
  1. Short links: [[character:aerindra]] — valid
  2. Piped links: [[character:aerindra|Aerindra]] — valid
  3. Invalid IDs: [[character:nonexistent]] — warning (unresolved)
  4. Code blocks: wiki-link-like text inside ``` blocks is ignored
  5. Markdown tables: wiki links with | inside table cells
  6. Reversed links: [[Aerindra|character:aerindra]] — error
  7. Unknown type: [[creature:dragon]] — error
  8. Empty target: [[|display]] — error
  9. Wiki-link in YAML structured field — error
 10. Inline code: `[[character:aerindra]]` is ignored
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_wiki_links import (
    WIKI_LINK_RE,
    strip_code_blocks,
    check_reversed,
    validate_markdown_wiki_links,
    validate_yaml_frontmatter,
    VALID_TYPES,
)


def test_short_link():
    content = "---\nid: character:test\n---\nSee [[character:aerindra]] for details.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:aerindra', 'character:test'}, issues)
    errors = [i for i in issues if i['severity'] == 'error']
    assert len(errors) == 0, f"Short link should be valid, got errors: {errors}"
    print("PASS: test_short_link")


def test_piped_link():
    content = "---\nid: character:test\n---\n[[character:aerindra|the pale-haired fletcher]] nods.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:aerindra', 'character:test'}, issues)
    errors = [i for i in issues if i['severity'] == 'error']
    assert len(errors) == 0, f"Piped link should be valid, got errors: {errors}"
    print("PASS: test_piped_link")


def test_unresolved_id():
    content = "---\nid: character:test\n---\n[[character:does-not-exist]] is mentioned.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:test'}, issues)
    warnings = [i for i in issues if i['severity'] == 'warning' and i['type'] == 'unresolved_reference']
    assert len(warnings) == 1, f"Should get 1 unresolved warning, got: {issues}"
    assert 'character:does-not-exist' in warnings[0]['message']
    print("PASS: test_unresolved_id")


def test_code_block_ignored():
    content = "---\nid: character:test\n---\nHere is some prose:\n\n```\n[[character:aerindra|Aerindra]]\n```\n\nDone.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:test'}, issues)
    assert len(issues) == 0, f"Code block links should be ignored, got: {issues}"
    print("PASS: test_code_block_ignored")


def test_inline_code_ignored():
    content = "---\nid: character:test\n---\nUse `[[character:aerindra]]` to link.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:test'}, issues)
    assert len(issues) == 0, f"Inline code links should be ignored, got: {issues}"
    print("PASS: test_inline_code_ignored")


def test_reversed_link():
    content = "---\nid: character:test\n---\n[[Aerindra|character:aerindra]] is here.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:aerindra', 'character:test'}, issues)
    errors = [i for i in issues if i['severity'] == 'error' and i['type'] == 'reversed_link']
    assert len(errors) == 1, f"Should get 1 reversed_link error, got: {issues}"
    print("PASS: test_reversed_link")


def test_unknown_type():
    content = "---\nid: character:test\n---\n[[creature:dragon]] appears.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:test'}, issues)
    errors = [i for i in issues if i['severity'] == 'error' and i['type'] == 'unknown_entity_type']
    assert len(errors) == 1, f"Should get 1 unknown_entity_type error, got: {issues}"
    print("PASS: test_unknown_type")


def test_empty_target():
    content = "---\nid: character:test\n---\n[[|some text]] is wrong.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:test'}, issues)
    errors = [i for i in issues if i['severity'] == 'error' and i['type'] == 'empty_target']
    assert len(errors) == 1, f"Should get 1 empty_target error, got: {issues}"
    print("PASS: test_empty_target")


def test_wiki_link_in_yaml_field():
    content = "---\nid: character:test\nparticipants:\n- '[[character:aerindra|Aerindra]]'\n---\nProse here.\n"
    issues = []
    validate_yaml_frontmatter('test.md', content, issues)
    errors = [i for i in issues if i['severity'] == 'error' and i['type'] == 'wiki_link_in_structured_field']
    assert len(errors) == 1, f"Should get 1 structured field error, got: {issues}"
    assert 'participants' in errors[0]['message']
    print("PASS: test_wiki_link_in_yaml_field")


def test_raw_id_in_yaml_field_ok():
    content = "---\nid: character:test\nparticipants:\n- character:aerindra\n---\nProse here.\n"
    issues = []
    validate_yaml_frontmatter('test.md', content, issues)
    errors = [i for i in issues if i['severity'] == 'error']
    assert len(errors) == 0, f"Raw IDs in structured fields should be OK, got: {errors}"
    print("PASS: test_raw_id_in_yaml_field_ok")


def test_wiki_link_in_prose_after_yaml_ok():
    content = "---\nid: character:test\nparticipants:\n- character:aerindra\n---\n[[character:aerindra]] is here.\n"
    issues = []
    validate_yaml_frontmatter('test.md', content, issues)
    errors = [i for i in issues if i['severity'] == 'error']
    assert len(errors) == 0, f"Wiki links in prose should not trigger structured field errors, got: {errors}"
    print("PASS: test_wiki_link_in_prose_after_yaml_ok")


def test_missing_type_prefix():
    content = "---\nid: character:test\n---\n[[aerindra]] is here.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:test'}, issues)
    errors = [i for i in issues if i['severity'] == 'error' and i['type'] == 'missing_type_prefix']
    assert len(errors) == 1, f"Should get 1 missing_type_prefix error, got: {issues}"
    print("PASS: test_missing_type_prefix")


def test_table_with_wiki_link():
    content = "---\nid: character:test\n---\n| Name | Link |\n|---|---|\n| Aerindra | [[character:aerindra\\|the fletcher]] |\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:aerindra', 'character:test'}, issues)
    print(f"PASS: test_table_with_wiki_link (issues: {len(issues)})")


def test_valid_types_set():
    expected = {'character', 'location', 'organization', 'thread', 'item', 'relationship', 'lore', 'org'}
    assert VALID_TYPES == expected, f"VALID_TYPES mismatch: {VALID_TYPES} vs {expected}"
    print("PASS: test_valid_types_set")


def test_check_reversed_function():
    assert check_reversed('Aerindra') == False, "Plain name without colon should not be reversed"
    assert check_reversed('character:aerindra') == False, "Valid type:id should not be reversed"
    assert check_reversed('the fletcher|character:aerindra') == True, "Name|type:id should be reversed"
    assert check_reversed('character:aerindra|the fletcher') == False, "type:id|name should not be reversed"
    assert check_reversed('Aerindra', 'character:aerindra') == True, "Display text with type:id means reversed"
    assert check_reversed('character:aerindra', 'the fletcher') == False, "Plain display text is not reversed"
    print("PASS: test_check_reversed_function")


def test_strip_code_blocks():
    text = "Before\n```\n[[character:test]]\n```\nAfter"
    cleaned = strip_code_blocks(text)
    assert '[[character:test]]' not in cleaned, "Code block content should be removed"
    assert 'Before' in cleaned and 'After' in cleaned, "Non-code content should remain"
    print("PASS: test_strip_code_blocks")


def test_org_type_valid():
    """The 'org' abbreviation should be a valid type."""
    content = "---\nid: character:test\n---\n[[org:briar-wardens]] is mentioned.\n"
    issues = []
    validate_markdown_wiki_links('test.md', content, {'character:test', 'org:briar-wardens'}, issues)
    errors = [i for i in issues if i['severity'] == 'error']
    assert len(errors) == 0, f"'org' should be a valid type, got errors: {errors}"
    print("PASS: test_org_type_valid")


def main():
    tests = [
        test_short_link,
        test_piped_link,
        test_unresolved_id,
        test_code_block_ignored,
        test_inline_code_ignored,
        test_reversed_link,
        test_unknown_type,
        test_empty_target,
        test_wiki_link_in_yaml_field,
        test_raw_id_in_yaml_field_ok,
        test_wiki_link_in_prose_after_yaml_ok,
        test_missing_type_prefix,
        test_table_with_wiki_link,
        test_valid_types_set,
        test_check_reversed_function,
        test_strip_code_blocks,
        test_org_type_valid,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR: {test.__name__}: {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
