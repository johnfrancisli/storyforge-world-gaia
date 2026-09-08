---
id: relationship:tamamo-and-katsura
name: Wild kitsune and shrine kitsune
participants:
- character:tamamo
- character:katsura
association: kinspirits and ancient rivals
public_status: The two fox spirits are occasionally seen near the shrine grounds together, though most
  folk cannot tell them apart and assume them the same creature.
bond: Katsura is Tamamo's younger kinspirit, bound to the shrine by pact where Tamamo refused all such
  ties. They argue in the fox-tongue about freedom and duty — Katsura believing Tamamo foolish for spurning
  the shrine's protection, Tamamo believing Katsure has traded her wild soul for safety. They love each
  other fiercely and neither will admit it.
disposition: 60
is_familial: false
summary: Tamamo and Katsura quarrel over freedom and duty with the theatrical spite of kinspirits who
  know every weakness and would still burn a province to rescue one another.
current_stage: ancient_rivalry_with_fierce_affection
perspectives:
- subject: character:tamamo
  object: character:katsura
  disposition: 62
  summary: Tamamo respects Katsura's ability but experiences every success as a challenge that must be
    answered.
  visibility: subject
- subject: character:katsura
  object: character:tamamo
  disposition: 74
  summary: Katsura resents Tamamo's pressure while privately relying on the standard only a worthy rival
    can provide.
  visibility: subject
history:
- id: pact-divided-them
  title: One accepted the shrine pact
  summary: Katsura accepted shrine protection where Tamamo refused it. Their argument lasted seven nights,
    changed three farmers' hair white, and settled absolutely nothing.
  occurred_at: When their connection took shape
  visibility: participants
  stage_after: forming_rivalry
  perspective_changes:
  - subject: character:tamamo
    object: character:katsura
    after: 45
    summary_after: Tamamo respects Katsura's ability but experiences every success as a challenge that
      must be answered.
    visibility: subject
  - subject: character:katsura
    object: character:tamamo
    after: 53
    summary_after: Katsura resents Tamamo's pressure while privately relying on the standard only a worthy
      rival can provide.
    visibility: subject
- id: same-fox-trick
  title: Mortals mistook them for one fox
  summary: When villagers blamed Katsura for Tamamo's theft, the sisters produced impossible sightings
    on opposite hills. They cleared Katsura's name and then fought over who performed the better tail
    flourish.
  occurred_at: During the present chapter
  visibility: public
  stage_after: ancient_rivalry_with_fierce_affection
  stage_before: forming_rivalry
  relationship_summary_after: Tamamo and Katsura quarrel over freedom and duty with the theatrical spite
    of kinspirits who know every weakness and would still burn a province to rescue one another.
  perspective_changes:
  - subject: character:tamamo
    object: character:katsura
    before: 45
    after: 62
    summary_after: Tamamo respects Katsura's ability but experiences every success as a challenge that
      must be answered.
    visibility: subject
  - subject: character:katsura
    object: character:tamamo
    before: 53
    after: 74
    summary_after: Katsura resents Tamamo's pressure while privately relying on the standard only a worthy
      rival can provide.
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
