# Skill: Figure Quality Control

## Mandate

Assess each figure for readability, label consistency, message clarity, and conformance with the target journal's figure requirements. Produce a QC report with specific actionable items. This skill does not modify figures — it produces a report for human review.

## Required inputs

- Figure files (or descriptions/captions provided by human)
- Figure captions (existing or draft)
- `@templates/AUTHOR_CONTEXT.md` — target journal figure requirements
- `@templates/NUMERICAL_REGISTRY.md` — to verify values visible in figures

## Quality checks

For each figure:

### Readability
- [ ] Font size ≥ 8pt for all labels and tick marks (minimum for print; journal may require 10pt)
- [ ] Line thickness sufficient for print reproduction
- [ ] Colour palette distinguishable in greyscale and by colour-blind readers
- [ ] No overlapping labels or tick marks

### Label and notation consistency
- [ ] Axis labels match the model/variable naming in `STYLE_GUIDE.md`
- [ ] Units are present on all axes
- [ ] Legend entries match the naming used in the manuscript text
- [ ] Figure title or caption panel label is consistent with the numbering in main text

### Message clarity
- [ ] The figure's main message is discernible within 5 seconds
- [ ] No unnecessary visual elements (chartjunk)
- [ ] Error bars or uncertainty regions are present where required by the data type
- [ ] The caption states the main message (not just what was plotted)

### Journal compliance
- [ ] Figure dimensions match journal requirements (check `AUTHOR_CONTEXT.md TARGET_JOURNAL_FAMILY`)
- [ ] File format is acceptable (typically EPS, PDF, TIFF, or PNG at specified DPI)
- [ ] Colour mode is correct (RGB for online, CMYK for print if required)

### Integration and production readiness
- [ ] Active figure filenames match the manuscript figure numbers or the documented journal naming convention
- [ ] The figure number, caption, LaTeX label, source plan, and output manifest all agree
- [ ] Reordered figures do not leave stale filenames, captions, cross-reference ranges, or manifest rows
- [ ] Large figures do not create avoidable figure-only pages in the compiled draft unless the journal requires full-page presentation
- [ ] The compiled PDF was visually spot-checked after resizing, renaming, or changing float placement

## Acceptance criteria

1. All readability checks pass.
2. All labels are consistent with `STYLE_GUIDE.md`.
3. Caption states the main message.
4. Journal dimension/format requirements met.
5. Figure filenames, manuscript numbering, labels, captions, and output manifests are internally consistent.
6. The compiled layout has been checked for avoidable float-only pages, excessive white space, or figures detached from their callout text.

## Human-in-the-loop checkpoint