---
id: relationship:cao-shen-and-sun-liang
name: Warlords of Jin and Chu
participants:
- character:cao-shen
- character:sun-liang
association: enemies
public_status: The warlord of Jin and the warlord of Chu are the principal rivals of the Sangguo conflict,
  and their enmity is the stuff of popular legend.
bond: They were once sworn brothers under the same banner before ambition split them. Each remembers the
  exact betrayal — though they disagree on who struck first — and neither will rest while the other holds
  land. The personal hatred has long outlasted any strategic rationale for the war between their states.
disposition: 5
summary: Cao Shen and Sun Liang converted the collapse of sworn brotherhood into a war whose strategic
  purpose has been consumed by personal hatred and competing memories of betrayal.
current_stage: war_without_a_rational_end
perspectives:
- subject: character:cao-shen
  object: character:sun-liang
  disposition: -96
  summary: Cao Shen sees Sun Liang as a personal danger that can no longer be answered by compromise.
  visibility: subject
- subject: character:sun-liang
  object: character:cao-shen
  disposition: -93
  summary: Sun Liang returns the hostility, but knows that understanding Cao Shen remains essential to
    surviving the conflict.
  visibility: subject
history:
- id: sworn-brothers
  title: They swore brotherhood beneath one banner
  summary: Before Jin and Chu divided them, Cao Shen and Sun Liang mixed blood into the same wine and
    promised that neither would seek power without the other.
  occurred_at: When their connection took shape
  visibility: gm_only
  stage_after: forming_enemy
  perspective_changes:
  - subject: character:cao-shen
    object: character:sun-liang
    after: -69
    summary_after: Cao Shen sees Sun Liang as a personal danger that can no longer be answered by compromise.
    visibility: subject
  - subject: character:sun-liang
    object: character:cao-shen
    after: -67
    summary_after: Sun Liang returns the hostility, but knows that understanding Cao Shen remains essential
      to surviving the conflict.
    visibility: subject
- id: rivergate-betrayal
  title: Rivergate made reconciliation impossible
  summary: At Rivergate each withheld reinforcements expecting the other to seize sole command. Thousands
    died while both armies waited, and each warlord now teaches that the other betrayed him first.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: war_without_a_rational_end
  stage_before: forming_enemy
  relationship_summary_after: Cao Shen and Sun Liang converted the collapse of sworn brotherhood into
    a war whose strategic purpose has been consumed by personal hatred and competing memories of betrayal.
  perspective_changes:
  - subject: character:cao-shen
    object: character:sun-liang
    before: -69
    after: -96
    summary_after: Cao Shen sees Sun Liang as a personal danger that can no longer be answered by compromise.
    visibility: subject
  - subject: character:sun-liang
    object: character:cao-shen
    before: -67
    after: -93
    summary_after: Sun Liang returns the hostility, but knows that understanding Cao Shen remains essential
      to surviving the conflict.
    visibility: subject
visual:
  prompt: ''
---
