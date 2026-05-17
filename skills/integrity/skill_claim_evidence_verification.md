# Skill: Claim–Evidence Verification

## Mandate

Map every substantive claim in a section to a source artifact (figure, table, registered number, or citation). Produce a claim map that shows each claim's evidence status. Flag items that are unsupported or require human decision. This skill does not edit the text — it only produces the map for human review.

## Required inputs

- The section text (pasted or referenced)
- `@templates/NUMERICAL_REGISTRY.md`
- `@templates/CLAIM_REGISTER.md`
- List of accepted figures and tables (provided by human or from figure plan)

## Evidence status labels

| Label | When to use |
|---|---|
| `RESULT_SUPPORTED` | Claim directly matches a number or finding in `NUMERICAL_REGISTRY.md` or an accepted figure |
| `LITERATURE_SUPPORTED` | Claim is supported by a citation confirmed at `ABSTRACT_RELEVANT` tier or higher |
| `METHOD_DEFINITION` | Claim is a definitional statement of the methodology |
| `INTERPRETATION` | Plausible interpretation; hedging present |
| `SPECULATION` | Goes beyond the data; must be flagged in text |
| `UNSUPPORTED` | No source found — must be removed or replaced |
| `NEEDS_HUMAN_DECISION` | Ambiguous — agent cannot classify |

## Acceptance criteria

1. Every claim in the section has a label.
2. Every `RESULT_SUPPORTED` claim is linked to a specific `NUMERICAL_REGISTRY.md` row or figure.
3. Every `LITERATURE_SUPPORTED` claim is linked to a citation key at `ABSTRACT_RELEVANT` tier or higher.
4. No `UNSUPPORTED` items remain unresolved in the accepted section.
5. The `CLAIM_REGISTER.md` is updated with all new mappings after human review.

## Human-in-the-loop checkpoint

Human receives the claim map and must:
- Verify each `RESULT_SUPPORTED` mapping against the actual source artifact
- Provide sources for `UNSUPPORTED` items or confirm they must be removed
- Resolve all `NEEDS_HUMAN_DECISION` items
- Update `CLAIM_REGISTER.md`

## Fail conditions

- Output contains a `RESULT_SUPPORTED` claim that links to no registry entry.
- `UNSUPPORTED` items are presented without a clear `ACTION REQUIRED` flag.
- The claim map covers fewer claims than are present in the section text.

## Output format

```
CLAIM–EVIDENCE MAP — [Section] — [Date]

Paragraph 1: "[Opening..."]
  1.1 "[Claim text]" — RESULT_SUPPORTED — NUMERICAL_REGISTRY row 4: R² = 0.847
  1.2 "[Claim text]" — METHOD_DEFINITION — procedure stated in Methods §2.3
  1.3 "[Claim text]" — UNSUPPORTED — ACTION REQUIRED: no source found

Paragraph 2: [...]

SUMMARY
  RESULT_SUPPORTED:      [N]
  LITERATURE_SUPPORTED:  [N]
  METHOD_DEFINITION:     [N]
  INTERPRETATION:        [N]
  SPECULATION:           [N]
  UNSUPPORTED:           [N] ← must be zero before section is accepted
  NEEDS_HUMAN_DECISION:  [N] ← must be zero before section is accepted
```
