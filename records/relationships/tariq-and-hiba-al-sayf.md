---
id: relationship:tariq-and-hiba-al-sayf
name: Tariq and Hiba al-Sayf
participants:
- character:tariq-al-sayf
- character:hiba-al-sayf
association: father and daughter
public_status: Hiba is Tariq al-Sayf's ten-year-old daughter and the family's firstborn daughter.
bond: Tariq loves Hiba but is weighing a new djinn bargain whose demanded price is her future; Hiba knows only that her father has grown frightened and distant.
is_familial: true
kinship:
- subject: character:tariq-al-sayf
  relation: parent_of
  object: character:hiba-al-sayf
  visibility: public
summary: Tariq loves Hiba but is considering a bargain that would trade away her future; she feels his
  fear and distance without knowing the choice before him.
current_stage: parent_and_child_under_strain
perspectives:
- subject: character:tariq-al-sayf
  object: character:hiba-al-sayf
  disposition: 65
  summary: He loves his daughter and wants to save her, but fear has made him consider using her future
    as the price of a replacement contract.
  visibility: subject
- subject: character:hiba-al-sayf
  object: character:tariq-al-sayf
  disposition: -15
  summary: She still sees him as her father, but his frightened distance and her nightmares make her fear
    that he may let the white-fire figure take her.
  visibility: subject
history:
- id: raised-as-firstborn-daughter
  title: Tariq raised Hiba as his firstborn daughter
  summary: Their public relationship was that of a binding-family patriarch and his young daughter.
  visibility: public
  stage_after: father_and_daughter
  perspective_changes: []
- id: replacement-bargain-considered
  title: Tariq considered the replacement bargain
  summary: A new djinn demanded Hiba's future as the price for replacing Nuria's contract, and Tariq began
    weighing that cost against the debt facing Rashid.
  visibility: gm_only
  stage_before: father_and_daughter
  stage_after: parent_and_child_under_strain
  perspective_changes:
  - subject: character:tariq-al-sayf
    object: character:hiba-al-sayf
    before: 80
    after: 65
    summary_after: Love remains, but fear has compromised the certainty that he will protect her.
  - subject: character:hiba-al-sayf
    object: character:tariq-al-sayf
    before: 70
    after: -15
    summary_after: She senses that something is being decided about her and no longer feels safe in his silence.
visual:
  prompt: ''
---
