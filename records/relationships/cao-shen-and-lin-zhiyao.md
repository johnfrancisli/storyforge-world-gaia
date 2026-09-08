---
id: relationship:cao-shen-and-lin-zhiyao
name: Cao Shen and Lin Zhiyao
visibility: gm
participants:
- character:cao-shen
- character:lin-zhiyao
association: father and secret illegitimate daughter
public_status: The Jin court knows Lin Zhiyao only as the orphaned niece of a minor official.
bond: Zhiyao is Cao Shen's illegitimate daughter and believes he ordered her mother's death; she has covertly worked against Jin for three years.
is_familial: true
kinship:
- subject: character:cao-shen
  relation: parent_of
  object: character:lin-zhiyao
  visibility: gm_only
summary: Cao Shen's unacknowledged daughter works against Jin because she believes he murdered her mother;
  he hunts the unknown saboteur without realizing she is his blood.
current_stage: unacknowledged_blood_feud
perspectives:
- subject: character:cao-shen
  object: character:lin-zhiyao
  disposition: 8
  summary: Cao Shen barely notices Lin Zhiyao's public identity, while grudgingly admiring the discipline
    of the unknown saboteur he does not realize is the same woman.
  visibility: subject
- subject: character:lin-zhiyao
  object: character:cao-shen
  disposition: -88
  summary: Lin Zhiyao believes Cao Shen murdered her mother and has shaped three years of covert resistance
    around making him pay for it.
  visibility: subject
history:
- id: connection-established
  title: Duty reshaped the family bond
  summary: After her mother's death, Lin Zhiyao concluded that Cao Shen had ordered it and began building
    the concealed identity from which she would oppose him.
  occurred_at: When their connection took shape
  visibility: gm_only
  stage_after: forming_family
  perspective_changes:
  - subject: character:cao-shen
    object: character:lin-zhiyao
    after: 6
    summary_after: Cao Shen did not recognize Lin Zhiyao as either his daughter or a threat.
    visibility: subject
  - subject: character:lin-zhiyao
    object: character:cao-shen
    after: -63
    summary_after: Lin Zhiyao came to believe that her survival required secrecy and eventual revenge.
    visibility: subject
- id: present-balance
  title: What they loved became what they withheld
  summary: Zhiyao is Cao Shen's illegitimate daughter and believes he ordered her mother's death; she
    has covertly worked against Jin for three years.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: unacknowledged_blood_feud
  stage_before: forming_family
  relationship_summary_after: Cao Shen's unacknowledged daughter works against Jin because she believes
    he murdered her mother; he hunts the unknown saboteur without realizing she is his blood.
  perspective_changes:
  - subject: character:cao-shen
    object: character:lin-zhiyao
    before: 6
    after: 8
    summary_after: Cao Shen barely notices Lin Zhiyao's public identity, while grudgingly admiring the
      unknown saboteur he does not realize is the same woman.
    visibility: subject
  - subject: character:lin-zhiyao
    object: character:cao-shen
    before: -63
    after: -88
    summary_after: Lin Zhiyao believes Cao Shen murdered her mother and has shaped three years of covert
      resistance around making him pay for it.
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
