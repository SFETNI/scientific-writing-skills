# context/ — Reference Materials for Style Calibration

Place `.md` extracts of your reference papers here before running `/srs-calibrate`. The style calibration subagent reads these files to understand the voice, hedging level, claim density, and terminology conventions of your target journal.

---

## Subdirectory structure

| Subdirectory | What to put here |
|---|---|
| `target_journal/` | 3–5 papers from your target journal — recent publications in your field |
| `group_papers/` | Your group's published papers — helps calibrate group-specific terminology |
| `reference_papers/` | Key benchmark or background papers cited in your manuscript |

---

## How to convert PDFs to .md

v0.1 requires manual conversion. `scripts/pdf_to_context.py` (automated extraction) is planned for v0.2.

**Manual workflow:**

1. Open the paper PDF.
2. Copy the text of the sections you want to calibrate from (Introduction, Methods, Results, Discussion — not the abstract alone).
3. Paste into a new `.md` file in the appropriate subdirectory.
4. Add a header at the top of the file:

```markdown
# [Author, Year] [Paper title]
# Source: [journal name, DOI or URL]
# Sections included: Introduction, Methods, Discussion
# Notes: [any relevant notes about this paper's style]
```

5. Save with a descriptive filename: `Smith2024_polymer_composites.md`

**Tips:**
- Focus on extracting the text of Results and Discussion sections — these drive style calibration most strongly.
- Remove tables, figure captions, and bibliography from the extracted text (they distort phrase analysis).
- 3–5 papers per subdirectory is sufficient for a good calibration.

---

## Privacy note

Do not place full PDF files or copyrighted text here. Extract the portions you need, use them for calibration, and keep the extracted text within your manuscript project. Do not commit extracted journal text to a public repository.

---

## If context/ is empty

Running `/srs-calibrate` with an empty `context/` directory will produce a family-defaults report based on `TARGET_JOURNAL_FAMILY` in `AUTHOR_CONTEXT.md`. The style calibration subagent will label this report clearly as "based on journal family defaults only — no papers read." It is less precise than calibration from actual papers but is better than no calibration.
