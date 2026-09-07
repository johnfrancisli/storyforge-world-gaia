---
id: relationship:amara-and-kaa
name: Amara and Kaa
participants:
- character:amara
- character:kaa
association: cousins
public_status: The river trader Amara and hunter Kaa are cousins.
bond: Amara has been trying to make Kaa stop drinking and tell her what he found in the rainforest.
is_familial: true
kinship:
- subject: character:amara
  relation: cousin_of
  object: character:kaa
  visibility: public
summary: Amara has been trying to make Kaa stop drinking and tell her what he found in the rainforest.
current_stage: complicated_family_bond
perspectives:
- subject: character:amara
  object: character:kaa
  disposition: 61
  summary: Amara loves Kaa fiercely, though protection, pride, and duty make that affection difficult
    to express cleanly.
  visibility: subject
- subject: character:kaa
  object: character:amara
  disposition: 65
  summary: Kaa remains attached to Amara, even where withheld truths and inherited expectations have made
    closeness painful.
  visibility: subject
history:
- id: connection-established
  title: Duty reshaped the family bond
  summary: A moment of family duty forced private affection into a public role. Love remained, but it
    acquired expectations neither party could ignore.
  occurred_at: When their connection took shape
  visibility: public
  stage_after: forming_family
  perspective_changes:
  - subject: character:amara
    object: character:kaa
    after: 44
    summary_after: Amara loves Kaa fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:kaa
    object: character:amara
    after: 47
    summary_after: Kaa remains attached to Amara, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: Amara has been trying to make Kaa stop drinking and tell her what he found in the rainforest.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: Amara has been trying to make Kaa stop drinking and tell her what he found
    in the rainforest.
  perspective_changes:
  - subject: character:amara
    object: character:kaa
    before: 44
    after: 61
    summary_after: Amara loves Kaa fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:kaa
    object: character:amara
    before: 47
    after: 65
    summary_after: Kaa remains attached to Amara, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
visual:
  prompt: ''
---
