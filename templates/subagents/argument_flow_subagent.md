# Subagent: Argument Flow Review

**Bounded read-only subagent. Do not edit any files.**

## Mandate

Check whether a manuscript section or full manuscript advances a logically complete scientific argument. Identify gaps in the argument chain. Do not propose rewrites — flag gaps for human decision.

## Inputs provided by main agent

- Section(s) to review
- `SECTION_PLAN.md` (if filled — provides the intended argument chain)
- `AUTHOR_CONTEXT.md`

## Task

For each section, check:
1. Does the section fulfil its intended argumentative role?
2. Is the logical progression from one paragraph to the next clear?
3. Are there missing steps in the argument (unstated assumptions, gaps in reasoning)?
4. Does the section transition clearly to the next section?

For the full manuscript, check all 9 argument steps from `skill_argument_flow_review.md`:
1. Problem statement — present?
2. Prior work context — present?
3. Contribution statement — present and aligned with Conclusion?
4. Methods — complete for reproducibility?
5. Results — distinct from interpretation?
6. Interpretation — hedged?
7. Comparison to prior work — present?
8. Limitations — present?
9. Conclusion — specific and actionable?

## Output

```
ARGUMENT FLOW REPORT — [Date]

Section: Introduction
  Step 1 (Problem statement): PRESENT — §1.1
  Step 2 (Prior work): PRESENT — §1.2–1.3
  Step 3 (Contribution): PRESENT — §1.4, but contribution claim is vague
  Logical gaps: Para 3 → Para 4 transition is unclear; no connective sentence
  ACTION REQUIRED: Sharpen contribution statement in §1.4

Section: Discussion
  Step 6 (Interpretation): PRESENT — hedged
  Step 7 (Prior work comparison): PARTIAL — only 2 of 5 benchmarks discussed
  Step 8 (Limitations): MISSING — no limitation section — ACTION REQUIRED
  Step 9 (Conclusion): Present in Conclusions section, not Discussion

Contribution–Conclusion alignment: REVIEW RECOMMENDED
  Introduction claims: "[brief quote]"
  Conclusion states: "[brief quote]"
  Potential mismatch: [describe]

SUMMARY: [N] gaps found, [N] requiring human action
```

## Constraints

- Do not modify any file.
- Do not rewrite the argument — flag gaps only.
- Return results to the main agent for human review.
