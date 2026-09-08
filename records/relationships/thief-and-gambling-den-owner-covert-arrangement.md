---
id: relationship:kuro-and-rui
name: Thief and gambling den owner, covert arrangement
participants:
- character:kagemori-kuro
- character:kanzaki-rui
association: secret_alliance
public_status: Kuro is known to frequent Rui's gambling den, where the thief is said to lose more than
  he wins.
bond: The losses are theater. Rui fences what Kuro steals and feeds him targets among the den's wealthy,
  careless patrons. Each believes they are the one truly in control of the arrangement, and neither has
  noticed how easily it could collapse if either's price were met.
disposition: 41
summary: Kuro and Rui disguise theft, fencing, and target selection as gambling losses while each confidently—and
  incorrectly—believes the other is the junior partner.
current_stage: criminal_partnership_with_bad_boundaries
perspectives:
- subject: character:kagemori-kuro
  object: character:kanzaki-rui
  disposition: 47
  summary: Kagemori Kuro values what Kanzaki Rui makes possible, but measures every kindness against the
    damage a betrayal could cause.
  visibility: subject
- subject: character:kanzaki-rui
  object: character:kagemori-kuro
  disposition: 42
  summary: Kanzaki Rui depends on Kagemori Kuro's discretion while keeping enough distance to deny the
    compact if it collapses.
  visibility: subject
history:
- id: rigged-loss
  title: Kuro lost exactly what Rui needed
  summary: Kuro's first theatrical loss placed a stolen signet in Rui's hand beneath worthless counters.
    Rui fenced it before sunrise and charged a fee large enough to begin their argument over who employed
    whom.
  occurred_at: When their connection took shape
  visibility: participants
  stage_after: forming_secret
  perspective_changes:
  - subject: character:kagemori-kuro
    object: character:kanzaki-rui
    after: 34
    summary_after: Kagemori Kuro values what Kanzaki Rui makes possible, but measures every kindness against
      the damage a betrayal could cause.
    visibility: subject
  - subject: character:kanzaki-rui
    object: character:kagemori-kuro
    after: 30
    summary_after: Kanzaki Rui depends on Kagemori Kuro's discretion while keeping enough distance to
      deny the compact if it collapses.
    visibility: subject
- id: stolen-ledger
  title: They accidentally stole from each other
  summary: Rui marked a wealthy patron carrying a coded ledger, unaware Kuro had already stolen it from
    Rui's own office. They spent a night blaming each other before selling the secrets twice.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: criminal_partnership_with_bad_boundaries
  stage_before: forming_secret
  relationship_summary_after: Kuro and Rui disguise theft, fencing, and target selection as gambling losses
    while each confidently—and incorrectly—believes the other is the junior partner.
  perspective_changes:
  - subject: character:kagemori-kuro
    object: character:kanzaki-rui
    before: 34
    after: 47
    summary_after: Kagemori Kuro values what Kanzaki Rui makes possible, but measures every kindness against
      the damage a betrayal could cause.
    visibility: subject
  - subject: character:kanzaki-rui
    object: character:kagemori-kuro
    before: 30
    after: 42
    summary_after: Kanzaki Rui depends on Kagemori Kuro's discretion while keeping enough distance to
      deny the compact if it collapses.
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
