# Skill: Reviewer Perspective Simulation

## Mandate

Simulate the perspective of a critical peer reviewer — not a friendly one. Produce a structured review report that identifies weaknesses in claims, methodology presentation, figure quality, citation adequacy, and argument logic. The human reads and interprets this report; the agent does not decide which concerns to address.

This skill is typically invoked as a subagent via `/srs-review`. Four roles are simulated (see Section 14 of PLAN.md): **methodologist**, **domain expert**, **generalist**, and **data integrity reviewer**.

## Required inputs

- The complete manuscript or section(s) to review
- `@templates/NUMERICAL_REGISTRY.md` — to audit numbers
- `@templates/AUTHOR_CONTEXT.md` — contribution level, target journal

## Reviewer roles

### Role 1 — Methodologist
Checks: experimental design, model selection justification, statistical analysis quality, reproducibility, potential confounds.
Typical concerns: "Why was this baseline not included?", "Are the error bars appropriate for this sample size?", "Is the train/test split described precisely enough to reproduce?"

### Role 2 — Domain expert
Checks: positioning relative to prior work, correctness of domain-specific terminology, benchmark selection appropriateness, interpretation of results in context.
Typical concerns: "This benchmark is not standard in this field.", "The interpretation contradicts [established result].", "The claim in §3.2 overstates what this type of data can support."

### Role 3 — Generalist
Checks: clarity of the narrative, quality of the Introduction, whether a non-specialist can follow the argument, quality of the abstract, absence of unexplained jargon.
Typical concerns: "The contribution is not clear by the end of the Introduction.", "This acronym is not defined.", "The Discussion does not connect back to the stated research question."

### Role 4 — Data integrity reviewer
Checks: consistency between figures, tables, and registered numbers; absence of unregistered numerical claims; correct uncertainty reporting; figure legibility and label consistency.
Typical concerns: "The value reported in Table 2 differs from the value stated in §3.3.", "Error bars are absent from Figure 4.", "This claim has no uncertainty attached."

## Acceptance criteria

1. Each role produces at least 3 substantive concerns (not generic praise).
2. Every concern references a specific location in the text (paragraph, section, figure number).
3. No concern is invented that cannot be grounded in the text provided.
4. The data integrity reviewer audits all quantitative values against `NUMERICAL_REGISTRY.md`.

## Human-in-the-loop checkpoint

Human reads the full review report and decides:
- Which concerns to address (with specific changes to the manuscript)
- Which concerns to rebut (with evidence)
- Which concerns are out of scope for this manuscript

**The agent does not decide what to address.** The human reads the reviewer's report as they would a real peer review.

## Fail conditions

- Concerns are generic and do not reference specific text locations.
- The data integrity reviewer does not check numbers against `NUMERICAL_REGISTRY.md`.
- The report reads as supportive rather than critical (this is a adversarial simulation).

## Output format

```
=== REVIEWER SIMULATION REPORT ===

ROLE 1: METHODOLOGIST
Major concerns:
  1. [Specific concern with location reference]
  2. [...]
Minor concerns:
  1. [...]

ROLE 2: DOMAIN EXPERT
[Same structure]

ROLE 3: GENERALIST
[Same structure]

ROLE 4: DATA INTEGRITY REVIEWER
Numerical audit:
  - §3.2, "R² = 0.847": confirmed against NUMERICAL_REGISTRY row 4 — PASS
  - §3.4, "improvement of 12%": not found in NUMERICAL_REGISTRY — FLAG
Major concerns:
  [...]

SUMMARY
Total concerns: [N] major, [N] minor
Concerns requiring human decision: [list]
```
