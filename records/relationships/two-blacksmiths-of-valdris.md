---
id: relationship:lyria-and-regor
name: Two blacksmiths of Valdris
participants:
- character:lyria-ironheart
- character:regor-blackhammer
association: rivalry
public_status: Lyria Ironheart and Regor Blackhammer are the two foremost smiths in the town, and their
  competition for commissions is well known.
bond: They were once apprenticed to the same master and loved each other as siblings before pride and
  a disputed inheritance of the forge divided them. Each secretly believes the other was the more talented
  and resents being forced to prove otherwise every single day.
disposition: 30
summary: They were once apprenticed to the same master and loved each other as siblings before pride and
  a disputed inheritance of the forge divided them. Each secretly believes the other was the more talented
  and resents being forced to prove otherwise every single day.
current_stage: productive_rivalry
perspectives:
- subject: character:lyria-ironheart
  object: character:regor-blackhammer
  disposition: 35
  summary: Lyria Ironheart respects Regor Blackhammer's ability but experiences every success as a challenge
    that must be answered.
  visibility: subject
- subject: character:regor-blackhammer
  object: character:lyria-ironheart
  disposition: 23
  summary: Regor Blackhammer resents Lyria Ironheart's pressure while privately relying on the standard
    only a worthy rival can provide.
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
  - subject: character:lyria-ironheart
    object: character:regor-blackhammer
    after: 25
    summary_after: Lyria Ironheart respects Regor Blackhammer's ability but experiences every success
      as a challenge that must be answered.
    visibility: subject
  - subject: character:regor-blackhammer
    object: character:lyria-ironheart
    after: 17
    summary_after: Regor Blackhammer resents Lyria Ironheart's pressure while privately relying on the
      standard only a worthy rival can provide.
    visibility: subject
- id: present-balance
  title: Respect complicated the contest
  summary: They were once apprenticed to the same master and loved each other as siblings before pride
    and a disputed inheritance of the forge divided them. Each secretly believes the other was the more
    talented and resents being forced to prove otherwise every single day.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: productive_rivalry
  stage_before: forming_rivalry
  relationship_summary_after: They were once apprenticed to the same master and loved each other as siblings
    before pride and a disputed inheritance of the forge divided them. Each secretly believes the other
    was the more talented and resents being forced to prove otherwise every single day.
  perspective_changes:
  - subject: character:lyria-ironheart
    object: character:regor-blackhammer
    before: 25
    after: 35
    summary_after: Lyria Ironheart respects Regor Blackhammer's ability but experiences every success
      as a challenge that must be answered.
    visibility: subject
  - subject: character:regor-blackhammer
    object: character:lyria-ironheart
    before: 17
    after: 23
    summary_after: Regor Blackhammer resents Lyria Ironheart's pressure while privately relying on the
      standard only a worthy rival can provide.
    visibility: subject
visual:
  prompt: ''
---
