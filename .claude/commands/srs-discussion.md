# /srs-discussion — Discussion Drafting Chain

Draft or improve the Discussion section using: argument flow review → claim calibration → reviewer perspective.

## Prerequisites

- [ ] Results section accepted (HG2c for Results)
- [ ] Style calibration approved (HG0c)
- [ ] Section plan for Discussion ready (interpretation chain, comparison to prior work, limitations)

## Protocol

### Step 1 — Argument flow check
Read `@skills/review/skill_argument_flow_review.md`.
Apply to the complete manuscript (all accepted sections so far) to verify argument completeness before drafting Discussion.
Present the argument map.

**Flag any gaps (missing limitations, contribution–conclusion mismatch, etc.) to the human. Wait for direction before proceeding.**

### Step 2 — Section plan confirmation
Ask: "Please provide the discussion plan: key interpretations to develop, benchmarks to compare against, limitations to state."

**Present the section plan. Wait for human to approve it before prose is written (HG1 for Discussion).**

### Step 3 — Discussion drafting
Read `@skills/writing/skill_section_drafting.md`, `@templates/NUMERICAL_REGISTRY.md`, `@agent_context/ANTI_AI_WRITING_STYLE.md`.
Draft the Discussion from the approved plan.
Label: `INTERPRETATION` for interpretations, `LITERATURE_SUPPORTED` for benchmark comparisons, `SPECULATION` for forward-looking claims.

**Wait for human review.**

### Step 4 — Claim calibration
Read `@skills/writing/skill_claim_calibration.md`.
Apply to Discussion. Check that all `INTERPRETATION` claims are hedged; all `SPECULATION` is labeled; no unregistered numbers appear.

**Wait for human to resolve all UNSUPPORTED and NEEDS_HUMAN_DECISION items.**

### Step 5 — Reviewer perspective
Read `@skills/review/skill_reviewer_perspective.md`.
Simulate a critical reviewer's response to the Discussion section (domain expert and generalist roles).

**Present the review. Human decides what to address and what to rebut (HG4b).**

### Step 6 — Quality gate
Run `@skills/writing/skill_revision_quality_gate.md`.
**Discussion not accepted until gate PASSES.**

## Human gate: HG2c (Discussion)

Record in `AGENT_HANDOFF.md`:
```
Discussion accepted — [date] — gate PASS
```
