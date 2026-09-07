---
id: relationship:sera-and-calla
name: Tavern keeper and innkeeper, competing hosts
participants:
- character:sera-thornwick
- character:calla-riversong
association: friendship
public_status: The tavern keeper and the innkeeper are neighboring establishments and apparent competitors
  for travelers' coin.
bond: The competition is a long-running performance they both maintain to keep prices credible. In truth
  they share staff, split bulk supplies, and send overflow custom to each other. Their partnership is
  the reason the riverfront district hasn't been bought out by outside interests — and neither wants that
  known.
disposition: 76
summary: Sera and Calla perform a loud commercial feud while secretly sharing staff, supplies, overflow
  customers, and a plan to keep the riverfront locally owned.
current_stage: staged_rivalry_and_business_partnership
perspectives:
- subject: character:sera-thornwick
  object: character:calla-riversong
  disposition: 88
  summary: Sera Thornwick trusts Calla Riversong as one of the few people who understands both the work
    and the burden beneath it.
  visibility: subject
- subject: character:calla-riversong
  object: character:sera-thornwick
  disposition: 84
  summary: Calla Riversong answers that trust with steady affection and the practical loyalty of someone
    who intends to remain.
  visibility: subject
history:
- id: first-public-feud
  title: They invented the feud over a soup ladle
  summary: Their supposed rivalry began when Sera accused Calla of stealing a soup ladle in front of traveling
    merchants. The argument drew such a crowd that they agreed to keep performing it.
  occurred_at: When their connection took shape
  visibility: participants
  stage_after: forming_friendship
  perspective_changes:
  - subject: character:sera-thornwick
    object: character:calla-riversong
    after: 63
    summary_after: Sera Thornwick trusts Calla Riversong as one of the few people who understands both
      the work and the burden beneath it.
    visibility: subject
  - subject: character:calla-riversong
    object: character:sera-thornwick
    after: 60
    summary_after: Calla Riversong answers that trust with steady affection and the practical loyalty
      of someone who intends to remain.
    visibility: subject
- id: buyout-defeated
  title: The rivals defeated a buyout together
  summary: When an outside investor tried to buy both businesses separately, each exaggerated the other's
    debts and defects until the offer collapsed. They celebrated in Sera's cellar with Calla's best wine.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: staged_rivalry_and_business_partnership
  stage_before: forming_friendship
  relationship_summary_after: Sera and Calla perform a loud commercial feud while secretly sharing staff,
    supplies, overflow customers, and a plan to keep the riverfront locally owned.
  perspective_changes:
  - subject: character:sera-thornwick
    object: character:calla-riversong
    before: 63
    after: 88
    summary_after: Sera Thornwick trusts Calla Riversong as one of the few people who understands both
      the work and the burden beneath it.
    visibility: subject
  - subject: character:calla-riversong
    object: character:sera-thornwick
    before: 60
    after: 84
    summary_after: Calla Riversong answers that trust with steady affection and the practical loyalty
      of someone who intends to remain.
    visibility: subject
visual:
  prompt: ''
---
