# V18 → Web Native parity audit — FINAL31

Source of truth: `Quan_ly_hoc_sinh_V18.py` in this package, unchanged.

## Behavioral fixes in FINAL31
- Delete a student: teacher password required, matching V18's destructive-confirmation flow.
- Delete all data: teacher password required before destructive action.
- Latest session endpoint: `/api/session/latest` re-reads the current SQLite values so teacher edits are authoritative for class/team/group.
- Existing Excel, QR, chat, reminders, diagram, officers, scores, tasks, summaries, approvals and account flows remain in the same package.
