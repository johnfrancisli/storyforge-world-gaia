---
id: relationship:elara-and-roderick
name: Princess Elara and Prince Roderick
participants:
- character:elara-valdris
- character:roderick-valdris
association: siblings, political rivals
public_status: The king's two eldest children, publicly civil, privately competing for the succession.
  The court watches them and bets quietly.
bond: Elara underestimates Roderick's cunning — she thinks he is a blunt soldier, but he has been feeding
  her false intelligence through a double agent. Roderick does not know about Elara's dragonbone research,
  which is the one card she has that he cannot counter. They are siblings and they are enemies, and neither
  of them has decided which matters more.
disposition: -20
is_familial: true
kinship:
- subject: character:elara-valdris
  relation: sibling_of
  object: character:roderick-valdris
  visibility: public
summary: Elara and Roderick weaponize the intimacy of siblings in a succession struggle, each remembering
  exactly which childhood trust makes the other's present betrayal hurt most.
current_stage: succession_cold_war
perspectives:
- subject: character:elara-valdris
  object: character:roderick-valdris
  disposition: -18
  summary: Elara Valdris loves Roderick Valdris fiercely, though protection, pride, and duty make that
    affection difficult to express cleanly.
  visibility: subject
- subject: character:roderick-valdris
  object: character:elara-valdris
  disposition: -34
  summary: Roderick Valdris remains attached to Elara Valdris, even where withheld truths and inherited
    expectations have made closeness painful.
  visibility: subject
history:
- id: childhood-oath
  title: They once swore never to divide the kingdom
  summary: As children they cut their palms on the same practice blade and promised that crown and kingdom
    would never make them enemies. Both still keep the scar hidden beneath a glove.
  occurred_at: When their connection took shape
  visibility: participants
  stage_after: forming_family
  perspective_changes:
  - subject: character:elara-valdris
    object: character:roderick-valdris
    after: -13
    summary_after: Elara Valdris loves Roderick Valdris fiercely, though protection, pride, and duty make
      that affection difficult to express cleanly.
    visibility: subject
  - subject: character:roderick-valdris
    object: character:elara-valdris
    after: -24
    summary_after: Roderick Valdris remains attached to Elara Valdris, even where withheld truths and
      inherited expectations have made closeness painful.
    visibility: subject
- id: false-intelligence
  title: Roderick poisoned Elara's intelligence
  summary: Roderick placed a double agent near his sister and fed her reports designed to waste her political
    capital. Elara has not found the source, but her dragonbone research is becoming a counterweight he
    cannot see.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: succession_cold_war
  stage_before: forming_family
  relationship_summary_after: Elara and Roderick weaponize the intimacy of siblings in a succession struggle,
    each remembering exactly which childhood trust makes the other's present betrayal hurt most.
  perspective_changes:
  - subject: character:elara-valdris
    object: character:roderick-valdris
    before: -13
    after: -18
    summary_after: Elara Valdris loves Roderick Valdris fiercely, though protection, pride, and duty make
      that affection difficult to express cleanly.
    visibility: subject
  - subject: character:roderick-valdris
    object: character:elara-valdris
    before: -24
    after: -34
    summary_after: Roderick Valdris remains attached to Elara Valdris, even where withheld truths and
      inherited expectations have made closeness painful.
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
