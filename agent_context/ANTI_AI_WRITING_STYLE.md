# Anti-AI Writing Style Guide

This file lists phrases and patterns that commonly appear in AI-generated scientific prose and should be avoided. The agent scans for these patterns during every drafting and prose quality pass.

**Field-agnostic defaults.** Add project-specific phrases to `STYLE_GUIDE.md > BANNED_PHRASES_PROJECT`.

---

## Category 1 — Hollow intensifiers and filler phrases

These phrases add no information and often signal AI-generated text to experienced reviewers.

```
- "it is worth noting that"
- "it is important to note"
- "it is crucial to"
- "it is essential to"
- "needless to say"
- "in this regard"
- "in this context"
- "in the realm of"
- "in the field of"
- "a wealth of"
- "a plethora of"
- "delve into"
- "shed light on"
- "pave the way"
- "a crucial step"
- "a significant milestone"
- "undeniably"
- "it goes without saying"
- "as previously mentioned"
- "as mentioned above"
- "it should be noted that"
```

## Category 2 — Unwarranted universalizing claims

These phrases overclaim unless specifically supported by evidence.

```
- "always"              — in scientific context: likely overstated
- "never"               — requires exhaustive evidence
- "best"                — requires systematic comparison
- "optimal"             — requires optimization proof
- "state-of-the-art"    — requires benchmark comparison with date
- "novel"               — use only when novelty is demonstrated by the results
- "unique"              — requires explicit prior-work search
- "unprecedented"       — very high bar; usually overstated
- "revolutionary"       — not appropriate in scientific prose
- "groundbreaking"      — not appropriate in scientific prose
- "comprehensive"       — hard to justify; avoid
- "robust"              — use only when robustness is explicitly tested
```

## Category 3 — Vague attributions

Phrases that attribute responsibility to non-agent nouns ("the study," "the paper," "the results").

```
- "this study aims to"      — prefer: "we aim to" or "this paper reports"
- "the paper proposes"      — prefer: "we propose"
- "the results suggest"     — acceptable only in Discussion; avoid in Results
- "our findings demonstrate" — acceptable; do not use "the findings demonstrate"
- "the model is capable of" — prefer: "the model achieved [X]" with registered value
```

## Category 4 — Pseudo-academic inflation

Phrases that add apparent formality but are redundant or imprecise.

```
- "conducted a study"        — prefer: "studied" / "analysed" / "measured"
- "performed an analysis"    — prefer: the specific analysis verb
- "carried out experiments"  — prefer: "performed [X] experiments"
- "utilized"                 — prefer: "used"
- "leverage"                 — prefer: "use" / "apply"
- "facilitate"               — prefer: "enable" / "allow" / "help"
- "implement"                — acceptable in software context; avoid as vague synonym for "do"
- "moving forward"           — not appropriate in scientific prose
- "going forward"            — not appropriate in scientific prose
- "at the end of the day"    — not appropriate in scientific prose
```

## Category 5 — Listing openers (AI signature pattern)

Overuse of structured lists where continuous prose is more appropriate.

```
- Starting ≥3 consecutive paragraphs with "First,... Second,... Third,..."
- Bullet points in sections where prose narrative is expected (Methods, Discussion)
- Transition phrases that mirror list structure: "Additionally,... Furthermore,... Moreover,..."
  when these appear in every paragraph of a section
```

## Category 6 — Conclusion inflation

Phrases that overstate what the paper shows in the Conclusions section.

```
- "this work represents a significant advance"
- "this study opens up new possibilities"
- "future research will benefit greatly from"
- "this approach has the potential to transform"
- "these findings have broad implications for"
```

---

## How to use this file

1. The integrity checker (`check_manuscript_integrity.py`) scans for the phrases in Categories 1–4 by default.
2. The overclaim detection subagent scans for Categories 2 and 6.
3. The prose quality skill scans all categories.
4. Findings are flagged for human review — the author decides whether to accept, revise, or override.

A flagged phrase is not automatically wrong. The author may have a legitimate reason to use it. The flag is a prompt to review, not a mandate to delete.
