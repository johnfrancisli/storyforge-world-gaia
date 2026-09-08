---
id: relationship:malik-and-tariq-al-sayf
name: Two binding family scions, Idris and al-Sayf
participants:
- character:malik-idris
- character:tariq-al-sayf
association: rivalry
public_status: Malik Idris of the Idris family and Tariq al-Sayf, patriarch of the al-Sayf family, are
  the two foremost figures of the binding families and their competition for Council influence is public.
bond: Their families have controlled rival contracts for generations, and the two men have inherited a
  feud older than either of them. Each respects the other's cunning and would never say so, because in
  Al-Khayzar the admission of an equal is the first step toward being outmaneuvered by one.
disposition: 18
summary: Malik and Tariq are public Council rivals who recognize one another's cunning while concealing
  that respect behind an inherited feud.
current_stage: council_rivals
perspectives:
- subject: character:malik-idris
  object: character:tariq-al-sayf
  disposition: -18
  summary: He respects Tariq's political skill but treats every move from the older patriarch as an attempt
    to outmaneuver the Idris house.
  visibility: subject
- subject: character:tariq-al-sayf
  object: character:malik-idris
  disposition: -25
  summary: He recognizes Malik as a capable rival and refuses to admit it, because acknowledging an equal
    would surrender political ground.
  visibility: subject
history:
- id: inherited-house-feud
  title: They inherited a generational feud
  summary: Rival binding contracts placed the Idris and al-Sayf houses in competition before either man
    assumed authority.
  occurred_at: Before either participant inherited his present role
  visibility: public
  stage_after: inherited_rivals
  perspective_changes: []
- id: council-competition
  title: Their rivalry moved onto the Council
  summary: Competition for influence made their opposition public, even as each privately recognized the
    other's cunning.
  visibility: public
  stage_before: inherited_rivals
  stage_after: council_rivals
  perspective_changes:
  - subject: character:malik-idris
    object: character:tariq-al-sayf
    after: -18
    summary_after: Respect for Tariq's skill is outweighed by suspicion of his political intent.
  - subject: character:tariq-al-sayf
    object: character:malik-idris
    after: -25
    summary_after: He treats Malik as a dangerous equal he cannot publicly acknowledge.
visual:
  prompt: ''
image:
  url: ''
  focalPoint:
    x: 0.5
    y: 0.1
  seed: null
---
