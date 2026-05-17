# Skill: Claim Calibration

## Mandate

Verify that every quantitative and qualitative claim in a section is supported by the registered results or an accepted citation, and that each claim is appropriately hedged for its evidence level. Output a claim-source map with evidence status labels. Do not change the text — report findings for human review.

## Required inputs

- The section text (pasted or referenced)
- `@templates/NUMERICAL_REGISTRY.md` — all accepted quantitative claims with source paths
- `@templates/CLAIM_REGISTER.md` — existing claim–evidence mappings (if populated)
- `@templates/AUTHOR_CONTEXT.md` — RESULT_FLEXIBILITY parameter

## Evidence status labels (required on every claim)

Every claim in the output map must carry exactly one label:

| Label | Meaning |
|---|---|
| `RESULT_SUPPORTED` | Directly supported by a figure, table, or number in the accepted results |
| `LITERATURE_SUPPORTED` | Supported by a citation whose full text was read and confirmed |
| `METHOD_DEFINITION` | Definitional statement of the methodology |
| `INTERPRETATION` | Plausible interpretation of results; requires hedging in text |
| `SPECULATION` | Goes beyond the evidence; must be labeled as speculation in the text |
| `UNSUPPORTED` | No supporting evidence found; must be removed or replaced |
| `NEEDS_HUMAN_DECISION` | Ambiguous; agent cannot classify without human judgment |

## Acceptance criteria

1. Every quantitative value in the section is present in `NUMERICAL_REGISTRY.md`.
2. Every claim is assigned one of the seven evidence status labels.
3. No `UNSUPPORTED` claim remains in the accepted section.
4. All `INTERPRETATION` claims use hedging language (e.g., "suggests," "is consistent with," "may indicate").
5. All `SPECULATION` claims are explicitly labeled as speculation in the text.
6. No `NEEDS_HUMAN_DECISION` item is left unresolved before section acceptance.

## Human-in-the-loop checkpoint

Human receives the claim-source map and must:
- Verify `RESULT_SUPPORTED` claims against their registered source artifact
- Confirm hedging level on all `INTERPRETATION` claims
- Decide on every `NEEDS_HUMAN_DECISION` and `UNSUPPORTED` item
- Update `CLAIM_REGISTER.md` with resolved mappings

No section is accepted with unresolved `UNSUPPORTED` or `NEEDS_HUMAN_DECISION` items.

## Fail conditions

Reject the output if:
- A quantitative value appears that is not in `NUMERICAL_REGISTRY.md`.
- Any `UNSUPPORTED` claim is left in the output without a flag.
- Evidence labels are missing from any claim in the map.
- The output proposes changes to numbers (this skill only reports; it does not edit).

## Output format

For each paragraph, produce:

```
Paragraph [N]: "[Opening sentence fragment...]"
  Claim 1: "[exact claim text]" — RESULT_SUPPORTED — source: NUMERICAL_REGISTRY row 12
  Claim 2: "[exact claim text]" — INTERPRETATION — hedging: "suggests" present ✓
  Claim 3: "[exact claim text]" — UNSUPPORTED — ACTION REQUIRED: provide source or remove
```

Total: [N] claims audited, [N] RESULT_SUPPORTED, [N] LITERATURE_SUPPORTED, [N] INTERPRETATION, [N] UNSUPPORTED, [N] NEEDS_HUMAN_DECISION
