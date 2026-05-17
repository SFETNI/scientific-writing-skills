# /srs-gate — Revision Quality Gate

Run the revision quality gate on the current section or full manuscript. Used both after individual sections and as the final pre-submission check.

## What this does

Invokes `@skills/writing/skill_revision_quality_gate.md` and (for full manuscript) also runs the policy checklist.

## Protocol

### Step 1 — Scope
Ask: "Are you running this gate on a specific section or the full manuscript?"

If a specific section: proceed with that section only.
If full manuscript: run on all accepted sections sequentially, then run the policy checklist.

### Step 2 — Gate execution
Read `@skills/writing/skill_revision_quality_gate.md`.
Read `@templates/NUMERICAL_REGISTRY.md`, `@templates/CLAIM_REGISTER.md`, `@agent_context/ANTI_AI_WRITING_STYLE.md`, `@templates/AUTHOR_CONTEXT.md`.

Apply all gate checks. Produce the gate report.

### Step 3 — Policy checklist (full manuscript only)

Read `@agent_context/JOURNAL_POLICY.md` and `@templates/AUTHOR_CONTEXT.md TARGET_JOURNAL_FAMILY`.

Run the policy checklist:
- [ ] AI use disclosure statement drafted and ready for submission form
- [ ] Data availability statement present (check journal requirement)
- [ ] Competing interests statement present
- [ ] Author contributions statement present (check journal requirement)
- [ ] All AI-assisted sections are logged
- [ ] No AI-generated figures in the manuscript
- [ ] No AI authorship claimed

### Step 4 — Human sign-off

Present the full gate report and policy checklist.

For a section: "Please confirm: Section [name] is accepted as of [date]."
For full manuscript: "Please confirm: the manuscript is submission-ready as of [date]. I certify that all content is accurate and reflects my own scientific work."

**The gate is not cleared until the human confirms explicitly.**

## Human gate: HG2c (per section) or HG5a + HG5b + HG5c (final)

Record in `AGENT_HANDOFF.md`:
```
[Section/Full manuscript] quality gate — PASS — [date]
HG5c — Submission certification: YES — [date]
```
