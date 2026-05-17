# /srs-intro — Introduction Drafting Chain

Draft or improve the Introduction section using the three-skill chain: benchmark positioning → section drafting → claim calibration.

## Prerequisites

Before activating this command, confirm:
- [ ] `/srs-check` has been run and hard errors are resolved (HG0a)
- [ ] `/srs-calibrate` has been run and approved (HG0c)
- [ ] The section plan for Introduction is ready (`@templates/SECTION_PLAN.md` filled, or human provides argument chain)

## Protocol

### Step 1 — Benchmark positioning
Read `@skills/writing/skill_benchmark_positioning.md`.
Ask: "Please list the benchmark and state-of-the-art papers that should be positioned in the Introduction."
Apply the skill to the benchmark list and any existing Introduction text.
Present findings. **Wait for human to confirm positioning framing before proceeding.**

### Step 2 — Section drafting
Read `@skills/writing/skill_section_drafting.md`.
Read `@templates/NUMERICAL_REGISTRY.md` and `@agent_context/ANTI_AI_WRITING_STYLE.md`.

Ask: "Do you have an existing Introduction draft or a section plan (argument chain, key claims)?"
- If existing draft: improve it per skill mandate.
- If section plan: draft from the plan.

Produce the draft with evidence labels on each claim.
**Wait for human to review the draft before proceeding.**

### Step 3 — Claim calibration
Read `@skills/writing/skill_claim_calibration.md`.
Apply it to the approved Introduction draft.
Produce the claim-source map.
Present for human review.

**Wait for human to resolve all UNSUPPORTED and NEEDS_HUMAN_DECISION items.**

### Step 4 — Quality gate
Run `@skills/writing/skill_revision_quality_gate.md` on the completed Introduction.
Present the gate report.

**The Introduction is not accepted until the gate PASSES and the human signs off.**

## Human gate: HG2c (Introduction)

Record in `AGENT_HANDOFF.md`:
```
Introduction accepted — [date] — gate PASS
```
