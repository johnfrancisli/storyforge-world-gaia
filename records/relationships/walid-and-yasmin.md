---
id: relationship:walid-and-yasmin
name: Walid al-Tujjar and Yasmin al-Barrani
visibility: gm
participants:
- character:walid-al-tujjar
- character:yasmin-al-barrani
association: unknown half-siblings
public_status: Walid and Yasmin are rival spice merchants with no known family connection.
bond: They share a mother, though neither knows it. Walid has been paid to spy on Yasmin and has begun trying to protect the woman he does not know is his half-sister.
is_familial: true
kinship:
- subject: character:walid-al-tujjar
  relation: half_sibling_of
  object: character:yasmin-al-barrani
  visibility: gm_only
summary: Walid spies on Yasmin for pay but increasingly shields her from the consequences, unaware that
  the protective instinct he cannot explain is directed toward his half-sister.
current_stage: unrecognized_siblings_in_a_spy_game
perspectives:
- subject: character:walid-al-tujjar
  object: character:yasmin-al-barrani
  disposition: 51
  summary: Walid cannot explain why protecting the merchant he was paid to watch increasingly matters
    more to him than completing the contract cleanly.
  visibility: subject
- subject: character:yasmin-al-barrani
  object: character:walid-al-tujjar
  disposition: 3
  summary: Yasmin regards Walid as a rival and possible spy, though his strangely timed warnings have
    kept her from dismissing him as a simple enemy.
  visibility: subject
history:
- id: paid-to-watch
  title: Walid accepted the contract
  summary: Walid was paid to map Yasmin's trade contacts and political donors. He approached her as a
    rival merchant and expected the work to remain impersonal.
  occurred_at: When their connection took shape
  visibility: gm_only
  stage_after: forming_family
  perspective_changes:
  - subject: character:walid-al-tujjar
    object: character:yasmin-al-barrani
    after: 37
    summary_after: Walid initially treated Yasmin as a profitable target whose habits could be mapped.
    visibility: subject
  - subject: character:yasmin-al-barrani
    object: character:walid-al-tujjar
    after: 2
    summary_after: Yasmin regarded Walid as one more aggressive rival in the spice trade.
    visibility: subject
- id: warning-without-reason
  title: He warned the target
  summary: When his employers prepared to act on his intelligence, Walid fed Yasmin an anonymous warning
    and falsified part of his report. She now suspects the rival watching her is also keeping her alive.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: unrecognized_siblings_in_a_spy_game
  stage_before: forming_family
  relationship_summary_after: Walid spies on Yasmin for pay but increasingly shields her from the consequences,
    unaware that the protective instinct he cannot explain is directed toward his half-sister.
  perspective_changes:
  - subject: character:walid-al-tujjar
    object: character:yasmin-al-barrani
    before: 37
    after: 51
    summary_after: Walid cannot explain why protecting the merchant he was paid to watch increasingly
      matters more to him than completing the contract cleanly.
    visibility: subject
  - subject: character:yasmin-al-barrani
    object: character:walid-al-tujjar
    before: 2
    after: 3
    summary_after: Yasmin regards Walid as a rival and possible spy, though his strangely timed warnings
      have kept her from dismissing him as a simple enemy.
    visibility: subject
visual:
  prompt: ''
---
