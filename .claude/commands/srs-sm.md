# /srs-sm — Supplementary Materials Chain

Draft and QC the Supplementary Materials: scope approval → SM writing → figure QC for SM figures.

## Prerequisites

- [ ] Main manuscript sections accepted
- [ ] Human has a list of content designated for SM (figures, extended methods, sensitivity analyses, etc.)

## Protocol

### Step 1 — SM scope approval
Read `@skills/writing/skill_sm_writing.md`.
Ask: "Please list everything you intend to include in SM: figures, tables, extended methods, raw data tables, sensitivity analyses."

Present a proposed SM structure (Table of Contents with item types and labels: Figure S1, Table S1, etc.).

**Wait for human to approve the SM scope and structure before any content is drafted (HG3c).**

Check journal policy:
- Read `@agent_context/JOURNAL_POLICY.md` for `TARGET_JOURNAL_FAMILY` SM rules.
- Flag any items that the journal does not allow in SM.

### Step 2 — SM content drafting
Draft each SM item from the content the human provides.
Apply evidence labels to any claims.
Verify all quantitative values against `NUMERICAL_REGISTRY.md`.

Produce cross-reference statements for the main text (where each SM item should be first mentioned).

**Wait for human to review the SM draft.**

### Step 3 — SM figure QC
Read `@skills/figures/skill_figure_qc.md`.
Apply to all SM figures.
Present the QC report.

**Wait for human to approve before revisions are initiated.**

### Step 4 — Cross-reference check
Verify that every SM item is referenced at least once in the main text.
List any orphan SM items (in SM but not referenced in main text).

**Wait for human to resolve orphan items.**

## Human gate: HG3c

Record in `AGENT_HANDOFF.md`:
```
SM scope approved — [date]
SM draft accepted — [date] — gate PASS
```
