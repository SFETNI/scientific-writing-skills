# /srs-methods — Methods Section Drafting Chain

Draft or improve the Methods section using: methods writing → claim evidence verification.

## Prerequisites

- [ ] `/srs-check` run and cleared (HG0a)
- [ ] Style calibration approved (HG0c)
- [ ] Section plan for Methods ready (subsection structure, scope, key items to include)

## Protocol

### Step 1 — Scope confirmation
Read `@skills/writing/skill_methods_writing.md`.
Ask: "Please provide your study design document or a bullet-point outline of the methods (materials, procedure, metrics, software)."

Present the proposed subsection structure for Methods.
**Wait for human to approve the structure (HG1 for Methods) before drafting begins.**

### Step 2 — Methods drafting
Read `@templates/NUMERICAL_REGISTRY.md` and `@agent_context/ANTI_AI_WRITING_STYLE.md`.
Draft the Methods section from the approved outline and human-provided content.
Produce output with evidence labels (`METHOD_DEFINITION` for all claims in this section).

**Wait for human to review the draft.**

### Step 3 — Claim evidence verification
Read `@skills/integrity/skill_claim_evidence_verification.md`.
Apply to the Methods draft to verify that all numerical values (sample sizes, parameter values, split ratios) are in `NUMERICAL_REGISTRY.md`.

**Wait for human to resolve any UNSUPPORTED or unregistered values.**

### Step 4 — Quality gate
Run `@skills/writing/skill_revision_quality_gate.md`.
Present the gate report.

**Methods section not accepted until gate PASSES.**

## Human gate: HG2c (Methods)

Record in `AGENT_HANDOFF.md`:
```
Methods accepted — [date] — gate PASS
```
