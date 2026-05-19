# Skill: Argument Flow Review

## Mandate

Verify that the manuscript advances a logically complete scientific argument from introduction to conclusion. Check whether each section fulfils its argumentative role, whether the paper's central claim is established progressively, and whether gaps in the argument chain exist. Produce an argument map for human review.

## Required inputs

- Complete manuscript sections (Introduction through Conclusions/Discussion)
- `@templates/SECTION_PLAN.md` (if filled — provides the intended argument chain)
- `@templates/AUTHOR_CONTEXT.md`

## Argument structure verification

A well-structured scientific manuscript advances through these steps:

1. **Problem statement** (Introduction §1): Why does this problem matter? What is unsolved?
2. **Prior work context** (Introduction §2): What has been done? What gap remains?
3. **Contribution statement** (Introduction §3): Specifically, what does this paper do?
4. **Methods** (Methods): How was it done? Is the protocol reproducible?
5. **Results** (Results): What was found? (Data only — no interpretation)
6. **Interpretation** (Discussion §1): What do the results mean?
7. **Comparison to prior work** (Discussion §2): How do these results relate to established knowledge?
8. **Limitations** (Discussion §3): What does this paper not answer? What are the boundaries?
9. **Conclusion** (Conclusions): What has been established? What is the actionable takeaway?

## Acceptance criteria

1. All 9 argument steps are present (gaps are flagged).
2. The contribution statement in the Introduction matches the Conclusion.
3. The Discussion does not introduce new results.
4. Limitations are stated explicitly (not omitted).
5. The final sentence of the manuscript states a concrete actionable conclusion.
6. Within Results/Discussion, the evidence that justifies selecting a focal case appears before detailed interpretation of that selected case.
7. Reordered sections preserve coherent figure/table numbering, cross-reference order, and transition sentences.


## Local order checks within Results and Discussion

In addition to the manuscript-wide argument map, inspect the local order of subsections:

- **Prerequisite evidence:** Does the reader see the benchmark, hierarchy, screen, or comparison that justifies the focal item before the text analyzes that item in detail?
- **Transition logic:** Does the first sentence of each subsection depend only on evidence that has already been introduced?
- **Figure sequence:** Do figure and table numbers follow the order in which evidence is needed by the argument?
- **No selected-item inversion:** Flag cases where the manuscript interprets a selected model, condition, material, cohort, or method before explaining why it was selected.
- **No orphaned cross-reference ranges:** After reordering, check ranges such as "Figs. X-Y" and references to earlier/later sections.

This review must remain content-agnostic: record the structural issue, not project-specific findings or numerical outcomes.

## Human-in-the-loop checkpoint

Human reviews the argument map and must:
- Confirm that the described argument chain matches their intended message
- Decide whether flagged gaps should be filled, or whether they are intentional scope boundaries
- Approve the argument map before any structural revisions are made

## Fail conditions

- The contribution statement and the Conclusion describe different outcomes.
- The Discussion introduces a new result not shown in the Results section.
- No limitation is stated anywhere in the manuscript.
- The argument map cannot be reconstructed from the text (incoherent structure).
- A focal item is analyzed in detail before the comparison or selection rationale that makes it focal.

## Output format

```
ARGUMENT FLOW MAP — [Date]

Step 1 — Problem statement: PRESENT — §1.1, lines 1–8
Step 2 — Prior work context: PRESENT — §1.2–1.4
Step 3 — Contribution statement: PRESENT — §1.5, last paragraph
Step 4 — Methods: PRESENT — §2
Step 5 — Results: PRESENT — §3
Step 6 — Interpretation: PRESENT — §4.1
Step 7 — Comparison to prior work: PARTIAL — §4.2 mentions two benchmarks but does not interpret differences
Step 8 — Limitations: MISSING — no limitations section found — ACTION REQUIRED
Step 9 — Conclusion: PRESENT — §5

GAPS REQUIRING HUMAN DECISION:
  - Step 7: Deepen comparison to prior work in §4.2
  - Step 8: Add limitations paragraph — this is required by most journals

Contribution–Conclusion alignment: PARTIAL
  Introduction claims: "a surrogate model for thermal conductivity prediction"
  Conclusion states: "a validated gradient boosting framework" — verify alignment
```
