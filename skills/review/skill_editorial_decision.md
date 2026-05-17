# Skill: Editorial Decision Estimation

## Mandate

Estimate the probable editorial decision (accept / minor revision / major revision / reject) with a rationale grounded in the manuscript content and target journal standards. This is a simulation — not a real editorial decision. Its purpose is to help the author identify the most critical issues before submission. The human reads and interprets this estimate; the agent does not prescribe revisions.

## Required inputs

- Complete manuscript (or summary of all sections)
- Reviewer simulation report from `skill_reviewer_perspective.md` (if available)
- `@templates/AUTHOR_CONTEXT.md` — target journal, contribution level, quality standard

## Assessment dimensions

| Dimension | Weight | What is assessed |
|---|---|---|
| Scientific contribution | High | Is the contribution novel and significant for the target journal? |
| Methodological soundness | High | Are the methods appropriate, reproducible, and correctly applied? |
| Claim calibration | High | Are claims proportionate to the evidence? |
| Citation quality | Medium | Are references current, relevant, and accurately cited? |
| Presentation quality | Medium | Is the manuscript well-structured and clearly written? |
| Journal fit | High | Does the scope and depth match the target journal's typical articles? |

## Decision categories

- **Accept** — all dimensions pass; minor issues do not impede publication decision
- **Minor revision** — 1–2 dimensions have addressable issues; major concerns are absent
- **Major revision** — core methodological, contribution, or claim concerns require substantial work
- **Reject** — significant scientific, methodological, or contribution gap; or out of scope for journal

## Acceptance criteria

1. Estimated decision is based on specific evidence from the manuscript, not generic comments.
2. Each dimension is assessed with a rating (STRONG / ADEQUATE / WEAK / MISSING) and a specific observation.
3. The rationale is honest even if unflattering.

## Human-in-the-loop checkpoint

Human reads the estimate and must:
- Decide which critical issues to address before submission
- Judge whether the estimated decision changes the submission target journal
- Not treat this estimate as a guarantee — it is a training tool, not an editorial board decision

## Fail conditions

- Decision is estimated without referencing specific manuscript content.
- The assessment is uniformly positive (this is a critical simulation, not a cheerleader).

## Output format

```
EDITORIAL DECISION ESTIMATE — [Date]
Target journal: [from AUTHOR_CONTEXT.md]

ASSESSMENT BY DIMENSION
  Scientific contribution: ADEQUATE — contribution is incremental; positioned correctly for [journal tier]
  Methodological soundness: STRONG — protocol is reproducible; split rationale is justified
  Claim calibration: WEAK — §3.4 overclaims based on limited sample; §4.2 lacks hedging
  Citation quality: ADEQUATE — most primary claims are cited; 3 claims lack ABSTRACT_RELEVANT verification
  Presentation quality: ADEQUATE — structure is clear; Abstract overpromises
  Journal fit: ADEQUATE — scope matches; contribution level is below top-tier but appropriate for [journal]

ESTIMATED DECISION: MAJOR REVISION

PRIMARY REASONS:
  1. Claim calibration issues in §3.4 and §4.2 are likely to be flagged by reviewers
  2. Abstract makes a stronger claim than the Results support — revise before submission
  3. Limitations section missing — required by [journal] author guidelines

ITEMS FOR HUMAN DECISION:
  - Should the contribution claim in the Introduction be strengthened or narrowed?
  - Is the current sample size sufficient for the primary claim in §3.4?
```
