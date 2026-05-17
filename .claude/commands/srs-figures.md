# /srs-figures — Figures & Tables QC Chain

Comprehensive quality control for all figures and tables: QC → captions → visual consistency → table design.

## Prerequisites

- [ ] All figures and tables are in their near-final form
- [ ] `@templates/NUMERICAL_REGISTRY.md` is complete with all values shown in figures/tables

## Protocol

### Step 1 — Figure QC
Read `@skills/figures/skill_figure_qc.md`.
Ask: "Please describe each figure (or paste the caption). How many figures are in the manuscript?"
Apply the QC checklist to each figure.
Present the QC report.

**Wait for human to approve the report before any revisions are initiated (HG3a).**

### Step 2 — Caption drafting/review
Read `@skills/figures/skill_figure_caption_writing.md`.
For each figure: check or draft the caption following the skill mandate (main message first, then description, scope, panels).
Verify all values in captions against `NUMERICAL_REGISTRY.md`.

**Wait for human to confirm captions match figure content (HG3b).**

### Step 3 — Visual consistency
Read `@skills/figures/skill_visual_consistency.md`.
Apply across all figures: check naming, colour palette, notation, unit consistency.
Present the consistency report.

**Wait for human to confirm proposed corrections.**

### Step 4 — Table design (if tables exist)
Read `@skills/figures/skill_table_design.md`.
Apply to each table: structure, column headers, units, uncertainty values.
Present redesign recommendations.

**Wait for human to approve any restructuring before it is implemented.**

## Outputs

- Figure QC report (one row per figure)
- Revised/drafted captions
- Visual consistency report
- Table redesign recommendations (if applicable)

All outputs are advisory — Codex handles the file-level changes once the human approves.

## Human gate: HG3a, HG3b

Record in `AGENT_HANDOFF.md`:
```
Figure QC approved — [date]
Captions confirmed — [date]
```
