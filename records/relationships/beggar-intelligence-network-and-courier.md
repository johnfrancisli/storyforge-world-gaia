---
id: relationship:isam-and-bushra
name: Beggar intelligence network and courier
participants:
- character:isam-al-miskin
- character:bushra-al-risala
association: secret_alliance
public_status: A beggar and a courier of Al-Khayzar are not publicly known to have any relationship.
bond: Isam runs a shadow intelligence network from the gutter, and Bushra is his fastest courier — together
  they move information that the binding families would kill to suppress. Isam was once a scribe and Bushra
  knows it; she is the only person who still addresses him by his old name, and he has never decided whether
  that is mercy or a threat.
disposition: 58
summary: Isam and Bushra run a covert information route against the binding families, but his uncertainty
  about her motives keeps their trust from matching their effectiveness.
current_stage: covert_partnership
perspectives:
- subject: character:isam-al-miskin
  object: character:bushra-al-risala
  disposition: 48
  summary: He values her speed and discretion, but her use of his old name leaves him unsure whether she
    is offering mercy or demonstrating leverage.
  visibility: subject
- subject: character:bushra-al-risala
  object: character:isam-al-miskin
  disposition: 68
  summary: She trusts his purpose enough to carry the network's most dangerous information and preserves
    the identity the binding family tried to erase.
  visibility: subject
history:
- id: joined-shadow-network
  title: Bushra joined the shadow network
  summary: Isam made Bushra his fastest courier, giving their separate intelligence work a shared route.
  occurred_at: After Isam established his network of discarded servants
  visibility: participants
  stage_after: covert_partnership
  perspective_changes:
  - subject: character:isam-al-miskin
    object: character:bushra-al-risala
    after: 55
    summary_after: He came to rely on her speed and discretion.
  - subject: character:bushra-al-risala
    object: character:isam-al-miskin
    after: 65
    summary_after: She accepted him as a principled handler for dangerous information.
- id: old-name
  title: Bushra used Isam's former name
  summary: She became the only person who still addressed him by the name taken from him when the al-Sayf
    family ruined him.
  visibility: participants
  stage_before: covert_partnership
  stage_after: covert_partnership
  perspective_changes:
  - subject: character:isam-al-miskin
    object: character:bushra-al-risala
    before: 55
    after: 48
    summary_after: He cannot decide whether the gesture is mercy or a reminder of what she knows.
  - subject: character:bushra-al-risala
    object: character:isam-al-miskin
    before: 65
    after: 68
    summary_after: She continues to recognize the identity his former employers tried to erase.
visual:
  prompt: ''
---
