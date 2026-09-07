---
id: relationship:aldran-and-elara
name: King Aldran and Princess Elara
participants:
- character:aldran-valdris-iii
- character:elara-valdris
association: father and daughter
public_status: Elara is one of King Aldran's two eldest children and a claimant to the succession.
bond: Aldran's failing health has made Elara's inheritance urgent, while her reformist ambitions place her at odds with the order he has maintained.
is_familial: true
kinship:
- subject: character:aldran-valdris-iii
  relation: parent_of
  object: character:elara-valdris
  visibility: public
summary: Aldran's failing health has made Elara's inheritance urgent, while her reformist ambitions place
  her at odds with the order he has maintained.
current_stage: complicated_family_bond
perspectives:
- subject: character:aldran-valdris-iii
  object: character:elara-valdris
  disposition: 59
  summary: Aldran Valdris III loves Elara Valdris fiercely, though protection, pride, and duty make that
    affection difficult to express cleanly.
  visibility: subject
- subject: character:elara-valdris
  object: character:aldran-valdris-iii
  disposition: 67
  summary: Elara Valdris remains attached to Aldran Valdris III, even where withheld truths and inherited
    expectations have made closeness painful.
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
  - subject: character:aldran-valdris-iii
    object: character:elara-valdris
    after: 42
    summary_after: Aldran Valdris III loves Elara Valdris fiercely, though protection, pride, and duty
      make that affection difficult to express cleanly.
    visibility: subject
  - subject: character:elara-valdris
    object: character:aldran-valdris-iii
    after: 48
    summary_after: Elara Valdris remains attached to Aldran Valdris III, even where withheld truths and
      inherited expectations have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: Aldran's failing health has made Elara's inheritance urgent, while her reformist ambitions
    place her at odds with the order he has maintained.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: Aldran's failing health has made Elara's inheritance urgent, while her reformist
    ambitions place her at odds with the order he has maintained.
  perspective_changes:
  - subject: character:aldran-valdris-iii
    object: character:elara-valdris
    before: 42
    after: 59
    summary_after: Aldran Valdris III loves Elara Valdris fiercely, though protection, pride, and duty
      make that affection difficult to express cleanly.
    visibility: subject
  - subject: character:elara-valdris
    object: character:aldran-valdris-iii
    before: 48
    after: 67
    summary_after: Elara Valdris remains attached to Aldran Valdris III, even where withheld truths and
      inherited expectations have made closeness painful.
    visibility: subject
visual:
  prompt: ''
---
