---
id: relationship:flor-and-temno
name: Herbalist and poison specialist
participants:
- character:flor
- character:temno
association: rivalry
public_status: Flor and Temno are both herbalists of the Verdania peoples, and locals
  consult each for different needs.
bond: Flor heals; Temno deals in poisons and antidotes. The professional boundary is clear, but the personal
  one is not — each suspects the other knows formulations they have not shared, and each has been quietly
  trying to learn the other's secrets for years without ever directly asking.
disposition: 34
summary: Flor heals; Temno deals in poisons and antidotes. The professional boundary is clear, but the
  personal one is not — each suspects the other knows formulations they have not shared, and each has
  been quietly trying to learn the other's secrets for years without ever directly asking.
current_stage: productive_rivalry
perspectives:
- subject: character:flor
  object: character:temno
  disposition: 32
  summary: Flor respects Temno's ability but experiences every success as a challenge that must be answered.
  visibility: subject
- subject: character:temno
  object: character:flor
  disposition: 34
  summary: Temno resents Flor's pressure while privately relying on the standard only a worthy rival can
    provide.
  visibility: subject
history:
- id: connection-established
  title: The rivalry found its terms
  summary: A public comparison of their work made private competition impossible to dismiss. Each recognized
    that only the other could provide a worthy measure.
  occurred_at: When their connection took shape
  visibility: public
  stage_after: forming_rivalry
  perspective_changes:
  - subject: character:flor
    object: character:temno
    after: 23
    summary_after: Flor respects Temno's ability but experiences every success as a challenge that must
      be answered.
    visibility: subject
  - subject: character:temno
    object: character:flor
    after: 24
    summary_after: Temno resents Flor's pressure while privately relying on the standard only a worthy
      rival can provide.
    visibility: subject
- id: present-balance
  title: Respect complicated the contest
  summary: Flor heals; Temno deals in poisons and antidotes. The professional boundary is clear, but the
    personal one is not — each suspects the other knows formulations they have not shared, and each has
    been quietly trying to learn the other's secrets for years without ever directly asking.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: productive_rivalry
  stage_before: forming_rivalry
  relationship_summary_after: Flor heals; Temno deals in poisons and antidotes. The professional boundary
    is clear, but the personal one is not — each suspects the other knows formulations they have not shared,
    and each has been quietly trying to learn the other's secrets for years without ever directly asking.
  perspective_changes:
  - subject: character:flor
    object: character:temno
    before: 23
    after: 32
    summary_after: Flor respects Temno's ability but experiences every success as a challenge that must
      be answered.
    visibility: subject
  - subject: character:temno
    object: character:flor
    before: 24
    after: 34
    summary_after: Temno resents Flor's pressure while privately relying on the standard only a worthy
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
