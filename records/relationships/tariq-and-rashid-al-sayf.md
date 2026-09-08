---
id: relationship:tariq-and-rashid-al-sayf
name: Tariq and Rashid al-Sayf
participants:
- character:tariq-al-sayf
- character:rashid-al-sayf
association: father and eldest son
public_status: Rashid is Tariq al-Sayf's eldest son and heir to the binding family.
bond: Tariq has raised Rashid to inherit the house and its binding contract, including burdens neither man can discuss freely.
is_familial: true
kinship:
- subject: character:tariq-al-sayf
  relation: parent_of
  object: character:rashid-al-sayf
  visibility: public
summary: Tariq raised Rashid to inherit both the al-Sayf house and its approaching courage-debt, binding
  paternal love to fear and succession.
current_stage: father_and_heir_under_contract
perspectives:
- subject: character:tariq-al-sayf
  object: character:rashid-al-sayf
  disposition: 58
  summary: He loves the son he trained as heir, while his terror of the coming debt drives him toward choices
    Rashid would reject.
  visibility: subject
- subject: character:rashid-al-sayf
  object: character:tariq-al-sayf
  disposition: 62
  summary: He respects his father and understands the courage-debt, but recognizes that fear is shaping
    decisions Tariq will not explain.
  visibility: subject
history:
- id: raised-as-heir
  title: Tariq raised Rashid as the al-Sayf heir
  summary: Rashid was trained to inherit the house, its authority, and the binding contract attached to it.
  visibility: public
  stage_after: father_and_heir
  perspective_changes: []
- id: courage-debt-revealed
  title: Tariq revealed Rashid's coming courage-debt
  summary: Tariq told Rashid that Nuria would take his courage at thirty, revealing the fear beneath the
    patriarch's controlled exterior.
  occurred_at: One year before the current campaign
  visibility: participants
  stage_before: father_and_heir
  stage_after: father_and_heir_under_contract
  perspective_changes:
  - subject: character:rashid-al-sayf
    object: character:tariq-al-sayf
    after: 62
    summary_after: He understands his father's fear but is increasingly alert to what that fear may cause.
visual:
  prompt: ''
image:
  url: ''
  focalPoint:
    x: 0.5
    y: 0.1
  seed: null
---
