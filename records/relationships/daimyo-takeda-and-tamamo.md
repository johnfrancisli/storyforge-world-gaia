---
id: relationship:takeda-and-tamamo
name: Daimyo Takeda and Tamamo
participants:
- character:takeda-renji
- character:tamamo
association: covert alliance
public_status: No public relationship. A daimyo and a wild kitsune would not be seen together.
bond: Takeda thinks he is using Tamamo to create yokai incidents that prove the shrine network's weakness.
  Tamamo is using Takeda to weaken the wards she hates. Neither trusts the other. Both believe they are
  the one in control. They are both wrong.
disposition: -10
summary: Takeda thinks he is using Tamamo to create yokai incidents that prove the shrine network's weakness.
  Tamamo is using Takeda to weaken the wards she hates. Neither trusts the other. Both believe they are
  the one in control. They are both wrong.
current_stage: covert_interdependence
perspectives:
- subject: character:takeda-renji
  object: character:tamamo
  disposition: -22
  summary: Takeda Renji values what Tamamo makes possible, but measures every kindness against the damage
    a betrayal could cause.
  visibility: subject
- subject: character:tamamo
  object: character:takeda-renji
  disposition: -35
  summary: Tamamo depends on Takeda Renji's discretion while keeping enough distance to deny the compact
    if it collapses.
  visibility: subject
history:
- id: connection-established
  title: The private bargain was struck
  summary: A first exchange of protected information made each party useful to the other and gave both
    enough leverage to make betrayal dangerous.
  occurred_at: When their connection took shape
  visibility: participants
  stage_after: forming_secret
  perspective_changes:
  - subject: character:takeda-renji
    object: character:tamamo
    after: -16
    summary_after: Takeda Renji values what Tamamo makes possible, but measures every kindness against
      the damage a betrayal could cause.
    visibility: subject
  - subject: character:tamamo
    object: character:takeda-renji
    after: -25
    summary_after: Tamamo depends on Takeda Renji's discretion while keeping enough distance to deny the
      compact if it collapses.
    visibility: subject
- id: present-balance
  title: The secret became mutual leverage
  summary: Takeda thinks he is using Tamamo to create yokai incidents that prove the shrine network's
    weakness. Tamamo is using Takeda to weaken the wards she hates. Neither trusts the other. Both believe
    they are the one in control. They are both wrong.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: covert_interdependence
  stage_before: forming_secret
  relationship_summary_after: Takeda thinks he is using Tamamo to create yokai incidents that prove the
    shrine network's weakness. Tamamo is using Takeda to weaken the wards she hates. Neither trusts the
    other. Both believe they are the one in control. They are both wrong.
  perspective_changes:
  - subject: character:takeda-renji
    object: character:tamamo
    before: -16
    after: -22
    summary_after: Takeda Renji values what Tamamo makes possible, but measures every kindness against
      the damage a betrayal could cause.
    visibility: subject
  - subject: character:tamamo
    object: character:takeda-renji
    before: -25
    after: -35
    summary_after: Tamamo depends on Takeda Renji's discretion while keeping enough distance to deny the
      compact if it collapses.
    visibility: subject
visual:
  prompt: ''
---
