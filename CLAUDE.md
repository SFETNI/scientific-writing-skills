# CLAUDE.md — scientific-redaction-skills

This is a human-in-the-loop quality-control framework for scientific manuscript redaction. Read this file at the start of every session.

## What this framework is

**Not a system that writes papers.** A quality-control framework for manuscripts that already exist. The researcher provides results, figures, section plans, or existing drafts. The agent verifies, calibrates, and improves — never invents scientific content.

## Mandatory Step 0 protocol

Before any drafting or review task in a new session:

1. **Step 0a — Integrity check**: Run `scripts/check_manuscript_integrity.py`. Resolve all hard errors before proceeding.
2. **Step 0b — Read context files**: Read `@templates/AUTHOR_CONTEXT.md`, `@templates/NUMERICAL_REGISTRY.md`, `@agent_context/ANTI_AI_WRITING_STYLE.md`.
3. **Step 0c — Style calibration** (before first drafting session): Run `/srs-calibrate` to read `context/` papers and produce the style calibration report. Human must approve before drafting begins.

## Skill routing

| Task | Primary skill(s) |
|---|---|
| Draft or improve a section | `@skills/writing/skill_section_drafting.md` |
| Check prose quality | `@skills/writing/skill_prose_quality.md` |
| Calibrate claims and numbers | `@skills/writing/skill_claim_calibration.md` |
| Position benchmark papers | `@skills/writing/skill_benchmark_positioning.md` |
| Draft Methods section | `@skills/writing/skill_methods_writing.md` |
| Draft Results section | `@skills/writing/skill_results_writing.md` |
| Draft Supplementary Materials | `@skills/writing/skill_sm_writing.md` |
| Run section acceptance gate | `@skills/writing/skill_revision_quality_gate.md` |
| Map claims to evidence | `@skills/integrity/skill_claim_evidence_verification.md` |
| Audit citations | `@skills/integrity/skill_citation_check.md` |
| Verify full-text support | `@skills/integrity/skill_reference_verification.md` |
| Fill citation gaps | `@skills/integrity/skill_literature_research.md` (requires explicit human authorization) |
| Review figures | `@skills/figures/skill_figure_qc.md` |
| Draft figure captions | `@skills/figures/skill_figure_caption_writing.md` |
| Review table structure | `@skills/figures/skill_table_design.md` |
| Check visual consistency | `@skills/figures/skill_visual_consistency.md` |
| Simulate peer reviewer | `@skills/review/skill_reviewer_perspective.md` |
| Review argument flow | `@skills/review/skill_argument_flow_review.md` |
| Estimate editorial decision | `@skills/review/skill_editorial_decision.md` |
| Calibrate style from context papers | `@skills/workflow/skill_style_calibration.md` |
| Standard task protocol | `@skills/workflow/skill_task_protocol.md` |

Full routing table: `@skills/SKILLS_INDEX.md`

## Core rules

1. **Never generate scientific content from nothing.** Every claim, number, and finding must come from the researcher's results or an accepted citation.
2. **Always confirm before accepting output.** Human must explicitly approve every skill output before it is acted upon.
3. **Never declare a citation "verified" without stating the tier reached.** Use the 4-tier ladder: `KEY_EXISTS` → `METADATA_VERIFIED` → `ABSTRACT_RELEVANT` → `FULL_TEXT_SUPPORTS_CLAIM`.
4. **Every claim must carry an evidence status label**: `RESULT_SUPPORTED`, `LITERATURE_SUPPORTED`, `METHOD_DEFINITION`, `INTERPRETATION`, `SPECULATION`, `UNSUPPORTED`, or `NEEDS_HUMAN_DECISION`.
5. **Read `RESULT_FLEXIBILITY` from `AUTHOR_CONTEXT.md`** before suggesting any changes to figures, tables, or numbers. Respect `LOCKED` / `FIGURES_IMPROVABLE` / `MINOR_ANALYSIS_ALLOWED`.
6. **Never search the web** without explicit human authorization (only `skill_literature_research` and only when explicitly invoked).
7. **End every task** with a process trace following `@skills/workflow/skill_process_trace.md`.

## Human-in-the-loop gates

Four mandatory gates in the workflow — no content is accepted without passing them:
1. **Gate 1 (Pre-draft)**: Hard errors resolved; style parameters confirmed
2. **Gate 2 (Section plan)**: Argument plan approved before any prose is written
3. **Gate 3 (Review)**: Reviewer reports read; human decides what to address vs. rebut
4. **Gate 4 (Final)**: Author certifies all content before submission

Full gate specification: `@docs/HUMAN_IN_THE_LOOP.md`

## Session startup checklist

```
[ ] Read AUTHOR_CONTEXT.md — know the target journal and RESULT_FLEXIBILITY
[ ] Read NUMERICAL_REGISTRY.md — know all accepted quantitative claims
[ ] Read AGENT_HANDOFF.md — know the current phase and active task
[ ] Run /srs-check if any new content was added since last session
```
