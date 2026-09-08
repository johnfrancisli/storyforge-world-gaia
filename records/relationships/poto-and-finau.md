---
id: relationship:poto-and-finau
name: Poto and Finau
participants:
- character:poto
- character:finau
association: father and daughter
public_status: Poto is Finau's father and taught her the rope maker's holding knot.
bond: Poto passed the holding knot to Finau but withheld its dangerous counterpart, the untying knot.
is_familial: true
kinship:
- subject: character:poto
  relation: parent_of
  object: character:finau
  visibility: public
summary: Poto passed the holding knot to Finau but withheld its dangerous counterpart, the untying knot.
current_stage: complicated_family_bond
perspectives:
- subject: character:poto
  object: character:finau
  disposition: 58
  summary: Poto loves Finau fiercely, though protection, pride, and duty make that affection difficult
    to express cleanly.
  visibility: subject
- subject: character:finau
  object: character:poto
  disposition: 68
  summary: Finau remains attached to Poto, even where withheld truths and inherited expectations have
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
  - subject: character:poto
    object: character:finau
    after: 42
    summary_after: Poto loves Finau fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:finau
    object: character:poto
    after: 49
    summary_after: Finau remains attached to Poto, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: Poto passed the holding knot to Finau but withheld its dangerous counterpart, the untying knot.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: Poto passed the holding knot to Finau but withheld its dangerous counterpart,
    the untying knot.
  perspective_changes:
  - subject: character:poto
    object: character:finau
    before: 42
    after: 58
    summary_after: Poto loves Finau fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:finau
    object: character:poto
    before: 49
    after: 68
    summary_after: Finau remains attached to Poto, even where withheld truths and inherited expectations
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
