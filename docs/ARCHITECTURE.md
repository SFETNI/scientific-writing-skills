# Architecture

## Pipeline overview

The framework organises manuscript preparation into five phases with four mandatory human gates.

```
RESEARCHER RESULTS          CONTEXT DOCUMENTS
(figures, tables, numbers)  (target journal papers, group papers)
        │                            │
        └──────────────┬─────────────┘
                       ▼
        ┌─────────────────────────────┐
        │  Phase 0 — Pre-draft        │
        │  /srs-check  /srs-calibrate │
        │  Integrity check            │
        │  Style calibration          │
        └──────────────┬──────────────┘
                       │
               [Human Gate 1]
               Resolve hard errors
               Approve style parameters
                       │
                       ▼
        ┌─────────────────────────────┐
        │  Section Plan               │
        │  Argument chain per section │
        │  (human-authored)           │
        └──────────────┬──────────────┘
                       │
               [Human Gate 2]
               Approve argument plan
               (no prose before this)
                       │
                       ▼
        ┌─────────────────────────────────────────────────┐
        │  Phase 2 — Section Drafting                     │
        │  /srs-intro  /srs-methods  /srs-results         │
        │  /srs-discussion  /srs-figures  /srs-sm         │
        └──────────────┬──────────────────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────────────────┐
        │  Phase 3 — Review Subagents (parallel)          │
        │  Citation audit  Figure QC                      │
        │  Reviewer simulation (4 roles)                  │
        │  Argument flow review                           │
        └──────────────┬──────────────────────────────────┘
                       │
               [Human Gate 3]
               Read all review reports
               Decide what to address vs. rebut
                       │
                       ▼
        ┌─────────────────────────────┐
        │  Phase 4 — Final QC         │
        │  /srs-gate                  │
        │  Revision quality gate      │
        │  Policy checklist           │
        └──────────────┬──────────────┘
                       │
               [Human Gate 4]
               Author certifies all content
                       │
                       ▼
        SUBMISSION-READY MANUSCRIPT
        Claim-calibrated · Integrity-verified · Publisher-compliant
```

---

## Skill–stage matrix

| Stage | Writing | Integrity | Figures | Review | Workflow |
|---|---|---|---|---|---|
| Pre-draft | — | `skill_citation_check` | — | — | `skill_style_calibration` |
| Section plan | `skill_section_drafting` | `skill_claim_evidence_verification` | — | `skill_argument_flow_review` | `skill_human_checkpoints` |
| Drafting | `skill_prose_quality`, `skill_claim_calibration`, `skill_benchmark_positioning`, `skill_methods_writing`, `skill_results_writing`, `skill_sm_writing` | `skill_citation_check`, `skill_reference_verification` | `skill_figure_qc`, `skill_figure_caption_writing`, `skill_table_design`, `skill_visual_consistency` | — | `skill_task_protocol`, `skill_process_trace` |
| Review | — | `skill_reference_verification` | — | `skill_reviewer_perspective`, `skill_editorial_decision` | — |
| Final QC | `skill_revision_quality_gate` | `skill_citation_check` | `skill_visual_consistency` | — | `skill_human_checkpoints` |

---

## Agent roles and responsibilities

| Agent | Responsibility | Must NOT do |
|---|---|---|
| **Claude (main)** | Prose, claim calibration, argument logic, reviewer simulation, HiTL management | File operations, LaTeX compilation, web search (without auth) |
| **Codex** | Batch file ops, LaTeX compilation, bibliography maintenance, format conversion | Scientific prose, claim evaluation, certifying sections |
| **Claude Subagents** | Bounded read-only reviews (citation audit, figure QC, overclaim detection, reviewer simulation, argument flow, style calibration) | Modifying files, web search, deciding what to address |

---

## File dependencies

```
AUTHOR_CONTEXT.md ──────────→ all skills (read at startup)
NUMERICAL_REGISTRY.md ──────→ skill_claim_calibration, skill_results_writing, all integrity skills
STYLE_GUIDE.md ─────────────→ skill_section_drafting, skill_prose_quality, skill_visual_consistency
CLAIM_REGISTER.md ──────────→ skill_citation_check, skill_reference_verification, skill_revision_quality_gate
SECTION_PLAN.md ────────────→ skill_section_drafting (each section has its own plan)
AGENT_HANDOFF.md ───────────→ read at startup; written at end of every session
context/ ───────────────────→ skill_style_calibration (read-only)
.bib file ──────────────────→ skill_citation_check, check_manuscript_integrity.py
manuscript/*.tex ───────────→ check_manuscript_integrity.py
```

---

## Relationship to academic-research-skills (ARS)

| Dimension | ARS | scientific-redaction-skills |
|---|---|---|
| Entry point | Literature discovery | Results complete |
| Primary function | Full research pipeline | Manuscript quality control |
| Output | Structured research output | Submission-ready manuscript |
| Scope | Exploratory research | Final redaction and QC |
| Audience | Researchers starting a project | Researchers finishing a paper |

The two frameworks are complementary. Use ARS to discover the literature and structure your research. Use scientific-redaction-skills when your results are ready and you need to produce a publication-quality manuscript.

---

## v0.1 scope boundaries

What v0.1 includes and does not include:

| In v0.1 | Not in v0.1 (deferred) |
|---|---|
| 24 skill files | `pdf_to_context.py` (automated PDF extraction) |
| 10 slash commands | Plugin marketplace listing |
| check_manuscript_integrity.py | Additional checker scripts (`check_figure_plan.py`, etc.) |
| 6 user templates + 6 subagent templates | Full Codex-native packaging |
| Synthetic example project | CI test suite |
| Multi-publisher policy table | Post-publication case study |
