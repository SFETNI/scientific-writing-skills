# Roadmap — manuscript-qc

> **On the public name:** `scientific-redaction-skills` is the GitHub repository name. The public alias **manuscript-qc** is preferred in documentation because "redaction" is commonly misread as "removing or blacking-out text." The two names refer to the same project.

**Author:** Seifallah El Fetni
**Current version:** v0.1.0 (2026-05-16)
**Status:** Public release

See [`CHANGELOG.md`](CHANGELOG.md) for what was delivered in each release.

---

## Mission and scope

**Mission:** A portable, field-agnostic human-in-the-loop quality-control framework for scientific manuscript redaction. The framework helps researchers verify claims, citations, figures, tables, and argument structure before submission — using AI as a controlled assistant rather than an autonomous author. The science is always the researcher's; the framework makes the redaction process auditable, reproducible, and publisher-compliant.

**In scope:**
- Manuscript section drafting (Introduction through Conclusions)
- Claim calibration and numerical discipline
- Citation discipline and reference verification
- Figure and table quality control
- Reviewer-perspective simulation
- Overclaim and forbidden-language detection
- Human-in-the-loop checkpoints at each stage
- Journal-policy awareness (AI disclosure, author accountability)
- Multi-agent coordination patterns (Claude, Codex, subagents)
- Executable integrity checks (Python scripts)
- Transferable workflow across research projects and fields

**Out of scope:**
- Literature discovery and systematic review (see `academic-research-skills`)
- AI-assisted writing of scientific findings (the findings must exist and be fixed)
- Data analysis, statistics, experiment design
- Journal submission mechanics (format conversion, cover letters)
- Anything that generates scientific claims from scratch

---

## Skill taxonomy

All 24 skills follow this structure: **Mandate · Required inputs · Acceptance criteria · HiTL checkpoint · Fail conditions.**

### Writing skills (8)

| Skill | Mandate | HiTL checkpoint |
|---|---|---|
| `skill_section_drafting` | Assist prose development from a human-provided section plan or existing draft. Never generates scientific content from nothing — the substance always comes from the human. | Human provides plan or draft before activation; human approves every output |
| `skill_prose_quality` | Review and improve prose without changing scientific content | Human confirms no content changes |
| `skill_claim_calibration` | Verify every quantitative claim is supported and appropriately hedged | Human reviews claim–source map |
| `skill_benchmark_positioning` | Ensure benchmark papers are positioned as methodological context, not competitors | Human confirms framing before Introduction is finalized |
| `skill_methods_writing` | Draft Methods from study design files | Human approves methods scope before drafting |
| `skill_results_writing` | Draft Results from accepted figures and tables | Human approves argument plan before subsection drafting |
| `skill_sm_writing` | Draft Supplementary Materials: scope, numbering, cross-references to main text | Human approves SM scope and structure before content is written |
| `skill_revision_quality_gate` | Run acceptance checklist before a section is accepted | Human sign-off required; no section accepted without passing this gate |

### Integrity skills (4)

| Skill | Mandate | HiTL checkpoint |
|---|---|---|
| `skill_claim_evidence_verification` | Map every claim to a source artifact or citation | Human resolves UNSUPPORTED claims |
| `skill_citation_check` | Advance each reference up the citation verification ladder. Reports tier reached for every reference; never declares "verified" without stating which tier. | Human confirms all items below `ABSTRACT_RELEVANT`; human reads full text to reach `FULL_TEXT_SUPPORTS_CLAIM` |
| `skill_reference_verification` | For citations flagged as `ABSTRACT_RELEVANT`, attempt to confirm `FULL_TEXT_SUPPORTS_CLAIM` by reading available text | Human makes the final call on every `NEEDS_HUMAN_DECISION` and `NEEDS_REPLACEMENT` item |
| `skill_literature_research` | Fill citation gaps when authorized | Requires explicit human authorization before any web search |

### Figure skills (4)

| Skill | Mandate | HiTL checkpoint |
|---|---|---|
| `skill_figure_qc` | Assess figure readability, label consistency, and message clarity | Human approves QC report before revisions |
| `skill_figure_caption_writing` | Draft captions that state the main message, model, and scope | Human confirms captions match figure content |
| `skill_table_design` | Assess table structure; flag Interpretation/Notes columns | Human approves table redesign |
| `skill_visual_consistency` | Verify consistent model labels, colors, and notation across all figures | Human confirms no narrative mismatches |

### Review skills (3)

| Skill | Mandate | HiTL checkpoint |
|---|---|---|
| `skill_reviewer_perspective` | Simulate a critical peer reviewer's response to each section | Human reads and interprets reviewer report |
| `skill_argument_flow_review` | Verify the argument chain is logically complete | Human approves argument map |
| `skill_editorial_decision` | Estimate editorial decision (accept/revise/reject) with rationale | Human reviews decision estimate |

### Workflow skills (4)

| Skill | Mandate | HiTL checkpoint |
|---|---|---|
| `skill_style_calibration` | Read `context/` papers and produce a style calibration report: preferred hedges, claim density, tense conventions, citation placement | Human approves style report before any section drafting begins |
| `skill_task_protocol` | Standard agent task flow (Step 0 through report) | N/A (process document) |
| `skill_human_checkpoints` | Explicit list of all points requiring human decision | N/A (process document) |
| `skill_process_trace` | End-of-task reporting template | Required for every agent task |

---

## Evidence status labels

Every claim produced or reviewed by an integrity skill must be assigned one of these labels. Skills must never collapse them into a generic "verified" or "supported" label.

| Label | Meaning |
|---|---|
| `RESULT_SUPPORTED` | Claim is directly supported by a figure, table, or number in the accepted results |
| `LITERATURE_SUPPORTED` | Claim is supported by a citation whose full text was read and confirmed |
| `METHOD_DEFINITION` | Claim is a definitional statement of the methodology — verifiable from the study design |
| `INTERPRETATION` | Claim is an interpretation of results — plausible but requires hedging |
| `SPECULATION` | Claim goes beyond the evidence — must be explicitly flagged as speculation in the text |
| `UNSUPPORTED` | No supporting evidence found — must be removed or replaced |
| `NEEDS_HUMAN_DECISION` | Ambiguous — agent cannot classify without human judgment |

---

## Citation verification tiers

Citation verification is a ladder, not a binary. Skills must report which tier was reached for each reference — never just "verified."

| Tier | What it means | Who confirms |
|---|---|---|
| `KEY_EXISTS` | Citation key is present in the `.bib` file | Script |
| `METADATA_VERIFIED` | Author, year, title, journal/venue are complete and internally consistent | Script + agent |
| `ABSTRACT_RELEVANT` | Abstract confirms the paper is relevant to the claim being made | Agent (with human review) |
| `FULL_TEXT_SUPPORTS_CLAIM` | Full text was read and confirms the specific claim | Human |
| `DOES_NOT_SUPPORT_CLAIM` | Full text does not support the claim as written | Agent flags; human decides |
| `NEEDS_REPLACEMENT` | Reference must be replaced before submission | Human |

---

## Human-in-the-loop design

Every skill enforces one principle: **AI assists, humans decide.**

All 15 checkpoints (HG0a through HG5c) are blocking. The workflow does not advance past a blocking checkpoint without explicit human confirmation.

Full rationale and checkpoint table: [`docs/HUMAN_IN_THE_LOOP.md`](docs/HUMAN_IN_THE_LOOP.md)

The five categories of human decision that cannot be delegated:
1. Whether a citation supports a specific claim (requires reading the full text)
2. Whether a claim is in scope for this manuscript
3. Whether an interpretation is appropriately hedged
4. Whether a limitation must be stated
5. Final submission certification

---

## Installation and use

**Pattern A — Claude Code slash commands (recommended)**

```bash
git clone https://github.com/SFETNI/scientific-writing-skills
cd your-manuscript-project
mkdir -p .claude
ln -s /path/to/scientific-writing-skills/.claude/commands .claude/commands
```

The `/srs-*` commands are immediately available in any Claude Code session.

**Pattern B — Manual copy**

```bash
cp -r scientific-writing-skills/.claude/commands  your-project/.claude/
cp -r scientific-writing-skills/skills            your-project/
cp -r scientific-writing-skills/templates         your-project/docs/templates/
cp -r scientific-writing-skills/agent_context     your-project/
cp    scientific-writing-skills/CLAUDE.md         your-project/
```

Note: a `/plugin install` command for one-line remote installation is not yet available in Claude Code. The `.claude/commands/` symlink approach (Pattern A) is the recommended distribution model for v0.1.

---

## Adding a new skill

Every skill file has this structure:

```markdown
# Skill: [Name]

## Mandate
[One paragraph: what this skill does and what it does not do]

## Required inputs
[List of files to read before activating this skill]

## Acceptance criteria
[Numbered list: when is the skill output good enough?]

## Human-in-the-loop checkpoint
[What the human must confirm before results are acted upon]

## Fail conditions
[When should the skill output be rejected entirely?]
```

To add a skill:
1. Create a new `.md` file in the appropriate `skills/` subdirectory
2. Follow the standard structure above
3. Add an entry to `skills/SKILLS_INDEX.md`
4. Test it against the synthetic example project

Full contributor guidance: [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## v0.1 — Delivered (2026-05-16)

| Deliverable | Status |
|---|---|
| 24 skill files (all 5 categories) | Done |
| 10 `/srs-*` Claude Code slash commands | Done |
| `CLAUDE.md` at repo root | Done |
| `CODEX.md` at repo root | Done |
| `skills/SKILLS_INDEX.md` | Done |
| `scripts/check_manuscript_integrity.py` (stdlib-only) | Done |
| Agent context files (ANTI_AI_WRITING_STYLE, JOURNAL_POLICY, MULTI_AGENT_ROLES) | Done |
| Templates: AUTHOR_CONTEXT, NUMERICAL_REGISTRY, STYLE_GUIDE, SECTION_PLAN, CLAIM_REGISTER, AGENT_HANDOFF | Done |
| `context/` directory with PDF-to-md instructions | Done |
| Subagent templates (6 files) | Done |
| Synthetic example (polymer-composite thermal conductivity, CC0) | Done |
| `docs/` documentation (ARCHITECTURE, SETUP, HUMAN_IN_THE_LOOP, WORKFLOW_GUIDE) | Done |
| `docs/graphical_abstract.png` | Done |
| MIT + CC BY 4.0 + CC0 license | Done |

**Not in v0.1 (deferred):**
- `scripts/pdf_to_context.py` — PDF-to-.md context extraction script
- Plugin marketplace listing
- Full Codex-native packaging
- Additional checker scripts (`check_figure_plan.py`, `check_model_names.py`)
- CI test suite

---

## v0.2 — Planned

Goal: PDF ingestion script, additional checker utilities, first real user feedback incorporated.

| Planned deliverable | Notes |
|---|---|
| `scripts/pdf_to_context.py` | PDF → `.md` context extraction (pdfminer.six) |
| `check_figure_plan.py` | Verify all figures in figure_plan.md have files and LaTeX labels |
| `check_model_names.py` | Verify model display names are consistent across all .tex files |
| `check_registry_coverage.py` | Report which manuscript sections cite registry numbers vs. missing |
| `srs-config.yaml` support | Config file for manuscript paths instead of CLI flags |
| Revised skill files based on first user feedback | Breaking changes require minor version bump |

---

## v1.0 — Planned

Goal: stable, thoroughly documented, community-ready. Entry bar: validated across at least two independent research projects.

| Planned deliverable | Notes |
|---|---|
| Full pipeline documentation at ARS quality level | Including Mermaid flow diagrams |
| All skill files at v1 stability | Breaking changes require major version bump |
| Plugin marketplace listing | When the Claude Code plugin API is available |
| CI tests for checker scripts | pytest or equivalent |
| Second synthetic example project | Different field (chemistry or environmental science) |
| Word/DOCX support | Via python-docx; v0.1 is LaTeX-only |
| Post-publication case study | After a paper using the framework is published |

---

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Agent declares citation "verified" after only checking the key exists | High | High — fabricated citations in published paper | Four-tier verification ladder enforced; skills must never collapse tiers into a single label |
| Checker script too noisy (too many false positives) | Medium | Medium — users ignore warnings | BANNED_PHRASES defaults tuned conservatively; thresholds configurable |
| Users treat it as a writing bot, not a quality-control tool | Medium | High — bad science | Strong HiTL messaging in README and HUMAN_IN_THE_LOOP.md; mandatory blocking checkpoints |
| LaTeX-centric design excludes Word users | Medium | Low — addressable in v1.0 | README states LaTeX requirement clearly; Word support deferred to v1.0 |
| Skill files too domain-specific | Low | Medium — low uptake | Materials science example chosen for broad STEM familiarity; all domain examples generalized |
| ARS adds manuscript-redaction features that overlap | Low | Low | Narrow scope maintained; different entry point (results complete vs. literature start) |
| License confusion (CC BY vs CC BY-NC) | Low | Low | MIT/CC BY 4.0 used consistently; rationale documented in CONTRIBUTING.md |

---

## Licensing

| Component | License |
|---|---|
| Scripts (`scripts/`) | [MIT](LICENSE) |
| Skills, templates, documentation | [CC BY 4.0](LICENSE) |
| Synthetic example (`example/`) | [CC0 — Public Domain](LICENSE) |

CC BY 4.0 was chosen over CC BY-NC to avoid restricting use by researchers at industry institutions or those under open-access mandates.
