# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project uses [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Added
- Generic return-of-experience rules for converting repeated human feedback into reusable skills without transferring project-specific data, findings, model names, or numerical results.
- Results-ordering checks requiring selection/comparison evidence before detailed selected-item analysis.
- Figure integration checks for filename/number alignment, stale cross-references after reordering, and avoidable figure-only pages in compiled drafts.
- Caption guidance for distinguishing modified terms, monitored diagnostics, relative-change quantities, residuals, penalties, and prediction errors.

---


## [0.1.0] — 2026-05-16

### Added
- Core skill framework: 24 skill files across 5 categories (writing, integrity, figures, review, workflow)
- 10 section-specific Claude Code slash commands (`.claude/commands/srs-*.md`)
- Executable integrity checker: `scripts/check_manuscript_integrity.py`
- 6 user-fill templates: STYLE_GUIDE, AUTHOR_CONTEXT, NUMERICAL_REGISTRY, CLAIM_REGISTER, SECTION_PLAN, AGENT_HANDOFF
- 6 subagent prompt templates in `templates/subagents/`
- Agent context files: ANTI_AI_WRITING_STYLE, JOURNAL_POLICY (multi-publisher table), MULTI_AGENT_ROLES
- `context/` directory for user-provided reference materials (target journal papers, group papers)
- Synthetic illustrative example project (polymer-composite thermal conductivity, all data fake)
- Documentation: SETUP.md, HUMAN_IN_THE_LOOP.md, WORKFLOW_GUIDE.md, ARCHITECTURE.md
- Graphical abstract (PNG) and generation script
- MIT + CC BY 4.0 + CC0 split license
- CLAUDE.md and CODEX.md orientation files

### Design decisions
- RESULT_FLEXIBILITY parameter (LOCKED / FIGURES_IMPROVABLE / MINOR_ANALYSIS_ALLOWED) in AUTHOR_CONTEXT
- 4-tier citation verification ladder (KEY_EXISTS → FULL_TEXT_SUPPORTS_CLAIM)
- 7 evidence status labels (RESULT_SUPPORTED, LITERATURE_SUPPORTED, etc.)
- 4 mandatory human-in-the-loop gates
- Style calibration from `context/` papers (Step 0c) before any drafting

### Not included in v0.1
- `scripts/pdf_to_context.py` (PDF → .md extraction; manual workflow documented instead)
- Codex-native packaging (CODEX.md documents integration patterns)
- Plugin marketplace listing
- CI test suite for scripts

---

[Unreleased]: https://github.com/SFETNI/scientific-writing-skills/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/SFETNI/scientific-writing-skills/releases/tag/v0.1.0
