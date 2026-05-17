# /srs-results — Results Section Drafting Chain

Draft or improve the Results section using: results writing → figure QC → claim calibration.

## Prerequisites

- [ ] `/srs-check` run and cleared (HG0a)
- [ ] Style calibration approved (HG0c)
- [ ] All accepted figures and tables are ready (or listed)
- [ ] Section plan for Results ready (argument plan: subsection order, key finding per subsection)

## Protocol

### Step 1 — Argument plan confirmation
Read `@skills/writing/skill_results_writing.md`.

Ask: "Please provide the argument plan for Results: subsection names, and the key finding you want to report in each subsection."

**Present the argument plan. Wait for human to approve it (HG1 for Results) before any prose is written.**

### Step 2 — Figure QC (parallel with drafting preparation)
Read `@skills/figures/skill_figure_qc.md`.
Ask: "Please describe or reference the figures for this section."
Apply the QC checklist to each figure described.
Present the QC report.
**Wait for human to approve the QC report before proceeding (HG3a).**

### Step 3 — Results drafting
Read `@templates/NUMERICAL_REGISTRY.md` and `@agent_context/ANTI_AI_WRITING_STYLE.md`.
Draft the Results section from the approved argument plan and registered values.
All claims must carry `RESULT_SUPPORTED` labels; no interpretation allowed.

**Wait for human review of the draft.**

### Step 4 — Claim calibration
Read `@skills/writing/skill_claim_calibration.md`.
Apply to the Results draft.
Check for any unregistered values or interpretation sentences that should move to Discussion.

**Wait for human to resolve all UNSUPPORTED and INTERPRETATION issues.**

### Step 5 — Quality gate
Run `@skills/writing/skill_revision_quality_gate.md`.
**Results not accepted until gate PASSES.**

## Human gate: HG2c (Results)

Record in `AGENT_HANDOFF.md`:
```
Results accepted — [date] — gate PASS
```
