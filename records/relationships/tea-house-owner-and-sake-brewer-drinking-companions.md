---
id: relationship:hanako-and-saya
name: Tea house owner and sake brewer, drinking companions
participants:
- character:hanako
- character:morikawa-saya
association: friendship
public_status: The tea house owner and the sake brewer are known to be old friends who share drinks after
  hours and refer customers to each other.
bond: Their friendship predates both their businesses — they survived a famine together as young women,
  rationing what little they had. Neither married, and the town quietly assumes they are simply set in
  their ways; in truth they are the closest thing to family either has.
disposition: 88
is_familial: true
kinship:
- subject: character:hanako
  relation: chosen_family_of
  object: character:morikawa-saya
  visibility: participants
summary: Hanako and Saya have been each other's chosen family since surviving famine together; shared
  cups and quiet physical tenderness say what neither has felt a need to name.
current_stage: lifelong_companions_with_unnamed_tenderness
perspectives:
- subject: character:hanako
  object: character:morikawa-saya
  disposition: 91
  summary: Hanako loves the life she and Saya have built and expresses it through food, warm baths, and
    always saving the seat nearest her own.
  visibility: subject
- subject: character:morikawa-saya
  object: character:hanako
  disposition: 93
  summary: Saya regards Hanako as home; her teasing grows flirtatious after the second cup, but the devotion
    beneath it is entirely sober.
  visibility: subject
history:
- id: famine-cup
  title: They shared one cup through the famine
  summary: As young women they watered one cup of weak brew across three evenings and took turns pretending
    not to be hungry. Neither survived alone, though both publicly credit luck.
  occurred_at: When their connection took shape
  visibility: participants
  stage_after: forming_family
  perspective_changes:
  - subject: character:hanako
    object: character:morikawa-saya
    after: 66
    summary_after: Hanako loves the life she and Saya have built and expresses it through food, warm baths,
      and always saving the seat nearest her own.
    visibility: subject
  - subject: character:morikawa-saya
    object: character:hanako
    after: 67
    summary_after: Saya regards Hanako as home; her teasing grows flirtatious after the second cup, but
      the devotion beneath it is entirely sober.
    visibility: subject
- id: closed-door-toast
  title: The private toast became nightly
  summary: After closing, Saya brings one small bottle and Hanako lowers the shutters. Their toast ends
    with shoulders touching, hands lingering, and an argument about which woman is too old to be blushing.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: lifelong_companions_with_unnamed_tenderness
  stage_before: forming_family
  relationship_summary_after: Hanako and Saya have been each other's chosen family since surviving famine
    together; shared cups and quiet physical tenderness say what neither has felt a need to name.
  perspective_changes:
  - subject: character:hanako
    object: character:morikawa-saya
    before: 66
    after: 91
    summary_after: Hanako loves the life she and Saya have built and expresses it through food, warm baths,
      and always saving the seat nearest her own.
    visibility: subject
  - subject: character:morikawa-saya
    object: character:hanako
    before: 67
    after: 93
    summary_after: Saya regards Hanako as home; her teasing grows flirtatious after the second cup, but
      the devotion beneath it is entirely sober.
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
