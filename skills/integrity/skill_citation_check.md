# Skill: Citation Check

## Mandate

Advance each reference cited in the manuscript up the citation verification ladder. Report the tier reached for every reference. Never declare any reference "verified" without stating which tier was reached. The goal is to ensure that no citation in the final manuscript is at `KEY_EXISTS` tier only.

## Required inputs

- The manuscript `.tex` file(s) (or list of all `\cite{key}` entries extracted from them)
- The `.bib` file
- `@templates/CLAIM_REGISTER.md` — to identify which claims each citation supports

## Citation verification ladder

| Tier | Meaning | Who confirms |
|---|---|---|
| `KEY_EXISTS` | Citation key is present in the `.bib` file | Script |
| `METADATA_VERIFIED` | Author, year, title, journal/venue are complete and internally consistent | Script + agent |
| `ABSTRACT_RELEVANT` | Abstract confirms the paper is relevant to the claim being made | Agent (with human review) |
| `FULL_TEXT_SUPPORTS_CLAIM` | Full text was read and confirms the specific claim | Human |
| `DOES_NOT_SUPPORT_CLAIM` | Full text does not support the claim as written | Agent flags; human decides |
| `NEEDS_REPLACEMENT` | Reference must be replaced before submission | Human |

The ladder is not binary. A citation at `ABSTRACT_RELEVANT` is better than one at `KEY_EXISTS`, but it is not the same as one confirmed by full text. Skills must always report the tier.

## Acceptance criteria

1. All `\cite{key}` entries appear in the `.bib` file (`KEY_EXISTS` confirmed for all).
2. All `.bib` entries used in the manuscript have complete metadata (`METADATA_VERIFIED`).
3. All critical citations (those supporting primary claims) have reached `ABSTRACT_RELEVANT` or higher.
4. No citation key is described as "verified" without a tier label.
5. All citations at `KEY_EXISTS` only are flagged for human follow-up.

## Human-in-the-loop checkpoint

Human receives the citation audit report and must:
- Read abstracts for citations at `KEY_EXISTS` or `METADATA_VERIFIED` tier and advance them to `ABSTRACT_RELEVANT` where possible
- Confirm or deny `FULL_TEXT_SUPPORTS_CLAIM` for all critical citations
- Resolve all `NEEDS_REPLACEMENT` items

## Fail conditions

- Any citation declared "verified" without a tier label.
- A critical claim supported only by a citation at `KEY_EXISTS` tier.
- Missing `.bib` entries for any cited key.

## Output format

```
CITATION AUDIT REPORT — [Section / Full Manuscript] — [Date]

Total citations found: [N]

KEY_EXISTS only (action required):
  - Smith2024: key exists; metadata incomplete — missing journal name
  - Doe2023:   key exists; metadata complete; abstract not confirmed

METADATA_VERIFIED (abstract check recommended):
  - Jones2022:  Author, year, title, journal complete
  - Lee2021:    Author, year, title, venue complete

ABSTRACT_RELEVANT (full text recommended for primary claims):
  - Chen2023:   Abstract confirms relevance to claim "..."
  - Wang2024:   Abstract confirms relevance to claim "..."

FULL_TEXT_SUPPORTS_CLAIM:
  - [none confirmed in this pass — human to confirm]

DOES_NOT_SUPPORT_CLAIM:
  - Taylor2022: abstract discusses X, but claim in §3.2 asserts Y — review required

NEEDS_REPLACEMENT: [none]

SUMMARY: [N] citations, [N] below ABSTRACT_RELEVANT — ACTION REQUIRED
```
