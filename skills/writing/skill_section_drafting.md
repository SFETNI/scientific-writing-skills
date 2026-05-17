# Skill: Section Drafting

## Mandate

Assist prose development when the human provides either **(a)** a drafted section for improvement, or **(b)** a structured section plan (argument chain, key findings to present, claim sequence). Never generates scientific content from nothing — the scientific substance always comes from the human.

This skill does not invent results, add claims, infer methodology details, or introduce citations that the human has not provided or authorized. It improves existing prose for clarity, flow, hedging appropriateness, and publisher-style compliance.

## Required inputs

- `@templates/AUTHOR_CONTEXT.md` — target journal, field, `RESULT_FLEXIBILITY`, `TARGET_JOURNAL_FAMILY`
- `@templates/NUMERICAL_REGISTRY.md` — all accepted quantitative claims (read before any numbers are touched)
- `@agent_context/ANTI_AI_WRITING_STYLE.md` — forbidden phrases and AI-writing artifacts to avoid
- One of:
  - `@templates/SECTION_PLAN.md` filled by the human (argument chain, key claims, scope), or
  - The existing drafted section (pasted or referenced by file path)

Optional:
- `@context/target_journal/` — target journal style papers for tone calibration
- `@workflow/skill_style_calibration.md` output (approved style report)

## Acceptance criteria

1. All quantitative values in the output appear in `NUMERICAL_REGISTRY.md`.
2. No claim is introduced that does not appear in the section plan or the existing draft.
3. All hedges are appropriate for the evidence level (results: hedge lightly; interpretations: hedge explicitly; speculation: label as speculation).
4. No AI-writing artifacts from `ANTI_AI_WRITING_STYLE.md` appear in the output.
5. Tense conventions are consistent with the journal style (past tense for results is standard; check calibration report).
6. Each paragraph has a clear topic sentence.
7. The section closes with a sentence that transitions to or motivates the next section.

## Human-in-the-loop checkpoint

The human must provide the section plan or existing draft **before** this skill activates.

After the skill produces output:
- Human reads the full draft or revised section.
- Human confirms that no scientific content was added, changed, or removed without authorization.
- Human runs `skill_revision_quality_gate.md` before the section is accepted.

**No section is accepted without explicit human approval.**

## Fail conditions

Reject the output and restart if:
- A quantitative value appears that is not in `NUMERICAL_REGISTRY.md`.
- A factual claim appears that is not in the section plan or existing draft.
- A citation is added that the human did not provide.
- Forbidden phrases from `ANTI_AI_WRITING_STYLE.md` appear in the output.
- `RESULT_FLEXIBILITY: LOCKED` is set and any figure, table, or number was modified.

## Activation protocol

1. Read `AUTHOR_CONTEXT.md`, `NUMERICAL_REGISTRY.md`, `ANTI_AI_WRITING_STYLE.md`.
2. Read the section plan or existing draft provided by the human.
3. If a style calibration report exists, read it.
4. Ask the human: "What is the main message this section must deliver?" if not stated in the plan.
5. Produce output with inline evidence labels (`RESULT_SUPPORTED`, `INTERPRETATION`, etc.) on each claim.
6. Present the output for human review.
7. Do not proceed to the next section until human approves this one.
