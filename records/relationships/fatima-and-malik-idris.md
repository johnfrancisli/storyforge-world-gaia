---
id: relationship:fatima-and-malik-idris
name: Fatima and Malik Idris
participants:
- character:fatima-idris
- character:malik-idris
association: younger sister and elder brother
public_status: Fatima is Malik Idris's younger sister and the family's second child.
bond: Fatima loves Malik but intends to use the research he hid to force reform within their binding family.
is_familial: true
kinship:
- subject: character:fatima-idris
  relation: sibling_of
  object: character:malik-idris
  visibility: public
summary: Fatima loves her elder brother, but secretly intends to use the research he hid to force reform
  inside their family.
current_stage: loving_siblings_with_hidden_leverage
perspectives:
- subject: character:fatima-idris
  object: character:malik-idris
  disposition: 55
  summary: She loves Malik and wants to help him, while also treating his crisis as leverage for reform.
  visibility: subject
history:
- id: raised-as-idris-siblings
  title: They grew up as Idris siblings
  summary: Malik became the firstborn heir while Fatima grew up outside the contract's direct claim.
  visibility: public
  stage_after: siblings
  perspective_changes: []
- id: found-maliks-research
  title: Fatima found Malik's hidden research
  summary: She discovered his failed attempts to escape the Idris contract and decided the evidence could
    force their family to confront the system.
  occurred_at: Three days before the current campaign
  visibility: gm_only
  stage_before: siblings
  stage_after: loving_siblings_with_hidden_leverage
  perspective_changes:
  - subject: character:fatima-idris
    object: character:malik-idris
    before: 70
    after: 55
    summary_after: Love remains, but she now sees his desperation as political leverage.
visual:
  prompt: ''
image:
  url: ''
  focalPoint:
    x: 0.5
    y: 0.1
  seed: null
---
