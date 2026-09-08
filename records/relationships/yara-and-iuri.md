---
id: relationship:yara-and-iuri
name: Yara and Iuri
participants:
- character:yara
- character:iuri
association: grandmother and granddaughter
public_status: Iuri is Yara's granddaughter and heir-apprentice in the Teluna shamanic lineage.
bond: Yara is preparing Iuri to inherit the Moonflower Pact while each has reached a different, dangerous understanding of the spirit bound within it.
is_familial: true
kinship:
- subject: character:yara
  relation: grandparent_of
  object: character:iuri
  visibility: public
summary: Yara is preparing Iuri to inherit the Moonflower Pact while each has reached a different, dangerous
  understanding of the spirit bound within it.
current_stage: complicated_family_bond
perspectives:
- subject: character:yara
  object: character:iuri
  disposition: 61
  summary: Yara loves Iuri fiercely, though protection, pride, and duty make that affection difficult
    to express cleanly.
  visibility: subject
- subject: character:iuri
  object: character:yara
  disposition: 49
  summary: Iuri remains attached to Yara, even where withheld truths and inherited expectations have made
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
    object: character:iuri
    after: 44
    summary_after: Yara loves Iuri fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:iuri
    object: character:yara
    after: 35
    summary_after: Iuri remains attached to Yara, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: Yara is preparing Iuri to inherit the Moonflower Pact while each has reached a different, dangerous
    understanding of the spirit bound within it.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: Yara is preparing Iuri to inherit the Moonflower Pact while each has reached
    a different, dangerous understanding of the spirit bound within it.
  perspective_changes:
  - subject: character:yara
    object: character:iuri
    before: 44
    after: 61
    summary_after: Yara loves Iuri fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:iuri
    object: character:yara
    before: 35
    after: 49
    summary_after: Iuri remains attached to Yara, even where withheld truths and inherited expectations
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
