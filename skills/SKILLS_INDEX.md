# Skills Index — Routing Table

Use this table to find the right skill for a given task. Read the linked skill file before activating it.

| Task type | Skill file | HiTL checkpoint |
|---|---|---|
| **WRITING** | | |
| Draft or improve a section | `writing/skill_section_drafting.md` | Human provides section plan or existing draft; approves every output |
| Check prose quality (no content change) | `writing/skill_prose_quality.md` | Human confirms no scientific content was changed |
| Verify and calibrate quantitative claims | `writing/skill_claim_calibration.md` | Human reviews claim–source map before accepting |
| Position benchmark / state-of-the-art papers | `writing/skill_benchmark_positioning.md` | Human confirms framing before Introduction is finalized |
| Draft Methods section | `writing/skill_methods_writing.md` | Human approves scope before drafting begins |
| Draft Results section | `writing/skill_results_writing.md` | Human approves argument plan before subsection drafting |
| Draft Supplementary Materials | `writing/skill_sm_writing.md` | Human approves SM scope and structure before content is written |
| Run section acceptance gate | `writing/skill_revision_quality_gate.md` | Human sign-off required; no section accepted without passing |
| **INTEGRITY** | | |
| Map every claim to evidence or citation | `integrity/skill_claim_evidence_verification.md` | Human resolves every UNSUPPORTED or NEEDS_HUMAN_DECISION item |
| Audit citation keys against .bib file | `integrity/skill_citation_check.md` | Human confirms all items below ABSTRACT_RELEVANT tier |
| Verify full-text claim support | `integrity/skill_reference_verification.md` | Human makes final call on NEEDS_REPLACEMENT items |
| Fill citation gaps (web search required) | `integrity/skill_literature_research.md` | **Requires explicit human authorization before any web search** |
| **FIGURES** | | |
| Assess figure readability and message clarity | `figures/skill_figure_qc.md` | Human approves QC report before initiating revisions |
| Draft figure and table captions | `figures/skill_figure_caption_writing.md` | Human confirms captions match figure content |
| Assess table structure and column design | `figures/skill_table_design.md` | Human approves redesign before implementation |
| Check cross-figure visual consistency | `figures/skill_visual_consistency.md` | Human confirms no narrative mismatches |
| **REVIEW** | | |
| Simulate peer reviewer perspective | `review/skill_reviewer_perspective.md` | Human reads full reviewer report; decides what to address vs. rebut |
| Review logical argument flow | `review/skill_argument_flow_review.md` | Human approves argument map |
| Estimate editorial decision | `review/skill_editorial_decision.md` | Human reviews decision estimate |
| **WORKFLOW** | | |
| Calibrate style from context papers | `workflow/skill_style_calibration.md` | Human approves style report before any drafting begins (Step 0c) |
| Standard agent task protocol | `workflow/skill_task_protocol.md` | Process document — no output approval required |
| Human checkpoint manifest | `workflow/skill_human_checkpoints.md` | Process document — defines all mandatory gates |
| End-of-task process trace | `workflow/skill_process_trace.md` | Required for every agent task |
| Convert repeated human feedback into reusable skill rules | `workflow/skill_process_trace.md` + relevant domain skill | Human confirms no project-specific findings or data are transferred |

## Slash command routing

| Command | Skill chain |
|---|---|
| `/srs-check` | Executable integrity checker (Step 0a) |
| `/srs-calibrate` | `workflow/skill_style_calibration` (Step 0c) |
| `/srs-intro` | `skill_benchmark_positioning` → `skill_section_drafting` → `skill_claim_calibration` |
| `/srs-methods` | `skill_methods_writing` → `skill_claim_evidence_verification` |
| `/srs-results` | `skill_results_writing` → `skill_figure_qc` → `skill_claim_calibration` |
| `/srs-discussion` | `skill_argument_flow_review` → `skill_claim_calibration` → `skill_reviewer_perspective` |
| `/srs-figures` | `skill_figure_qc` → `skill_figure_caption_writing` → `skill_visual_consistency` → `skill_table_design` |
| `/srs-sm` | `skill_sm_writing` → `skill_figure_qc` |
| `/srs-review` | `skill_reviewer_perspective` (4-role parallel subagents) |
| `/srs-gate` | `skill_revision_quality_gate` |
