# Skill: Prose Quality Review

## Mandate

Review and improve the prose quality of an existing section without changing any scientific content. This skill is a pure writing pass: it improves clarity, concision, sentence structure, transition quality, and paragraph cohesion. It does not evaluate whether claims are correct or supported — that is `skill_claim_calibration.md`.

## Required inputs

- The section text (pasted or referenced by file path)
- `@agent_context/ANTI_AI_WRITING_STYLE.md` — forbidden phrases
- `@templates/AUTHOR_CONTEXT.md` — target journal, hedging level
- Style calibration report (if available from `/srs-calibrate`)

## Acceptance criteria

1. No scientific content (claims, numbers, citations, method names) was changed from the input.
2. No AI-writing artifacts from `ANTI_AI_WRITING_STYLE.md` appear in the output.
3. Sentence length variance is improved (mix of short and longer sentences).
4. Passive/active voice balance matches the journal style (check calibration report).
5. All paragraph-opening topic sentences are clear.
6. Transitions between paragraphs are explicit.
7. No sentences longer than 40 words (flag any that remain for human review).

## Human-in-the-loop checkpoint

Human must confirm:
- No scientific content changed (diff the input and output sections side by side)
- Tone is consistent with the target journal
- No AI-writing artifacts slipped through

## Fail conditions

Reject the output if:
- Any quantitative value differs from the input section.
- Any citation was added, removed, or changed.
- A claim is stronger or weaker than in the original (scope creep or unwarranted hedging).
- Output contains phrases from `ANTI_AI_WRITING_STYLE.md`.

## Notes

This skill is appropriate for a final polish pass. It should not be the first pass on a section — run `skill_claim_calibration.md` first so that the prose being polished is already accurate.
