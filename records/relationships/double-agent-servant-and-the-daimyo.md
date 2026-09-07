---
id: relationship:tomi-and-daimyo-takeda
name: Double agent servant and the daimyo
participants:
- character:sakaki-tomi
- character:takeda-renji
association: secret_alliance
public_status: Tomi is a household servant within the Takeda clan's service, unremarkable and overlooked.
bond: Tomi reports to Daimyo Takeda on the shogunate's interior movements — a spy placed so low in the
  household that no one thinks to watch her. Takeda treats her with a quiet courtesy he shows no other
  servant, which is the only thing preventing her from being made. She has begun to wonder what happens
  to her the day she is no longer useful.
disposition: 52
summary: Tomi reports to Daimyo Takeda on the shogunate's interior movements — a spy placed so low in
  the household that no one thinks to watch her. Takeda treats her with a quiet courtesy he shows no other
  servant, which is the only thing preventing her from being made. She has begun to wonder what happens
  to her the day she is no longer useful.
current_stage: covert_interdependence
perspectives:
- subject: character:sakaki-tomi
  object: character:takeda-renji
  disposition: 24
  summary: Sakaki Tomi values what Takeda Renji makes possible, but measures every kindness against the
    damage a betrayal could cause.
  visibility: subject
- subject: character:takeda-renji
  object: character:sakaki-tomi
  disposition: 46
  summary: Takeda Renji depends on Sakaki Tomi's discretion while keeping enough distance to deny the
    compact if it collapses.
  visibility: subject
history:
- id: connection-established
  title: The private bargain was struck
  summary: A first exchange of protected information made each party useful to the other and gave both
    enough leverage to make betrayal dangerous.
  occurred_at: When their connection took shape
  visibility: public
  stage_after: forming_secret
  perspective_changes:
  - subject: character:sakaki-tomi
    object: character:takeda-renji
    after: 17
    summary_after: Sakaki Tomi values what Takeda Renji makes possible, but measures every kindness against
      the damage a betrayal could cause.
    visibility: subject
  - subject: character:takeda-renji
    object: character:sakaki-tomi
    after: 33
    summary_after: Takeda Renji depends on Sakaki Tomi's discretion while keeping enough distance to deny
      the compact if it collapses.
    visibility: subject
- id: present-balance
  title: The secret became mutual leverage
  summary: Tomi reports to Daimyo Takeda on the shogunate's interior movements — a spy placed so low in
    the household that no one thinks to watch her. Takeda treats her with a quiet courtesy he shows no
    other servant, which is the only thing preventing her from being made. She has begun to wonder what
    happens to her the day she is no longer useful.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: covert_interdependence
  stage_before: forming_secret
  relationship_summary_after: Tomi reports to Daimyo Takeda on the shogunate's interior movements — a
    spy placed so low in the household that no one thinks to watch her. Takeda treats her with a quiet
    courtesy he shows no other servant, which is the only thing preventing her from being made. She has
    begun to wonder what happens to her the day she is no longer useful.
  perspective_changes:
  - subject: character:sakaki-tomi
    object: character:takeda-renji
    before: 17
    after: 24
    summary_after: Sakaki Tomi values what Takeda Renji makes possible, but measures every kindness against
      the damage a betrayal could cause.
    visibility: subject
  - subject: character:takeda-renji
    object: character:sakaki-tomi
    before: 33
    after: 46
    summary_after: Takeda Renji depends on Sakaki Tomi's discretion while keeping enough distance to deny
      the compact if it collapses.
    visibility: subject
visual:
  prompt: ''
---
