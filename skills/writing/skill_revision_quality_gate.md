# Skill: Revision Quality Gate

## Mandate

Run the acceptance checklist for a completed section before it is marked as accepted. This is the final QC pass before the section is locked. The gate checks claim calibration, numerical discipline, prose quality, and policy compliance. No section is accepted without passing this gate.

## Required inputs

- The completed section text
- `@templates/NUMERICAL_REGISTRY.md`
- `@templates/CLAIM_REGISTER.md`
- `@agent_context/ANTI_AI_WRITING_STYLE.md`
- `@templates/AUTHOR_CONTEXT.md`

## Gate checklist

Run each check and report PASS / FAIL / WARNING:

### Claim discipline
- [ ] All quantitative values match `NUMERICAL_REGISTRY.md` — no unregistered numbers
- [ ] All claims are assigned an evidence status label
- [ ] No `UNSUPPORTED` claims remain
- [ ] No `NEEDS_HUMAN_DECISION` items remain unresolved
- [ ] Interpretations are hedged; speculation is labeled as speculation

### Citation discipline
- [ ] All `\cite{}` keys exist in the `.bib` file
- [ ] No citation key is used without at least `METADATA_VERIFIED` tier reached
- [ ] Critical claims have citations at `ABSTRACT_RELEVANT` tier or higher

### Prose quality
- [ ] No AI-writing artifacts from `ANTI_AI_WRITING_STYLE.md`
- [ ] No sentences longer than 40 words (or flagged for human review)
- [ ] Each paragraph has a clear topic sentence
- [ ] Section closes with a transition to the next section

### Registry consistency
- [ ] `CLAIM_REGISTER.md` updated with all new claim-source mappings from this section
- [ ] `NUMERICAL_REGISTRY.md` entries referenced in this section are all marked "used in: [section name]"

### Policy compliance (check `AUTHOR_CONTEXT.md TARGET_JOURNAL_FAMILY`)
- [ ] No verbatim text from published papers
- [ ] AI use will be disclosed in the final manuscript (log this section as AI-assisted)
- [ ] No prohibited AI-generated content (images, generated data) present

## Human-in-the-loop checkpoint

Human must:
- Review the full gate report before accepting the section
- Sign off explicitly: "Section [name] accepted at [date]"
- Record the acceptance in `AGENT_HANDOFF.md`

No section is accepted without human sign-off on the gate report.

## Fail conditions (immediate rejection)

- Any unregistered quantitative value (FAIL — do not accept)
- Any `UNSUPPORTED` claim (FAIL — do not accept)
- Any AI-writing artifact (FAIL — prose quality pass required first)
- Missing citation tier for any critical claim (FAIL — citation check required)

## Output format

```
=== REVISION QUALITY GATE — [Section Name] ===

CLAIM DISCIPLINE
  [PASS] All quantitative values in NUMERICAL_REGISTRY
  [FAIL] Claim "..." is UNSUPPORTED — no source found — ACTION REQUIRED
  [PASS] All interpretations hedged
  ...

CITATION DISCIPLINE
  [PASS] All keys exist in .bib
  [WARNING] Citation Smith2024 at KEY_EXISTS tier only — full text not confirmed
  ...

PROSE QUALITY
  [PASS] No AI artifacts
  [WARNING] Sentence in para 3 is 44 words — review recommended
  ...

REGISTRY CONSISTENCY
  [PASS] CLAIM_REGISTER updated
  ...

POLICY COMPLIANCE
  [PASS] No verbatim journal text
  [PASS] AI use logged
  ...

GATE RESULT: [PASS / CONDITIONAL PASS / FAIL]
CONDITIONAL PASS items requiring human action: [list]
```
