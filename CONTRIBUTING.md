# Contributing to scientific-redaction-skills

Thank you for considering a contribution. This project is a skill framework, not a software library — contributions take the form of new skills, improved templates, new subagent patterns, or corrections to existing skills.

---

## Adding a new skill

Every skill file follows this structure:

```markdown
# Skill: [Name]

## Mandate
[One paragraph: what this skill does and what it does not do.
Include what human input is required to activate it.]

## Required inputs
- `@templates/AUTHOR_CONTEXT.md` — always required
- [additional files specific to this skill]

## Acceptance criteria
1. [Numbered list: when is the output good enough?]

## Human-in-the-loop checkpoint
[What the human must explicitly confirm before the output is acted upon.]

## Fail conditions
[When must the output be rejected entirely?]
```

Steps:
1. Create a new `.md` file in the appropriate `skills/` subdirectory.
2. Follow the structure above exactly — all five sections are required.
3. Add an entry to `skills/SKILLS_INDEX.md` with the task type, skill file path, and HiTL checkpoint summary.
4. Test the skill against the synthetic `example/` project before opening a pull request.
5. If the skill has a corresponding slash command, add or update `.claude/commands/srs-*.md`.

---

## Adding a phrase to the banned list

The default `BANNED_PHRASES` list in `scripts/check_manuscript_integrity.py` is intentionally conservative. If you encounter a phrase that recurs as an AI-writing artifact, open an issue with:
- The phrase
- Why it signals an AI-writing artifact
- A brief example of the problematic usage

Phrases are only added to the defaults if they are field-neutral and unlikely to produce false positives in normal scientific prose.

---

## Reporting issues

Use GitHub Issues with one of these templates:

**Broken skill** — the skill produces output that violates its mandate or acceptance criteria.
Required: skill file path, what input you provided, what output you received, what you expected.

**False positive** — the integrity checker flags something that is legitimate prose.
Required: the flagged text, the manuscript context, the script flag that triggered it.

**New skill request** — you need a skill that doesn't exist.
Required: what task it would perform, what human input it requires, what its fail condition would be.

---

## Pull request guidelines

- One PR per skill or logical change.
- New skills must include an entry in `skills/SKILLS_INDEX.md`.
- Do not include any real manuscript content, real citation keys, or real numerical results in example files.
- All example content must use clearly synthetic keys (e.g., `Author2024_ILLUSTRATIVE`).
- If you modify `check_manuscript_integrity.py`, verify it still runs correctly on `example/manuscript/main.tex`.
- Maintain the split license: skills/docs are CC BY 4.0, scripts are MIT, example content is CC0.

---

## Code of conduct

This project serves the scientific community. Contributions should be constructive, accurate, and honest about what AI tools can and cannot do. Overclaiming the capabilities of this framework in documentation or examples is treated as a quality defect.
