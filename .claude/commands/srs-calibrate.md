# /srs-calibrate — Style Calibration

Run style calibration from `context/` papers (Step 0c). Must be run before any section drafting begins, and approved by the human before proceeding.

## What this does

Invokes `@skills/workflow/skill_style_calibration.md` on the contents of `context/target_journal/` and `context/group_papers/`.

## Protocol

1. Read `@skills/workflow/skill_style_calibration.md`.
2. Read `@templates/AUTHOR_CONTEXT.md` to get `TARGET_JOURNAL_FAMILY` and field.
3. List all `.md` files in `context/target_journal/` and `context/group_papers/`.
4. If both are empty: produce a family-defaults report and label it "BASED ON JOURNAL FAMILY DEFAULTS — no actual papers read."
5. If papers are present: read them and extract the style dimensions described in the skill.
6. Produce the calibration report in the format specified by the skill.
7. Present the report to the human.

## After running

Ask: "Does this calibration report match your experience with the target journal? Please approve it before we begin drafting."

Do not begin any section drafting until the human approves the report (say "approved" or "yes").

Record gate clearance in `AGENT_HANDOFF.md`:
```
HG0c — Style calibration approved — [date]
Style key points: [brief summary of the most important calibration outcomes]
```

## Human gate: HG0c

Style calibration report must be explicitly approved before first drafting session.
