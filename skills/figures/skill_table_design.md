# Skill: Table Design Review

## Mandate

Assess table structure for clarity, column design, and appropriate content scope. Flag tables that mix data with interpretation, that have redundant columns, or that violate journal formatting conventions. Produce a restructuring recommendation for human approval.

## Required inputs

- Table content (provided by human)
- `@templates/NUMERICAL_REGISTRY.md` — to verify values
- `@templates/AUTHOR_CONTEXT.md` — target journal table conventions

## Table design checklist

### Structure
- [ ] Each column has a clear, unique purpose
- [ ] Column headers include units
- [ ] No duplicate information across columns
- [ ] Rows represent a consistent unit (one row = one observation, one model, one condition)

### Content scope
- [ ] Data values are in the table; interpretation is in the caption or text (not in a "Notes" column unless clearly labeled)
- [ ] Uncertainty values (± or confidence intervals) are present for all primary metrics
- [ ] Significant figures are consistent within each column
- [ ] Missing values are explicitly marked (e.g., "—" not left blank)

### Formatting
- [ ] No vertical lines (most journals prefer horizontal rules only)
- [ ] Font size ≥ 8pt
- [ ] Table fits within journal column or page width
- [ ] Footnotes are used for definitions, not for data

### Registry check
- [ ] All primary numerical values in the table appear in `NUMERICAL_REGISTRY.md`

## Acceptance criteria

1. All numerical values are in `NUMERICAL_REGISTRY.md`.
2. No interpretation appears in the table cells (belongs in caption or discussion).
3. Column headers include units.
4. Uncertainty values are present for all primary metrics.

## Human-in-the-loop checkpoint

Human must:
- Approve any proposed restructuring before implementation
- Verify all numbers against registered values
- Confirm that the table scope is complete (no missing conditions or models)

## Common table problems to flag

- **Redundant columns**: "Score" and "Score (%)" both in the same table
- **Interpretation in cells**: "Best result (outperforms baseline)" — move to caption
- **Missing uncertainty**: reporting a mean without SD or CI
- **Inconsistent precision**: one column shows "0.847" and another shows "84.7% ± 3.1%"
- **Orphan table**: a table not referenced in the Results text
