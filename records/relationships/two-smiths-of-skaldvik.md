---
id: relationship:ragna-and-sten
name: Two smiths of Skaldvik
participants:
- character:ragna-forgebreak
- character:sten-ironwake
association: rivalry
public_status: Ragna Forgebreak and Sten Ironwake are both smiths serving the Skaldvik community, and
  their competing work is a common comparison.
bond: They share a forge because neither can afford to build a second, and they have divided the work
  by a grudging agreement — she forges the tools, he forges the weapons. The arrangement works but chafes;
  each believes the other's half is the easier one, and the forge rings with pointed silences.
disposition: 36
summary: Ragna and Sten divide one forge between tools and weapons, sustaining a productive cold war over
  whose work is harder while quietly correcting each other's mistakes after dark.
current_stage: shared_forge_cold_war
perspectives:
- subject: character:ragna-forgebreak
  object: character:sten-ironwake
  disposition: 29
  summary: Ragna Forgebreak respects Sten Ironwake's ability but experiences every success as a challenge
    that must be answered.
  visibility: subject
- subject: character:sten-ironwake
  object: character:ragna-forgebreak
  disposition: 34
  summary: Sten Ironwake resents Ragna Forgebreak's pressure while privately relying on the standard only
    a worthy rival can provide.
  visibility: subject
history:
- id: chalk-line
  title: They divided the forge with chalk
  summary: Ragna drew a line down the forge and declared one half fit for honest tools and the other for
    Sten's oversized knives. Sten moves the line an inch toward her side every market day.
  occurred_at: When their connection took shape
  visibility: public
  stage_after: forming_rivalry
  perspective_changes:
  - subject: character:ragna-forgebreak
    object: character:sten-ironwake
    after: 21
    summary_after: Ragna Forgebreak respects Sten Ironwake's ability but experiences every success as
      a challenge that must be answered.
    visibility: subject
  - subject: character:sten-ironwake
    object: character:ragna-forgebreak
    after: 24
    summary_after: Sten Ironwake resents Ragna Forgebreak's pressure while privately relying on the standard
      only a worthy rival can provide.
    visibility: subject
- id: secret-repair
  title: Each repaired the other's failure
  summary: Ragna secretly reforged a cracked spear socket before Sten's customer arrived; Sten later replaced
    the handle of her best hammer without comment. Both know. Neither has surrendered the argument.
  occurred_at: During the present chapter
  visibility: participants
  stage_after: shared_forge_cold_war
  stage_before: forming_rivalry
  relationship_summary_after: Ragna and Sten divide one forge between tools and weapons, sustaining a
    productive cold war over whose work is harder while quietly correcting each other's mistakes after
    dark.
  perspective_changes:
  - subject: character:ragna-forgebreak
    object: character:sten-ironwake
    before: 21
    after: 29
    summary_after: Ragna Forgebreak respects Sten Ironwake's ability but experiences every success as
      a challenge that must be answered.
    visibility: subject
  - subject: character:sten-ironwake
    object: character:ragna-forgebreak
    before: 24
    after: 34
    summary_after: Sten Ironwake resents Ragna Forgebreak's pressure while privately relying on the standard
      only a worthy rival can provide.
    visibility: subject
visual:
  prompt: ''
---
