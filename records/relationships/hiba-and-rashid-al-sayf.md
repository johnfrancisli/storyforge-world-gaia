---
id: relationship:hiba-and-rashid-al-sayf
name: Hiba and Rashid al-Sayf
participants:
- character:hiba-al-sayf
- character:rashid-al-sayf
association: younger sister and elder brother
public_status: Hiba is Rashid al-Sayf's ten-year-old sister.
bond: Hiba knows her father is considering a sacrifice to save Rashid, while Rashid knows their father is making a decision about his sister that he may be unable to undo.
is_familial: true
kinship:
- subject: character:hiba-al-sayf
  relation: sibling_of
  object: character:rashid-al-sayf
  visibility: public
summary: Rashid is determined to protect his young sister, while Hiba senses that their father is deciding
  which child will pay the family's debt.
current_stage: siblings_under_contract_threat
perspectives:
- subject: character:rashid-al-sayf
  object: character:hiba-al-sayf
  disposition: 90
  summary: He would rather surrender his own courage than allow Hiba to be traded for his safety.
  visibility: subject
history:
- id: raised-as-al-sayf-siblings
  title: Hiba and Rashid grew up as al-Sayf siblings
  summary: Rashid was raised as the eldest heir and Hiba as the family's firstborn daughter.
  visibility: public
  stage_after: siblings
  perspective_changes: []
- id: rashid-noticed-danger
  title: Rashid noticed a decision forming around Hiba
  summary: His father's private meetings and fear convinced Rashid that Hiba may be made to pay for the
    contract coming due on him.
  visibility: gm_only
  stage_before: siblings
  stage_after: siblings_under_contract_threat
  perspective_changes:
  - subject: character:rashid-al-sayf
    object: character:hiba-al-sayf
    after: 90
    summary_after: He is prepared to lose his courage rather than let the family sacrifice her.
visual:
  prompt: ''
---
