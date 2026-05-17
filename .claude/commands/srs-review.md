# /srs-review — Full-Manuscript Reviewer Simulation

Run a 4-role peer reviewer simulation across the complete manuscript. Each role is a bounded, read-only subagent. All reports are presented to the human before any revisions are considered.

## Prerequisites

- [ ] All sections are accepted or near-final
- [ ] `/srs-check` has been run recently
- [ ] `@templates/NUMERICAL_REGISTRY.md` is complete

## Protocol

### Step 1 — Preparation
Read `@skills/review/skill_reviewer_perspective.md`.
Ask: "Is the manuscript complete enough for a full reviewer simulation? Which sections should be included?"

Read the manuscript sections specified by the human.

### Step 2 — Subagent invocation (4 roles)

Invoke four separate bounded review passes using `@templates/subagents/reviewer_simulation_subagent.md`:

**Role 1 — Methodologist**: Focus on experimental design, reproducibility, statistical methods, potential confounds.

**Role 2 — Domain expert**: Focus on positioning, terminology, benchmark selection, interpretation in field context.

**Role 3 — Generalist**: Focus on narrative clarity, Introduction quality, jargon, abstract accuracy.

**Role 4 — Data integrity reviewer**: Audit all numbers against `NUMERICAL_REGISTRY.md`; check figures for label/value consistency; flag any unregistered quantitative claims.

Each role produces: major concerns (≥3), minor concerns, and a one-line verdict.

### Step 3 — Report consolidation

Combine all four reports into a single review document.
Sort concerns by role and severity.
Do NOT propose revisions yet — this step only produces the review report.

**Present the full report to the human (HG4a).**

### Step 4 — Human decision

Ask: "For each concern, please tell me: (A) address — I will revise, (B) rebut — I have a response, (C) out of scope — deliberate choice."

Record all decisions in `AGENT_HANDOFF.md` (HG4b).

**Do not begin revision drafts until the human has decided on each concern.**

## Human gate: HG4a, HG4b

Record in `AGENT_HANDOFF.md`:
```
Reviewer simulation complete — [date]
HG4a — Report read and reviewed — [date]
HG4b — [N] concerns to address, [N] to rebut, [N] out of scope
```
