# Skill: Reference Verification

## Mandate

For citations already confirmed at `ABSTRACT_RELEVANT` tier by `skill_citation_check.md`, attempt to advance them to `FULL_TEXT_SUPPORTS_CLAIM` by reading available full text, or flag them as `DOES_NOT_SUPPORT_CLAIM` or `NEEDS_REPLACEMENT`. The human makes all final decisions. This skill does not search the web — it reads text the human provides.

## Required inputs

- Citation audit report from `skill_citation_check.md` (list of `ABSTRACT_RELEVANT` items to verify)
- Full text of the papers to verify (human provides PDF text, DOI links, or copied excerpts)
- The specific claim each citation is intended to support (from `CLAIM_REGISTER.md`)
- `@templates/CLAIM_REGISTER.md`

## Verification protocol

For each citation provided:
1. Read the abstract and relevant sections of the full text.
2. Identify the passage(s) that most directly support the claim being made.
3. Classify the citation as one of:
   - `FULL_TEXT_SUPPORTS_CLAIM` — with the supporting passage quoted
   - `PARTIAL_SUPPORT` — the text is related but does not directly support the specific claim
   - `DOES_NOT_SUPPORT_CLAIM` — the text is about something different, or contradicts the claim
   - `NEEDS_REPLACEMENT` — the citation should be replaced with a more appropriate reference

## Acceptance criteria

1. Every citation in the report has a final tier classification.
2. For `FULL_TEXT_SUPPORTS_CLAIM`: a supporting passage is quoted.
3. For `DOES_NOT_SUPPORT_CLAIM` and `NEEDS_REPLACEMENT`: the reason is stated.
4. `CLAIM_REGISTER.md` is updated with the verified tier after human review.

## Human-in-the-loop checkpoint

Human must:
- Confirm `FULL_TEXT_SUPPORTS_CLAIM` by reading the passage themselves (the agent extracts; the human confirms)
- Decide what to do with every `DOES_NOT_SUPPORT_CLAIM` (remove citation, adjust claim, find replacement)
- Authorise every `NEEDS_REPLACEMENT` (agent suggests alternatives only if human explicitly requests a web search)

**The agent cannot independently conclude that a citation supports a claim. The human reads and confirms.**

## Fail conditions

- Output assigns `FULL_TEXT_SUPPORTS_CLAIM` without quoting a specific supporting passage.
- A `NEEDS_REPLACEMENT` item is left without an action plan.
- The skill runs a web search without explicit human authorization.

## Output format

```
REFERENCE VERIFICATION REPORT — [Date]
Citations provided for full-text verification: [N]

Smith2024 — Claim: "X has been shown to improve Y by Z%"
  Tier reached: FULL_TEXT_SUPPORTS_CLAIM
  Supporting passage (§2.3, p.4): "[exact quoted text]"
  Human confirmation required: YES — please confirm you have read this passage

Doe2023 — Claim: "Y is typically limited by..."
  Tier reached: DOES_NOT_SUPPORT_CLAIM
  Reason: Paper discusses Z, not Y; the stated limitation is not supported by this reference
  Recommended action: Remove citation or find a source that directly addresses Y

Jones2022 — Claim: "..."
  Tier reached: PARTIAL_SUPPORT
  Note: Paper discusses a related concept but in a different experimental context
  Recommended action: Human to decide whether partial support is sufficient or replacement needed

SUMMARY
  FULL_TEXT_SUPPORTS_CLAIM:  [N]
  PARTIAL_SUPPORT:           [N]
  DOES_NOT_SUPPORT_CLAIM:    [N] ← requires human action
  NEEDS_REPLACEMENT:         [N] ← requires human action
```
