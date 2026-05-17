# Skill: Visual Consistency Review

## Mandate

Verify that all figures in the manuscript use consistent model labels, colours, notation, and terminology — and that this visual consistency matches the naming conventions in the manuscript text and `STYLE_GUIDE.md`. Inconsistencies create confusion and suggest low manuscript quality to reviewers.

## Required inputs

- All figure files or captions (provided by human)
- `@templates/AUTHOR_CONTEXT.md`
- `STYLE_GUIDE.md` (preferred model/variable names, abbreviations)

## Consistency checks

### Naming consistency
- [ ] All model/method names are the same across all figures and in the text
- [ ] Abbreviations are consistent (e.g., "GBR" or "gradient boosting regressor" — not both)
- [ ] Variable names on axes match the variable names in the Methods section

### Colour and style consistency
- [ ] The same model/condition uses the same colour across all figures
- [ ] Line styles are consistent (solid for model A, dashed for model B — same across all plots)
- [ ] Marker shapes are consistent for the same data series

### Notation consistency
- [ ] Units are expressed consistently (e.g., "W m⁻¹ K⁻¹" not "W/m/K" in some figures)
- [ ] Uncertainty notation is consistent (± in all, or CI in all — not mixed)
- [ ] Subscripts and superscripts are formatted consistently

### Cross-reference consistency
- [ ] Figure numbers in the manuscript text match the figure file order
- [ ] Panel labels (A, B, C) are referenced correctly in the caption and text

## Acceptance criteria

1. No naming inconsistency between figures and manuscript text.
2. Colour palette is consistent across all figures for the same model/condition.
3. Units and notation are uniform across the manuscript.

## Human-in-the-loop checkpoint

Human must:
- Confirm the canonical naming from `STYLE_GUIDE.md` and approve any corrections
- Verify that proposed colour/style corrections would not conflict with the source figure files
- Flag any figure that requires regeneration (out of scope for this skill — Codex handles it)

## Fail conditions

- The same model is called by two different names in different figures.
- Colour assignments are inconsistent (Model A is blue in Figure 1 but red in Figure 3).
- Unit notation differs between figures showing the same quantity.

## Output format

```
VISUAL CONSISTENCY REPORT — [Date]

Naming inconsistencies:
  Figure 2: "GBR" / Figure 4: "gradient boosting" — should be "GBR" (per STYLE_GUIDE)

Colour inconsistencies:
  Model A: blue (Fig 1, Fig 3) / red (Fig 4) — standardize to blue

Notation inconsistencies:
  Thermal conductivity: "W/m/K" (Fig 1) vs "W m⁻¹ K⁻¹" (Fig 3) — use SI notation throughout

Figure–text cross-reference:
  [PASS] All figure numbers referenced correctly

ITEMS REQUIRING HUMAN DECISION: [N]
```
