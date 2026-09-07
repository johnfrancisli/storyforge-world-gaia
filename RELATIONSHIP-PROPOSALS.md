# Relationship proposals (non-canonical)

This report contains review candidates only. Nothing here is part of Gaia's relationship graph until an author creates or enriches a record under `records/relationships/`.

## Satsuki and Haru as chosen family

- Proposed endpoints: [[character:ichinose-satsuki]] and [[character:ashikara-haru]]
- Predicate: `chosen_family_of`
- Proposed visibility: `participants`
- Evidence: Satsuki's biography says she has become a mother figure to Haru since his mother died.
- Rationale: “Mother figure” may describe affection or mentorship rather than a mutually recognized chosen-family bond. Author confirmation is needed.

## Kai and Tamatoa as siblings

- Proposed endpoints: [[character:kai]] and [[character:tamatoa]]
- Predicate: `sibling_of` or `half_sibling_of`
- Proposed visibility: `participants`
- Evidence: Separate canonical records identify [[character:lani]] as the mother of each man.
- Rationale: The records do not identify their fathers, so the exact sibling predicate is unresolved. The graph should not guess between full and half siblings.

## Tamamo and Katsura as chosen family

- Proposed endpoints: [[character:tamamo]] and [[character:katsura]]
- Predicate: `chosen_family_of`
- Proposed visibility: `participants`
- Evidence: Their relationship record calls Katsura Tamamo's “younger kinspirit” and says they love one another fiercely, while Katsura's biography describes them as ancient rivals.
- Rationale: “Kinspirit” may be literal yokai terminology rather than chosen family. The former broad `association: family` was removed pending a cultural ruling.

## Lyria and Regor as former chosen family

- Proposed endpoints: [[character:lyria-ironheart]] and [[character:regor-blackhammer]]
- Predicate: `chosen_family_of`, if the bond is still considered familial
- Proposed visibility: `participants`
- Evidence: Their relationship record says they once loved one another as siblings before their rivalry divided them.
- Rationale: The schema has no `former_chosen_family_of` predicate, and the prose is explicitly past-tense. Author confirmation is needed before treating it as a current chosen-family bond.

## Cao Shen and Sun Liang as former sworn brothers

- Proposed endpoints: [[character:cao-shen]] and [[character:sun-liang]]
- Predicate: `chosen_family_of`, if their oath still carries familial standing
- Proposed visibility: `participants`
- Evidence: Their relationship record says they were once sworn brothers before ambition split them into enemies.
- Rationale: The oath is canonical, but its present kinship status is unclear and the schema has no former-sworn-family predicate.

## Resolved: Rashid al-Sayf romance conflict

- Proposed endpoints: [[character:rashid-al-sayf]] and [[character:zahra-al-dhahab]]
- Existing record: [[relationship:rashid-al-sayf-and-zahra-binding-daughter]]
- Evidence conflict: The relationship record says Rashid and Zahra are secretly in love. Zahra's biography instead says she has refused marriage arrangements because she is secretly in love with the unnamed djinn Rafiq. Rashid's biography identifies [[character:reem-al-faris]] as his clandestine al-Faris contact.
- Resolution: The relationship is now an intentional, asymmetric triangle. Rashid is falling in love with Zahra; Zahra feels attraction and political interest but remains in love with Rafiq. The structured dispositions and history preserve that imbalance.

## Resolved: Rashid's “Layla” reference

- Proposed endpoint correction: [[character:reem-al-faris]]
- Evidence: Rashid's biography calls his secret contact “the youngest daughter of the al-Faris family, Layla” but immediately supplies the stable ID `character:reem-al-faris`.
- Resolution: The canonical stable ID was retained and the contradictory visible name was corrected to Reem in Rashid's biography.

## Isam's refused child contract and Hiba

- Proposed endpoints: [[character:isam-al-miskin]] and [[character:hiba-al-sayf]]
- Predicate: no kinship; possible protector/beneficiary history
- Proposed visibility: `gm_only`
- Evidence: Isam was destroyed by the al-Sayf family after refusing to write a contract trapping an unnamed ten-year-old daughter. Hiba is Tariq al-Sayf's ten-year-old daughter and is currently endangered by a different proposed bargain.
- Rationale: The matching family and age are suggestive, but the records never identify the earlier child as Hiba. A relationship would conflate two contracts without author confirmation.

## Audit note: Astrid Blacktide

`records/characters/astrid-blacktide.md` was empty. It was restored with only the stable ID and canonical name already established by the filename and existing references; no biography, traits, or relationships were invented from it.
