---
id: relationship:fatima-idris-and-reem
name: Idris reformer daughter and al-Faris scholar heiress
participants:
- character:fatima-idris
- character:reem-al-faris
association: friendship
public_status: The Idris daughter and the al-Faris heiress are both educated women of the binding families
  and are known to correspond on scholarly matters.
bond: They are friends across a family rivalry, bound by a shared frustration with the limits their houses
  place on women. Each is the other's only peer who understands what it is to be brilliant and contained.
  They have begun to wonder, privately, whether their friendship could become an alliance their families
  would forbid.
disposition: 74
summary: Fatima and Reem are scholarly friends across rival houses and are privately considering whether
  their trust can become a forbidden political alliance.
current_stage: confidantes_considering_alliance
perspectives:
- subject: character:fatima-idris
  object: character:reem-al-faris
  disposition: 82
  summary: She considers Reem the only peer who understands both her intelligence and the constraints of
    a binding-family daughter.
  visibility: subject
- subject: character:reem-al-faris
  object: character:fatima-idris
  disposition: 78
  summary: She trusts Fatima as a rare intellectual equal, while remaining cautious about what an alliance
    between their houses could expose.
  visibility: subject
history:
- id: scholarly-correspondence
  title: They began corresponding
  summary: The two binding-family scholars established a public correspondence on academic matters.
  visibility: public
  stage_after: scholarly_correspondents
  perspective_changes: []
- id: became-confidantes
  title: Correspondence became friendship
  summary: Shared frustration with the limits imposed by their houses made each woman the other's closest
    intellectual peer.
  visibility: participants
  stage_before: scholarly_correspondents
  stage_after: confidantes
  perspective_changes:
  - subject: character:fatima-idris
    object: character:reem-al-faris
    after: 82
    summary_after: She considers Reem the only peer who fully understands her position.
  - subject: character:reem-al-faris
    object: character:fatima-idris
    after: 78
    summary_after: She trusts Fatima as a rare intellectual equal.
- id: considered-house-alliance
  title: They considered an alliance
  summary: Their private conversations turned toward an alliance their rival families might forbid.
  visibility: participants
  stage_before: confidantes
  stage_after: confidantes_considering_alliance
  perspective_changes: []
visual:
  prompt: ''
image:
  url: ''
  focalPoint:
    x: 0.5
    y: 0.1
  seed: null
---
