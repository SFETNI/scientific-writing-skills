# Agent Handoff

The agent reads this file at the start of every session to understand the current state of the project. Update it at the end of every session.

---

## Current state

```
CURRENT_PHASE:      [Pre-draft / Drafting — Introduction / Drafting — Methods / ... / Final QC]
ACTIVE_TASK:        [Brief description of what to do next]
LAST_UPDATED:       [YYYY-MM-DD]
LAST_SESSION_AGENT: [Claude / Codex]
```

## Read-first list

Files the agent must read at the start of the next session, in order:

1. `AUTHOR_CONTEXT.md`
2. `NUMERICAL_REGISTRY.md`
3. `STYLE_GUIDE.md`
4. [Add any section-specific files for the current task]

---

## HiTL checkpoint log

Record every human checkpoint clearance here (append, do not overwrite):

```
# HG0a — Integrity check cleared — [date]
# HG0c — Style calibration approved — [date]
# HG1  — Introduction section plan approved — [date]
# HG2c — Introduction accepted — [date] — gate PASS
# [Add entries as work progresses]
```

---

## Section status

| Section | Status | Gate | Date |
|---|---|---|---|
| Introduction | [Not started / In progress / Accepted] | [PASS/FAIL/—] | |
| Methods | | | |
| Results | | | |
| Discussion | | | |
| Conclusions | | | |
| SM | | | |

---

## Deferred items

Tasks that were identified but not completed — address in next session:

| Item | Priority | Description |
|---|---|---|
| [e.g., Citation check for Doe2023] | High | Abstract not yet confirmed — at KEY_EXISTS only |
| | | |

---

## Process trace log

Append process traces here after each session (from `skill_process_trace.md`):

```
[Process traces appended here]
```
