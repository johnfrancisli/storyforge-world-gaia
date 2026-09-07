---
id: relationship:malik-and-zuhayr
name: Malik Idris and Zuhayr the Patient
participants:
- character:malik-idris
- character:zuhayr-the-patient
association: 'contract-bound: creditor and debtor'
public_status: Malik is the heir to the Idris family's oldest djinn contract. Zuhayr is the djinn bound
  by it. The contract's terms are family knowledge but not public.
bond: 'Zuhayr genuinely wants to help Malik renegotiate — a willing partner is more useful than a bound
  servant. But the contract''s deadline is binding on both of them, and neither can extend it alone. Zuhayr
  is the most dangerous kind of ally: one who is on Malik''s side but constrained by law from giving him
  more time. Their relationship is warm in a way that makes the debt more painful, not less.'
disposition: 35
summary: Malik and Zuhayr are warm but unequal allies trapped on opposite sides of a binding contract neither
  can alter alone.
current_stage: contract_bound_allies
perspectives:
- subject: character:malik-idris
  object: character:zuhayr-the-patient
  disposition: 20
  summary: He believes Zuhayr genuinely prefers negotiation, but cannot forget that the djinn must collect
    him if the deadline passes.
  visibility: subject
- subject: character:zuhayr-the-patient
  object: character:malik-idris
  disposition: 62
  summary: He finds Malik interesting and sincerely wants a willing partnership, though djinn law prevents
    him from simply releasing the debt.
  visibility: subject
history:
- id: idris-contract-created
  title: Malik's grandfather bound Zuhayr
  summary: The Idris contract promised the firstborn of each generation and placed Malik's future inside
    an agreement made before his birth.
  occurred_at: Three generations before the current campaign
  visibility: participants
  stage_after: inherited_debt
  perspective_changes: []
- id: malik-learned-his-price
  title: Malik learned he was the contract's price
  summary: From childhood, Malik knew that being the Idris firstborn meant he was owed to Zuhayr.
  occurred_at: During Malik's childhood
  visibility: participants
  stage_before: inherited_debt
  stage_after: known_creditor_and_debtor
  perspective_changes:
  - subject: character:malik-idris
    object: character:zuhayr-the-patient
    after: -15
    summary_after: He associated Zuhayr with a future taken from him before he could consent.
- id: zuhayr-offered-renegotiation
  title: Zuhayr began appearing to Malik
  summary: Zuhayr explained that he preferred renegotiation and a willing partner, but could not extend
    the deadline by himself.
  visibility: participants
  stage_before: known_creditor_and_debtor
  stage_after: contract_bound_allies
  perspective_changes:
  - subject: character:malik-idris
    object: character:zuhayr-the-patient
    before: -15
    after: 20
    summary_after: He accepts Zuhayr's goodwill without mistaking it for freedom from the contract.
  - subject: character:zuhayr-the-patient
    object: character:malik-idris
    after: 62
    summary_after: He wants Malik to become a willing partner rather than a resentful servant.
visual:
  prompt: ''
---
