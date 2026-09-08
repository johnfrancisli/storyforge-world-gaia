---
id: relationship:yara-and-sol
name: Yara and Sol
participants:
- character:yara
- character:sol
association: mother and daughter
public_status: Sol is Yara's daughter and an elder of Iara's council.
bond: Yara's spiritual authority and Sol's civic influence place mother and daughter at the center of Iara's choices about survival and change.
is_familial: true
kinship:
- subject: character:yara
  relation: parent_of
  object: character:sol
  visibility: public
summary: Yara's spiritual authority and Sol's civic influence place mother and daughter at the center
  of Iara's choices about survival and change.
current_stage: complicated_family_bond
perspectives:
- subject: character:yara
  object: character:sol
  disposition: 67
  summary: Yara loves Sol fiercely, though protection, pride, and duty make that affection difficult to
    express cleanly.
  visibility: subject
- subject: character:sol
  object: character:yara
  disposition: 58
  summary: Sol remains attached to Yara, even where withheld truths and inherited expectations have made
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
  - subject: character:yara
    object: character:sol
    after: 48
    summary_after: Yara loves Sol fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:sol
    object: character:yara
    after: 42
    summary_after: Sol remains attached to Yara, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: Yara's spiritual authority and Sol's civic influence place mother and daughter at the center
    of Iara's choices about survival and change.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: Yara's spiritual authority and Sol's civic influence place mother and daughter
    at the center of Iara's choices about survival and change.
  perspective_changes:
  - subject: character:yara
    object: character:sol
    before: 48
    after: 67
    summary_after: Yara loves Sol fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:sol
    object: character:yara
    before: 42
    after: 58
    summary_after: Sol remains attached to Yara, even where withheld truths and inherited expectations
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
