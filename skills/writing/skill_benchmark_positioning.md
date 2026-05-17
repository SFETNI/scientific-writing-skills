# Skill: Benchmark Positioning

## Mandate

Ensure that benchmark, baseline, and state-of-the-art references in the Introduction and Discussion are positioned as methodological context — not as competitors to be defeated. This skill flags overclaiming comparisons and suggests reframings that are accurate, honest, and consistent with the target journal's citation norms.

Benchmarks are papers or methods that the author builds upon, validates against, or contextualises. They are not opponents in a competition. The manuscript should position them as enabling prior work, not as obstacles overcome.

## Required inputs

- The Introduction or Discussion section text
- `@templates/AUTHOR_CONTEXT.md` — contribution level, target journal
- `@templates/CLAIM_REGISTER.md` — claim–citation mappings
- List of benchmark/baseline paper keys (provided by human)

## Acceptance criteria

1. No benchmark is introduced with language implying the author's work "defeats," "outperforms," or "solves" the benchmark's limitations (unless explicitly supported by a registered result).
2. All comparisons use registered quantitative values from `NUMERICAL_REGISTRY.md`.
3. The framing of each benchmark reference clearly states:
   - What methodological or scientific contribution the benchmark made
   - How this manuscript builds on, extends, or differs from it
4. Hedging language is appropriate: observed performance differences are stated, not universalized.
5. The Introduction closes with a clear statement of the manuscript's specific contribution.

## Human-in-the-loop checkpoint

Human confirms:
- The framing of each benchmark reflects what the cited paper actually did (human must check)
- Comparative performance claims are registered in `NUMERICAL_REGISTRY.md`
- The contribution statement is accurate and not overstated

## Fail conditions

Reject the output if:
- A performance comparison claims superiority without a registered numerical result.
- A benchmark paper is described in a way that misrepresents what it actually contributed.
- "We show that [method X] fails to..." type framing without supporting evidence.

## Common overclaiming patterns to flag

- "X suffers from Y limitation, which we overcome" — acceptable only with evidence
- "Unlike X, our method can..." — check if this is a registered result or speculative
- "X cannot handle..." — claims about what prior work cannot do need citation or evidence
- "State-of-the-art methods fail to..." — requires specific evidence
- "We achieve the best reported..." — requires systematic comparison across all relevant work
