---
id: relationship:soji-and-suzume
name: Soji and Suzume
participants:
- character:soji
- character:suzume
association: brother and younger sister
public_status: Suzume is Soji's younger sister and followed him out of the tengu mountain dojo.
bond: They share exile and a determination to save the shrine network, but Soji seeks outside help while Suzume secretly negotiates a path back to the elders.
is_familial: true
kinship:
- subject: character:soji
  relation: sibling_of
  object: character:suzume
  visibility: public
summary: They share exile and a determination to save the shrine network, but Soji seeks outside help
  while Suzume secretly negotiates a path back to the elders.
current_stage: complicated_family_bond
perspectives:
- subject: character:soji
  object: character:suzume
  disposition: 65
  summary: Soji loves Suzume fiercely, though protection, pride, and duty make that affection difficult
    to express cleanly.
  visibility: subject
- subject: character:suzume
  object: character:soji
  disposition: 61
  summary: Suzume remains attached to Soji, even where withheld truths and inherited expectations have
    made closeness painful.
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
  - subject: character:soji
    object: character:suzume
    after: 47
    summary_after: Soji loves Suzume fiercely, though protection, pride, and duty make that affection
      difficult to express cleanly.
    visibility: subject
  - subject: character:suzume
    object: character:soji
    after: 44
    summary_after: Suzume remains attached to Soji, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: They share exile and a determination to save the shrine network, but Soji seeks outside help
    while Suzume secretly negotiates a path back to the elders.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: They share exile and a determination to save the shrine network, but Soji
    seeks outside help while Suzume secretly negotiates a path back to the elders.
  perspective_changes:
  - subject: character:soji
    object: character:suzume
    before: 47
    after: 65
    summary_after: Soji loves Suzume fiercely, though protection, pride, and duty make that affection
      difficult to express cleanly.
    visibility: subject
  - subject: character:suzume
    object: character:soji
    before: 44
    after: 61
    summary_after: Suzume remains attached to Soji, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
visual:
  prompt: ''
image:
  url: ''
  focalPoint:
    x: 0.5
    y: 0.1
  seed: null
---
