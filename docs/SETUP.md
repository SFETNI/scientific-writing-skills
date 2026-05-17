# Setup Guide

Install and configure scientific-redaction-skills for your manuscript project in 15 minutes.

---

## Pattern A — Claude Code slash commands (recommended)

This is the primary distribution model. The `/srs-*` commands become available immediately in any Claude Code session run from your manuscript directory.

### Step 1 — Clone the framework

```bash
git clone https://github.com/SFETNI/scientific-writing-skills
```

### Step 2 — Link commands to your manuscript project

```bash
# From your manuscript project directory:
mkdir -p .claude
ln -s /path/to/scientific-writing-skills/.claude/commands .claude/commands
```

### Step 3 — Copy templates and skills

```bash
cp -r /path/to/scientific-writing-skills/templates docs/templates/
cp -r /path/to/scientific-writing-skills/skills .
cp -r /path/to/scientific-writing-skills/agent_context .
cp -r /path/to/scientific-writing-skills/context .
```

### Step 4 — Fill in your context files

```bash
cp docs/templates/AUTHOR_CONTEXT.md AUTHOR_CONTEXT.md
cp docs/templates/NUMERICAL_REGISTRY.md NUMERICAL_REGISTRY.md
cp docs/templates/STYLE_GUIDE.md STYLE_GUIDE.md
cp docs/templates/AGENT_HANDOFF.md AGENT_HANDOFF.md
```

Fill in `AUTHOR_CONTEXT.md` with your target journal, file paths, and `RESULT_FLEXIBILITY` setting.

### Step 5 — Configure the CLAUDE.md

Copy the framework's `CLAUDE.md` to your manuscript project root:

```bash
cp /path/to/scientific-writing-skills/CLAUDE.md .
```

Edit the skill routing paths if your directory structure differs from the defaults.

### Step 6 — Add reference papers to context/

Place `.md` extracts of 3–5 target journal papers in `context/target_journal/`. See `context/README.md` for instructions.

### Step 7 — Verify installation

Open Claude Code in your manuscript directory and run:
```
/srs-check
```

If the `/srs-check` command is not found, verify that `.claude/commands/` exists and contains the `srs-check.md` file.

---

## Pattern B — Manual copy (no symlink)

Use this if symlinks are not available in your environment.

```bash
mkdir -p your-manuscript-project/.claude/commands
cp -r scientific-writing-skills/.claude/commands/* your-manuscript-project/.claude/commands/
cp -r scientific-writing-skills/skills your-manuscript-project/
cp -r scientific-writing-skills/templates your-manuscript-project/docs/templates/
cp -r scientific-writing-skills/agent_context your-manuscript-project/
cp    scientific-writing-skills/CLAUDE.md your-manuscript-project/
cp    scientific-writing-skills/CODEX.md  your-manuscript-project/
```

Then follow Steps 4–7 above.

---

## Codex setup

For Codex/GPT-4 agent integration, read `CODEX.md` at the root of this repository. Key Codex tasks:

```bash
# Run the integrity checker
python scripts/check_manuscript_integrity.py \
  --main-tex manuscript/main.tex \
  --bib manuscript/references/refs.bib \
  --registry NUMERICAL_REGISTRY.md

# Compile LaTeX (requires a LaTeX distribution)
pdflatex -halt-on-error manuscript/main.tex

# Export to DOCX (requires pandoc)
pandoc manuscript/main.tex -o manuscript/main.docx
```

---

## Python requirements

The integrity checker uses Python standard library only. Verified on Python 3.8+.

```bash
# Verify
python scripts/check_manuscript_integrity.py --help
```

No `pip install` needed for v0.1.

Planned for v0.2: `pdfminer.six` for `scripts/pdf_to_context.py`.

---

## Testing the installation

Run the checker on the illustrative example:

```bash
python scripts/check_manuscript_integrity.py \
  --main-tex example/manuscript/main.tex \
  --bib example/manuscript/references/example_references.bib \
  --registry example/NUMERICAL_REGISTRY.md

# Expected output: 0 hard errors, 12 warnings (SM values not in registry — expected for this demo)
# Compare with: example/outputs/example_integrity_check.txt
```

Then open Claude Code in the `example/` directory and run `/srs-check` to verify command routing.

---

## Troubleshooting

**`/srs-check` command not found in Claude Code**
- Verify `.claude/commands/srs-check.md` exists in your project directory.
- Restart the Claude Code session after creating the symlink or copying files.

**`check_manuscript_integrity.py` reports "main.tex not found"**
- Check the `MAIN_TEX_PATH` in `AUTHOR_CONTEXT.md`.
- Make sure you run the script from the project root, not from `scripts/`.

**All numbers flagged as unregistered**
- The numerical discipline check extracts all decimal values. Numbers in headers, section numbers, and figure labels will be flagged.
- Tune by: (a) adding important numbers to `NUMERICAL_REGISTRY.md`, or (b) running with `--no-numerical` for a faster check.

**Style calibration produces "family defaults only" report**
- Add `.md` paper extracts to `context/target_journal/`. See `context/README.md`.
