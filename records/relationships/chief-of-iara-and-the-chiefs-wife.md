---
id: relationship:oron-and-sol
name: Chief of Iara and the chief's wife
participants:
- character:oron
- character:sol
association: family
public_status: Chief Oron and Sol are husband and wife and jointly lead the Iara community,
  she as elder council member, he as chief.
bond: 'Their partnership is the marriage of two complementary powers — his is the voice that speaks for
  the people in war, hers is the memory that speaks for them in council. They disagree often and loudly,
  to the alarm of outsiders, but it is the disagreement of two people who have already agreed on the one
  thing that matters: the people come first.'
disposition: 79
is_familial: true
kinship:
- subject: character:oron
  relation: spouse_of
  object: character:sol
  visibility: public
summary: 'Their partnership is the marriage of two complementary powers — his is the voice that speaks
  for the people in war, hers is the memory that speaks for them in council. They disagree often and loudly,
  to the alarm of outsiders, but it is the disagreement of two people who have already agreed on the one
  thing that matters: the people come first.'
current_stage: complicated_family_bond
perspectives:
- subject: character:oron
  object: character:sol
  disposition: 80
  summary: Oron loves Sol fiercely, though protection, pride, and duty make that affection difficult to
    express cleanly.
  visibility: subject
- subject: character:sol
  object: character:oron
  disposition: 76
  summary: Sol remains attached to Oron, even where withheld truths and inherited expectations have made
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
  - subject: character:oron
    object: character:sol
    after: 58
    summary_after: Oron loves Sol fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:sol
    object: character:oron
    after: 55
    summary_after: Sol remains attached to Oron, even where withheld truths and inherited expectations
      have made closeness painful.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: 'Their partnership is the marriage of two complementary powers — his is the voice that speaks
    for the people in war, hers is the memory that speaks for them in council. They disagree often and
    loudly, to the alarm of outsiders, but it is the disagreement of two people who have already agreed
    on the one thing that matters: the people come first.'
  occurred_at: During the present chapter
  visibility: participants
  stage_after: complicated_family_bond
  stage_before: forming_family
  relationship_summary_after: 'Their partnership is the marriage of two complementary powers — his is
    the voice that speaks for the people in war, hers is the memory that speaks for them in council. They
    disagree often and loudly, to the alarm of outsiders, but it is the disagreement of two people who
    have already agreed on the one thing that matters: the people come first.'
  perspective_changes:
  - subject: character:oron
    object: character:sol
    before: 58
    after: 80
    summary_after: Oron loves Sol fiercely, though protection, pride, and duty make that affection difficult
      to express cleanly.
    visibility: subject
  - subject: character:sol
    object: character:oron
    before: 55
    after: 76
    summary_after: Sol remains attached to Oron, even where withheld truths and inherited expectations
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
