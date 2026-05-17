# Multi-Agent Roles

This framework uses three distinct agent types with clearly separated responsibilities. Understanding these boundaries prevents role confusion and ensures the right agent handles each task.

---

## Agent roles

### Claude (primary agent)

**What Claude does:**
- Scientific prose: drafting, improving, calibrating
- Claim verification: evidence mapping, citation tier assessment
- Argument logic: structure review, argument flow analysis
- Reviewer simulation: generating adversarial review perspectives
- Human-in-the-loop management: presenting outputs for human review, enforcing gates
- Style calibration: reading context papers and generating calibration reports

**What Claude does not do:**
- File system batch operations (renaming, moving, renumbering files)
- LaTeX compilation and error reporting
- Programmatic bibliography maintenance
- DOCX export or format conversion

**Typical Claude session flow:**
1. Step 0: read context files, run integrity check
2. Read section plan or existing draft
3. Apply skill, produce output with labels
4. Present for human review
5. Wait for approval
6. Write process trace

---

### Codex / GPT-4 (operations agent)

**What Codex does:**
- Run `check_manuscript_integrity.py` and capture output
- LaTeX compilation (`pdflatex`, `bibtex`) and error reporting
- Batch file operations: renaming figures, reordering section files
- Inserting `\input{}` commands in `main.tex`
- Verifying figure paths against actual files
- Updating `\label{}` and `\ref{}` consistently across `.tex` files
- Running `pandoc` for DOCX export
- Normalising `.bib` file formatting
- Registry coverage checks

**What Codex does not do:**
- Scientific prose
- Claim evaluation
- Citation content (DOIs, author names)
- Certifying any section

**Typical Codex session flow:**
1. Receive task specification from Claude or human
2. Execute mechanical operation
3. Produce a one-paragraph handoff summary
4. Return to Claude for prose/logic follow-up if needed

---

### Claude Subagents (bounded review)

**What subagents do:**
- Run a single bounded, read-only review task
- Return a structured report to the main Claude agent
- Never modify files

**Available subagent templates:**
| Template | Task | Input | Output |
|---|---|---|---|
| `citation_audit_subagent.md` | Audit 20–30 citation keys | `.bib` file + claim list | Tier report |
| `figure_qc_subagent.md` | Review figure captions | Captions + NUMERICAL_REGISTRY | QC report |
| `overclaim_detection_subagent.md` | Scan for forbidden phrases + unregistered numbers | Section text + ANTI_AI_WRITING_STYLE + NUMERICAL_REGISTRY | Flagged report |
| `reviewer_simulation_subagent.md` | Simulate one reviewer role | Manuscript sections + NUMERICAL_REGISTRY | Review report |
| `argument_flow_subagent.md` | Check argument completeness | All sections + SECTION_PLAN | Argument map |
| `style_calibration_subagent.md` | Calibrate style from context papers | `context/` files + AUTHOR_CONTEXT | Style report |

**Subagent constraints:**
- Read-only: never modify any file
- Bounded: only process the inputs provided; do not read beyond the scope given
- No web access: cannot search the internet
- Return to main agent: all output goes back for human review

---

## Coordination pattern

```
Human ──→ Claude (main) ──→ [Skill invocation]
                     ├──→ Subagent (read-only) ──→ report ──→ Claude ──→ Human
                     └──→ Codex (operations)  ──→ summary ──→ Human
```

The human is always the final decision point. Claude presents reports and summaries; the human approves or rejects; Codex executes the approved mechanical changes.

---

## Session handoff between agents

When handing off between Claude and Codex:

**Claude → Codex handoff:**
```
CODEX TASK:
  - Run: [specific command]
  - Input files: [list]
  - Expected output: [description]
  - Do NOT: [list of prohibited actions]
  - Return: one-paragraph summary of what was done
```

**Codex → Claude handoff:**
```
CODEX SUMMARY:
  - Completed: [what was done]
  - Not changed: [what was left untouched]
  - Issues requiring scientific judgment: [list]
  - Next step for Claude: [description]
```
