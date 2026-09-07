---
id: relationship:marcus-and-sable
name: Mercenary captain and bounty hunter
participants:
- character:marcus-briarwood
- character:sable-quickthorn
association: enemies
public_status: The mercenary captain and the bounty hunter are known to cross paths professionally and
  are said to dislike each other.
bond: Years ago, Sable was hired to bring in a deserter who had joined Marcus's company. Marcus refused
  to give him up, and Sable took him anyway — killing two of Marcus's men in the process. The deserter
  hanged. Marcus has neither forgiven nor forgotten, and Sable knows it, and watches her own back whenever
  his company is in town.
disposition: 8
summary: Years ago, Sable was hired to bring in a deserter who had joined Marcus's company. Marcus refused
  to give him up, and Sable took him anyway — killing two of Marcus's men in the process. The deserter
  hanged. Marcus has neither forgiven nor forgotten, and Sable knows it, and watches her own back whenever
  his company is in town.
current_stage: active_enmity
perspectives:
- subject: character:marcus-briarwood
  object: character:sable-quickthorn
  disposition: -91
  summary: Marcus Briarwood sees Sable Quickthorn as a personal danger that can no longer be answered
    by compromise.
  visibility: subject
- subject: character:sable-quickthorn
  object: character:marcus-briarwood
  disposition: -58
  summary: Sable Quickthorn returns the hostility, but knows that understanding Marcus Briarwood remains
    essential to surviving the conflict.
  visibility: subject
history:
- id: connection-established
  title: The grievance became personal
  summary: An earlier confrontation transformed opposition into a personal wound. From that point forward,
    neither treated the conflict as merely professional.
  occurred_at: When their connection took shape
  visibility: public
  stage_after: forming_enemy
  perspective_changes:
  - subject: character:marcus-briarwood
    object: character:sable-quickthorn
    after: -66
    summary_after: Marcus Briarwood sees Sable Quickthorn as a personal danger that can no longer be answered
      by compromise.
    visibility: subject
  - subject: character:sable-quickthorn
    object: character:marcus-briarwood
    after: -42
    summary_after: Sable Quickthorn returns the hostility, but knows that understanding Marcus Briarwood
      remains essential to surviving the conflict.
    visibility: subject
- id: present-balance
  title: The cost of hatred became clear
  summary: Years ago, Sable was hired to bring in a deserter who had joined Marcus's company. Marcus refused
    to give him up, and Sable took him anyway — killing two of Marcus's men in the process. The deserter
    hanged. Marcus has neither forgiven nor forgotten, and Sable knows it, and watches her own back whenever
    his company is in town.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: active_enmity
  stage_before: forming_enemy
  relationship_summary_after: Years ago, Sable was hired to bring in a deserter who had joined Marcus's
    company. Marcus refused to give him up, and Sable took him anyway — killing two of Marcus's men in
    the process. The deserter hanged. Marcus has neither forgiven nor forgotten, and Sable knows it, and
    watches her own back whenever his company is in town.
  perspective_changes:
  - subject: character:marcus-briarwood
    object: character:sable-quickthorn
    before: -66
    after: -91
    summary_after: Marcus Briarwood sees Sable Quickthorn as a personal danger that can no longer be answered
      by compromise.
    visibility: subject
  - subject: character:sable-quickthorn
    object: character:marcus-briarwood
    before: -42
    after: -58
    summary_after: Sable Quickthorn returns the hostility, but knows that understanding Marcus Briarwood
      remains essential to surviving the conflict.
    visibility: subject
visual:
  prompt: ''
---
