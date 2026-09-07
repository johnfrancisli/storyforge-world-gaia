---
id: relationship:shifa-and-afaf
name: Physician and herbalist, mentor and student
participants:
- character:shifa-al-tabib
- character:afaf-al-ashab
association: mentor-student
public_status: Afaf al-A'shab the herbalist is known to supply Shifa al-Tabib the physician with rare
  medicinal plants, and the two consult on difficult cases.
bond: Shifa is teaching Afaf the djinn-fire medicine that no herbalist is supposed to learn, because she
  has realized Afaf's contract-bearing status makes her one of the few who can safely handle it. The teaching
  is covert and accelerates a trust neither expected; Afaf is beginning to suspect Shifa is grooming a
  successor for something she has not yet explained.
disposition: 70
summary: Shifa is teaching Afaf the djinn-fire medicine that no herbalist is supposed to learn, because
  she has realized Afaf's contract-bearing status makes her one of the few who can safely handle it. The
  teaching is covert and accelerates a trust neither expected; Afaf is beginning to suspect Shifa is grooming
  a successor for something she has not yet explained.
current_stage: demanding_apprenticeship
perspectives:
- subject: character:shifa-al-tabib
  object: character:afaf-al-ashab
  disposition: 66
  summary: Shifa al-Tabib believes Afaf al-A'shab is worth the severity of the work and feels responsible
    for what the teaching may awaken.
  visibility: subject
- subject: character:afaf-al-ashab
  object: character:shifa-al-tabib
  disposition: 72
  summary: Afaf al-A'shab values Shifa al-Tabib's knowledge but carries private doubts about the lesson,
    the motive, or the price of succeeding.
  visibility: subject
history:
- id: connection-established
  title: The first difficult lesson
  summary: A demanding first lesson revealed both the student's potential and the teacher's exacting expectations.
    Neither could return to being a casual acquaintance afterward.
  occurred_at: When their connection took shape
  visibility: public
  stage_after: forming_mentor
  perspective_changes:
  - subject: character:shifa-al-tabib
    object: character:afaf-al-ashab
    after: 48
    summary_after: Shifa al-Tabib believes Afaf al-A'shab is worth the severity of the work and feels
      responsible for what the teaching may awaken.
    visibility: subject
  - subject: character:afaf-al-ashab
    object: character:shifa-al-tabib
    after: 52
    summary_after: Afaf al-A'shab values Shifa al-Tabib's knowledge but carries private doubts about the
      lesson, the motive, or the price of succeeding.
    visibility: subject
- id: present-balance
  title: The lesson began changing both of them
  summary: Shifa is teaching Afaf the djinn-fire medicine that no herbalist is supposed to learn, because
    she has realized Afaf's contract-bearing status makes her one of the few who can safely handle it.
    The teaching is covert and accelerates a trust neither expected; Afaf is beginning to suspect Shifa
    is grooming a successor for something she has not yet explained.
  occurred_at: During the present chapter
  visibility: gm_only
  stage_after: demanding_apprenticeship
  stage_before: forming_mentor
  relationship_summary_after: Shifa is teaching Afaf the djinn-fire medicine that no herbalist is supposed
    to learn, because she has realized Afaf's contract-bearing status makes her one of the few who can
    safely handle it. The teaching is covert and accelerates a trust neither expected; Afaf is beginning
    to suspect Shifa is grooming a successor for something she has not yet explained.
  perspective_changes:
  - subject: character:shifa-al-tabib
    object: character:afaf-al-ashab
    before: 48
    after: 66
    summary_after: Shifa al-Tabib believes Afaf al-A'shab is worth the severity of the work and feels
      responsible for what the teaching may awaken.
    visibility: subject
  - subject: character:afaf-al-ashab
    object: character:shifa-al-tabib
    before: 52
    after: 72
    summary_after: Afaf al-A'shab values Shifa al-Tabib's knowledge but carries private doubts about the
      lesson, the motive, or the price of succeeding.
    visibility: subject
visual:
  prompt: ''
---
