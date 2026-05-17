"""
Graphical abstract for scientific-redaction-skills.
Run: ~/miniforge3/bin/python docs/generate_graphical_abstract.py
Output: docs/graphical_abstract.png
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse
import os

# ── Palette ────────────────────────────────────────────────────────────────────
# All white-text backgrounds verified >= 4.5:1 WCAG AA contrast ratio
C_INPUT  = '#1d3557'   # dark navy       — white contrast 11.0:1  ✓
C_SKILL  = '#1a5276'   # deep ocean blue — white contrast  7.4:1  ✓ (was #457b9d = 3.3:1 ✗)
C_HUMAN  = '#145a32'   # deep green      — white contrast  8.9:1  ✓
C_GATE   = '#7b241c'   # deep crimson    — white contrast  7.2:1  ✓
C_SUB    = '#d4eaf3'   # pale blue       — dark text only
C_OUTPUT = '#f4a227'   # amber gold      — dark contrast   3.5:1  (bold large text only)
C_CMD    = '#17405a'   # dark ocean      — white contrast 10.1:1  ✓
C_PHASE  = '#eef4f8'   # very light blue-grey
C_ARROW  = '#2c3e50'
C_WHITE  = '#ffffff'
C_DARK   = '#1a1a1a'
# Subtext colours — explicit, not transparency-based
CT_YELLOW = '#ffd166'  # yellow subtext on dark blue / red backgrounds
CT_LIGHT  = '#ddeaf5'  # off-white (gate ovals & fallback)
CT_DARK   = '#2c3e50'  # dark blue-grey for light backgrounds
CT_GOLD   = '#5a3200'  # dark brown for gold output box

FW, FH = 18, 28
fig, ax = plt.subplots(figsize=(FW, FH))
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.axis('off')
fig.patch.set_facecolor(C_WHITE)
ax.set_facecolor(C_WHITE)


# ── Drawing helpers ─────────────────────────────────────────────────────────────

def rbox(cx, cy, w, h, lines, fc, tc=C_WHITE, fs=12, bold=False,
         subtext=None, subfs=10.5, stc=None, ec=None):
    """Rounded rectangle with a bold title line and an optional details line."""
    edge = ec if ec else fc
    patch = FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle='round,pad=0.15',
        facecolor=fc, edgecolor=edge, linewidth=2, zorder=3, clip_on=False
    )
    ax.add_patch(patch)
    weight = 'bold' if bold else 'normal'
    y_title = cy + (0.16 if subtext else 0)
    ax.text(cx, y_title, lines,
            ha='center', va='center', fontsize=fs, color=tc,
            fontweight=weight, zorder=4, multialignment='center',
            linespacing=1.45, clip_on=False)
    if subtext:
        # yellow on dark-bg boxes, dark on light-bg boxes, or explicit override
        sc = stc if stc else (CT_YELLOW if tc == C_WHITE else CT_DARK)
        ax.text(cx, cy - 0.3, subtext,
                ha='center', va='center', fontsize=subfs, color=sc,
                fontweight='normal', zorder=4, multialignment='center',
                linespacing=1.4, clip_on=False)


def gate_oval(cx, cy, rw, rh, line1, line2=None, fc=C_HUMAN):
    e = Ellipse((cx, cy), rw, rh,
                facecolor=fc, edgecolor=C_WHITE, linewidth=2.5,
                zorder=3, clip_on=False)
    ax.add_patch(e)
    y1 = cy + (0.18 if line2 else 0)
    ax.text(cx, y1, line1,
            ha='center', va='center', fontsize=13, color=C_WHITE,
            fontweight='bold', zorder=4, multialignment='center', clip_on=False)
    if line2:
        ax.text(cx, cy - 0.24, line2,
                ha='center', va='center', fontsize=11, color=CT_LIGHT,
                fontweight='bold', zorder=4, multialignment='center',
                clip_on=False)


def arr(x1, y1, x2, y2, lw=2.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=C_ARROW,
                                lw=lw, mutation_scale=18),
                zorder=2, clip_on=False)


def phase_band(y_top, y_bot, label, fc=C_PHASE):
    p = FancyBboxPatch(
        (0.3, y_bot - 0.2), FW - 0.6, y_top - y_bot + 0.4,
        boxstyle='round,pad=0.05',
        facecolor=fc, edgecolor='#c8d6e0', linewidth=1, zorder=1, clip_on=False
    )
    ax.add_patch(p)
    ax.text(0.78, (y_top + y_bot) / 2, label,
            ha='center', va='center', fontsize=10.5, color='#555',
            style='italic', rotation=90, zorder=2, clip_on=False)


def hline(y, x1=0.4, x2=FW - 0.4, lw=0.8, color='#c0c8d0'):
    ax.plot([x1, x2], [y, y], color=color, lw=lw, zorder=1)


# ── Title block ────────────────────────────────────────────────────────────────
ax.text(FW/2, 27.35,
        'scientific-redaction-skills',
        ha='center', va='center', fontsize=22, fontweight='bold',
        color=C_INPUT)
ax.text(FW/2, 26.75,
        'A Human-in-the-Loop Skill Framework for Scientific Manuscript Redaction',
        ha='center', va='center', fontsize=12.5, color='#444')
hline(26.35)

# ── INPUT ROW ─────────────────────────────────────────────────────────────────
Y_IN = 25.6
IW = 7.2
rbox(5.0, Y_IN, IW, 1.1,
     'RESEARCHER RESULTS',
     C_INPUT, fs=12.5, bold=True,
     subtext='Figures  |  Tables  |  Numbers  |  Key findings',
     subfs=10.5)
rbox(13.0, Y_IN, IW, 1.1,
     'CONTEXT DOCUMENTS',
     C_SKILL, fs=12.5, bold=True,
     subtext='Target journal papers  |  Group papers  |  Reports',
     subfs=10.5)

# ── PHASE 1 : PRE-DRAFT ────────────────────────────────────────────────────────
phase_band(24.9, 22.2, '① Pre-draft')

arr(5.0, Y_IN - 0.53, 6.8, 24.35)
arr(13.0, Y_IN - 0.53, 11.2, 24.35)

rbox(9.0, 24.0, 12.5, 1.1,
     'Executable Integrity Check  —  check_manuscript_integrity.py',
     C_GATE, fs=11.5, bold=True,
     subtext='citation keys  |  figure paths  |  forbidden phrases  |  policy checklist',
     subfs=10.5)

arr(9.0, 23.45, 9.0, 22.83)

rbox(9.0, 22.5, 12.5, 1.1,
     'Style Calibration  —  skill_style_calibration',
     C_SKILL, fs=11.5, bold=True,
     subtext='align to journal voice  |  match group terminology  |  set hedging level',
     subfs=10.5)

# ── HUMAN GATE 1 ──────────────────────────────────────────────────────────────
arr(9.0, 22.05, 9.0, 21.38)
gate_oval(9.0, 21.05, 11.0, 1.0,
          'Human Gate 1',
          'Resolve hard errors  |  Confirm style parameters')

# ── SECTION PLAN ──────────────────────────────────────────────────────────────
arr(9.0, 20.55, 9.0, 19.93)
rbox(9.0, 19.6, 12.5, 1.1,
     'Section Plan  (per section)',
     C_SKILL, fs=11.5, bold=True,
     subtext='Argument chain  |  Key claims  |  Logical flow  |  Scope  |  Target message',
     subfs=10.5)

# ── HUMAN GATE 2 ──────────────────────────────────────────────────────────────
arr(9.0, 19.1, 9.0, 18.48)
gate_oval(9.0, 18.15, 11.0, 1.0,
          'Human Gate 2',
          'Approve argument plan  —  no prose written before this confirmation')

# ── PHASE 2 : SECTION DRAFTING ─────────────────────────────────────────────────
phase_band(17.55, 15.75, '② Drafting')

arr(9.0, 17.65, 9.0, 17.15)

CMD_Y  = 16.7
CMD_W  = 2.45
CMD_H  = 1.05
CMD_XS = [1.55, 4.1, 6.65, 9.0, 11.35, 13.9, 16.45]
CMD_LABELS = [
    ('/srs-intro',      'Introduction'),
    ('/srs-methods',    'Methods'),
    ('/srs-results',    'Results'),
    ('/srs-discussion', 'Discussion'),
    ('/srs-figures',    'Figures\n& Tables'),
    ('/srs-sm',         'Supplementary\nMaterials'),
]
for (cmd, sec), cx in zip(CMD_LABELS, CMD_XS[:6]):
    rbox(cx, CMD_Y, CMD_W, CMD_H,
         cmd, C_CMD, fs=12, bold=True,
         subtext=sec, subfs=10.5)

ax.text(FW/2, 16.0,
        '/srs-*  Section Drafting Commands',
        ha='center', va='center', fontsize=10, color='#777', style='italic')

# ── PHASE 3 : REVIEW SUBAGENTS ─────────────────────────────────────────────────
phase_band(15.35, 13.5, '③ Review')

arr(9.0, 15.45, 9.0, 14.95)

SUB_Y  = 14.3
SUB_W  = 3.4
SUB_H  = 1.1
SUB_XS = [2.3, 6.0, 9.0, 12.0, 15.7]
SUB_LABELS = [
    ('Citation Audit',          None),
    ('Figure QC\n& Overclaim',  None),
    ('Reviewer Simulation',     '3 roles + Data Integrity'),
    ('Argument\nFlow Review',   None),
]
for lbl, sub, cx in [(l, s, x) for (l, s), x in zip(SUB_LABELS, SUB_XS[:4])]:
    rbox(cx, SUB_Y, SUB_W, SUB_H,
         lbl, C_SUB, tc=CT_DARK, fs=11, bold=True,
         subtext=sub, subfs=10, stc='#3a6070')

ax.text(FW/2, 13.65,
        'Parallel  |  Bounded  |  Read-only',
        ha='center', va='center', fontsize=10.5, color='#777', style='italic')

# ── HUMAN GATE 3 ──────────────────────────────────────────────────────────────
arr(9.0, 13.6, 9.0, 12.98)
gate_oval(9.0, 12.65, 11.0, 1.0,
          'Human Gate 3',
          'Read all reports  |  Decide what to address vs. rebut')

# ── PHASE 4 : FINAL QC ─────────────────────────────────────────────────────────
phase_band(12.05, 9.85, '④ Final QC')

arr(9.0, 12.15, 9.0, 11.58)

rbox(9.0, 11.25, 12.5, 1.1,
     'Revision Quality Gate  —  /srs-gate',
     C_GATE, fs=11.5, bold=True,
     subtext='all acceptance criteria  |  CLAIM_REGISTER updated  |  numerical discipline',
     subfs=10.5)

arr(9.0, 10.7, 9.0, 10.13)

rbox(9.0, 9.8, 12.5, 1.1,
     'Policy Checklist',
     C_GATE, fs=11.5, bold=True,
     subtext='AI disclosure  |  Data availability  |  Competing interests  |  Author accountability',
     subfs=10.5)

# ── HUMAN GATE 4 ──────────────────────────────────────────────────────────────
arr(9.0, 9.35, 9.0, 8.73)
gate_oval(9.0, 8.4, 11.0, 1.0,
          'Human Gate 4',
          'Author certifies all content before submission')

# ── OUTPUT ────────────────────────────────────────────────────────────────────
arr(9.0, 7.9, 9.0, 7.28)
rbox(9.0, 6.9, 13.0, 1.2,
     'SUBMISSION-READY MANUSCRIPT',
     C_OUTPUT, tc=C_DARK, fs=14, bold=True,
     subtext='Claim-calibrated  |  Integrity-verified  |  Publisher-compliant',
     subfs=11, stc=CT_GOLD, ec='#c88000')

# ── LEGEND ────────────────────────────────────────────────────────────────────
hline(5.95)
ax.text(1.1, 5.62, 'Legend', fontsize=12, fontweight='bold', color='#444')

LEG = [
    (C_INPUT,  C_WHITE,  'Researcher input'),
    (C_SKILL,  C_WHITE,  'AI skill'),
    (C_GATE,   C_WHITE,  'Executable quality gate'),
    (C_HUMAN,  C_WHITE,  'Human decision checkpoint'),
    (C_SUB,    CT_DARK,  'Review subagent (read-only)'),
    (C_CMD,    C_WHITE,  'Section slash command'),
    (C_OUTPUT, CT_GOLD,  'Final output'),
]
dx, dy = 5.6, 0.75
for i, (fc, tc, label) in enumerate(LEG):
    col, row = i % 3, i // 3
    x = 1.1 + col * dx
    y = 5.0 - row * dy
    p = FancyBboxPatch((x, y - 0.22), 0.6, 0.44,
                       boxstyle='round,pad=0.05',
                       facecolor=fc, edgecolor='#bbb', linewidth=1.2, zorder=3)
    ax.add_patch(p)
    ax.text(x + 0.78, y, label,
            ha='left', va='center', fontsize=10.5, color='#333')

# ── Footer ─────────────────────────────────────────────────────────────────────
hline(3.42)
ax.text(FW/2, 3.1,
        'Aligned with guidelines from:  Elsevier  |  Springer Nature  |  Nature Portfolio  |  IEEE  |  MDPI',
        ha='center', va='center', fontsize=10.5, color='#555')
ax.text(FW/2, 2.62,
        'AI assistance with author accountability and disclosure  —  verify your target journal policy',
        ha='center', va='center', fontsize=10.5, color='#777', style='italic')
ax.text(FW/2, 2.15,
        'CC BY 4.0 (skills & docs)  |  MIT (scripts)  |  CC0 (example)',
        ha='center', va='center', fontsize=10, color='#aaa')

# ── Save ──────────────────────────────────────────────────────────────────────
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'graphical_abstract.png')
fig.savefig(out, dpi=150, bbox_inches='tight',
            facecolor=C_WHITE, edgecolor='none')
print(f'Saved: {out}')
