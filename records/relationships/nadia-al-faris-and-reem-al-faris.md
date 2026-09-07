---
id: relationship:nadia-al-faris-and-reem-al-faris
name: Nadia al-Faris and Reem al-Faris
participants:
- character:nadia-al-faris
- character:reem-al-faris
association: grandmother and granddaughter
public_status: Reem is Nadia al-Faris's granddaughter and heir to the al-Faris binding line.
bond: Reem is the matriarch's granddaughter and designated heir, but has concealed the ancient voice she
  hears because she fears Nadia would answer it by binding her to a contract she did not choose. Nadia's
  private view of Reem is not established in canon.
summary: The al-Faris matriarch and her granddaughter are joined by succession, while Reem secretly fears
  what Nadia would do if she discovered the voice guiding her research.
current_stage: matriarch_and_heir_with_hidden_voice
is_mutual: false
is_romantic: false
is_familial: true
kinship:
- subject: character:nadia-al-faris
  relation: grandparent_of
  object: character:reem-al-faris
  visibility: public
perspectives:
- subject: character:reem-al-faris
  object: character:nadia-al-faris
  disposition: -10
  summary: She recognizes Nadia's authority but fears her grandmother would bind her if the hidden voice
    and forbidden research became known.
  visibility: subject
history:
- id: named-al-faris-heir
  title: Reem became heir to the al-Faris line
  summary: Nadia's granddaughter took her place in the binding family's succession despite being third-born.
  visibility: public
  stage_after: matriarch_and_heir
  perspective_changes: []
- id: reem-hid-the-voice
  title: Reem concealed the ancient voice
  summary: After hearing the voice from childhood, Reem hid it from her family and secretly studied the
    original language of the Pact in the family vault.
  occurred_at: From age nine through the current campaign
  visibility: gm_only
  stage_before: matriarch_and_heir
  stage_after: matriarch_and_heir_with_hidden_voice
  perspective_changes:
  - subject: character:reem-al-faris
    object: character:nadia-al-faris
    after: -10
    summary_after: Fear that Nadia would impose a contract keeps Reem from trusting her with the truth.
visual:
  prompt: ''
---
