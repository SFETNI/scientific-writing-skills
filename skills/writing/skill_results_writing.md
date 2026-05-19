# Skill: Results Writing

## Mandate

Draft the Results section as a structured reporting of accepted figures and tables. Each subsection reports what was found — in measured, hedged, factual language — without interpretation. Interpretation belongs in the Discussion. The skill organises the argument plan approved by the human into prose, using only registered numerical values.

## Required inputs

- Accepted figures and tables (provided or listed by human)
- `@templates/NUMERICAL_REGISTRY.md` — all accepted quantitative claims
- `@templates/SECTION_PLAN.md` (filled for Results) — argument chain: subsection order, key findings per subsection
- `@templates/AUTHOR_CONTEXT.md` — RESULT_FLEXIBILITY, target journal
- Figure captions (from `skill_figure_caption_writing.md`, if available)

## Acceptance criteria

1. Every quantitative value is drawn from `NUMERICAL_REGISTRY.md`.
2. No interpretation appears in Results (flag any sentence beginning with "This suggests," "This demonstrates," "These results indicate that...").
3. Each subsection opens with a sentence stating what was measured or compared.
4. Each subsection closes with a sentence summarising the key finding of that subsection.
5. Every figure or table in the manuscript is referenced at least once in the Results section.
6. Uncertainty values (± or confidence intervals) are reported for all primary metrics.
7. Past tense throughout (results were observed, were measured, showed, etc.).
8. The subsection order respects prerequisite logic: the comparison or selection evidence appears before detailed analysis of the selected case, model, method, or condition.
9. Any derived diagnostic quantity is explicitly defined before a relative change, ratio, normalized score, or ablation result is reported.
10. If section order changes, figure/table numbering, filenames, captions, cross-references, and any figure-range statements are checked again.

## Human-in-the-loop checkpoint

Human must:
- Approve the argument plan (subsection order, key finding per subsection) **before** any prose is written
- Confirm that the subsection order tells the reader why a selected item is being analyzed before the detailed analysis begins
- Confirm that all quantitative values in the draft match `NUMERICAL_REGISTRY.md`
- Confirm that no interpretation has crossed over from Discussion
- Run `skill_claim_calibration.md` on the completed draft

No Results subsection is accepted without the argument plan being approved first.

## Fail conditions

Reject the output if:
- A number appears that is not in `NUMERICAL_REGISTRY.md`.
- An interpretation sentence appears (move it to Discussion).
- A subsection presents results that were not in the approved argument plan.
- A detailed selected-case analysis appears before the evidence that justifies that selection.
- A relative change or ablation metric is reported before the underlying baseline and monitored quantity are defined.
- `RESULT_FLEXIBILITY: LOCKED` is set and any value was modified.

## Boundary: Results vs. Discussion

Results states what was observed. Discussion explains what it means.

Allowed in Results:
- "The model achieved R² = 0.847 ± 0.031 on the test set."
- "Feature importance analysis identified variable X as the dominant predictor."

Not allowed in Results:
- "This suggests that the model generalises well to unseen conditions."
- "The high R² demonstrates the effectiveness of the proposed approach."

## Reusable revision lessons

When revising an existing Results section, perform these checks before editing prose:

1. **Selection-before-detail check:** if the manuscript chooses a headline model, condition, cohort, catalyst, treatment, or benchmark using a comparison, place that comparison before the detailed selected-item analysis.
2. **Quantity-separation check:** distinguish prediction error, selection criteria, penalties, diagnostics, residuals, scores, and monitored post-selection quantities. Do not let one generic word such as "error" stand for several different quantities.
3. **Relative-change check:** define the denominator, baseline, monitored quantity, and evaluation subset before reporting a percent change, fold change, ablation response, or normalized diagnostic.
4. **Production-order check:** after reordering subsections, verify figure/table order, filenames, captions, labels, cross-reference ranges, and any compiled layout consequences.

These checks are generic. Do not encode project-specific results, numerical values, model names, or paper-specific findings in this skill.
