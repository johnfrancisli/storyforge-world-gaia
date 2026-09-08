---
id: relationship:argila-and-pedra
name: Argila and Pedra
participants:
- character:argila
- character:pedra
association: sister and younger brother
public_status: Argila and her younger brother Pedra work as potters and kiln keepers in Iara.
bond: They work alongside one another, but Pedra's suspicion that Argila is hiding something has begun to strain their trust.
is_familial: true
kinship:
- subject: character:argila
  relation: sibling_of
  object: character:pedra
  visibility: public
summary: They work alongside one another, but Pedra's suspicion that Argila is hiding something has begun
  to strain their trust.
current_stage: complicated_family_bond
perspectives:
- subject: character:argila
  object: character:pedra
  disposition: 69
  summary: Argila loves Pedra fiercely, though protection, pride, and duty make that affection difficult
    to express cleanly.
  visibility: subject
- subject: character:pedra
  object: character:argila
  disposition: 57
  summary: Pedra remains attached to Argila, even where withheld truths and inherited expectations have
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
  - subject: character:argila
    object: character:pedra
    after: 50
    summary_after: Argila loves Pedra fiercely, though protection, pride, and duty make that affection
      difficult to express cleanly.
    visibility: subject
  - subject: character:pedra
    object: character:argila
    after: 41
    summary_after: Pedra remains attached to Argila, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: They work alongside one another, but Pedra's suspicion that Argila is hiding something has
    begun to strain their trust.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: They work alongside one another, but Pedra's suspicion that Argila is hiding
    something has begun to strain their trust.
  perspective_changes:
  - subject: character:argila
    object: character:pedra
    before: 50
    after: 69
    summary_after: Argila loves Pedra fiercely, though protection, pride, and duty make that affection
      difficult to express cleanly.
    visibility: subject
  - subject: character:pedra
    object: character:argila
    before: 41
    after: 57
    summary_after: Pedra remains attached to Argila, even where withheld truths and inherited expectations
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
