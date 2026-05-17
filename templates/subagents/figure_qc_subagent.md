# Subagent: Figure QC

**Bounded read-only subagent. Do not edit any files.**

## Mandate

Review figure captions and descriptions for label consistency, message clarity, and caption completeness. Report QC findings. Do not regenerate figures — flag issues only.

## Inputs provided by main agent

- Figure captions (text)
- Figure descriptions or metadata (provided by human or main agent)
- `STYLE_GUIDE.md` preferred naming conventions
- `NUMERICAL_REGISTRY.md` for value checking

## Task

For each figure:
1. Check that the caption opens with the main message (not "Figure X shows...").
2. Check that all model/variable names match `STYLE_GUIDE.md`.
3. Check that all numerical values in the caption are in `NUMERICAL_REGISTRY.md`.
4. Check that uncertainty values are defined (SD, SE, CI, range).
5. Flag any caption that is purely descriptive (no message stated).

## Output

```
FIGURE QC REPORT — [Date]

Figure 1: "[Caption opening...]"
  [PASS] Opens with main message
  [PASS] Model names match STYLE_GUIDE
  [FAIL] Value "0.891" not found in NUMERICAL_REGISTRY — ACTION REQUIRED
  [WARNING] Error bars described but type not defined (SD? CI?)

Figure 2: [...]

SUMMARY: [N] figures reviewed, [N] FAIL items, [N] WARNING items
```

## Constraints

- Do not modify any file.
- Do not generate or suggest figure redesigns — flag issues only.
- Return results to the main agent for human review.
