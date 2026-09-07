---
id: relationship:dunya-and-nabil
name: Two glassblowers, accidental magician and reluctant weaponsmith
participants:
- character:dunya-al-zujaj
- character:nabil-al-zujaj
association: cousins and fellow glassblowers
public_status: Dunya al-Zujaj and her older cousin Nabil al-Zujaj are glassblowers of the same quarter
  and share a workshop name.
bond: They are cousins who inherited the same furnace, and each has stumbled into a dangerous secret
  the other does not know — Dunya's glass accidentally channels djinn-fire, and Nabil has been coerced
  into shaping glass weapons for a binding family. Each is protecting the other by hiding what they do
  after hours, and the day their two secrets collide in the same furnace may burn the workshop to the
  ground.
disposition: 52
is_familial: true
kinship:
- subject: character:dunya-al-zujaj
  relation: cousin_of
  object: character:nabil-al-zujaj
  visibility: public
summary: Dunya and Nabil are affectionate cousins sharing a craft lineage and furnace, while each hides
  dangerous glasswork from the other in the hope of keeping them safe.
current_stage: close_cousins_hiding_dangerous_secrets
perspectives:
- subject: character:dunya-al-zujaj
  object: character:nabil-al-zujaj
  disposition: 72
  summary: She trusts her older cousin as family and a fellow craftsperson, unaware of the weapon vessels
    he has been coerced into making.
  visibility: subject
- subject: character:nabil-al-zujaj
  object: character:dunya-al-zujaj
  disposition: 78
  summary: He is protective of Dunya and withholds the arsenal's existence because he believes knowing
    would place her in greater danger.
  visibility: subject
history:
- id: inherited-shared-furnace
  title: They inherited the same furnace
  summary: Their shared workshop and craft made the cousins part of the same glassblowing lineage.
  visibility: public
  stage_after: cousins_and_fellow_glassblowers
  perspective_changes: []
- id: dunya-found-bound-sand
  title: Dunya discovered light-bearing glass
  summary: Dunya began mining sand from an old djinn site and making affordable bottles that hold light,
    without telling Nabil the full source of the effect.
  occurred_at: Three years before the current campaign
  visibility: gm_only
  stage_before: cousins_and_fellow_glassblowers
  stage_after: cousins_with_secrets
  perspective_changes:
  - subject: character:dunya-al-zujaj
    object: character:nabil-al-zujaj
    after: 72
    summary_after: She remains close to him while keeping her dwindling magical sand supply private.
- id: nabil-saw-the-arsenal
  title: Nabil discovered the vessel arsenal
  summary: After supplying specialized vessels, Nabil entered the locked chamber and saw hundreds of
    captured djinn fragments; he chose not to tell Dunya because he feared for her safety.
  visibility: gm_only
  stage_before: cousins_with_secrets
  stage_after: close_cousins_hiding_dangerous_secrets
  perspective_changes:
  - subject: character:nabil-al-zujaj
    object: character:dunya-al-zujaj
    after: 78
    summary_after: His affection has become protective secrecy as he searches for a way to stop the arsenal.
visual:
  prompt: ''
---
