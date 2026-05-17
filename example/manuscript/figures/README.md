# Figures — ILLUSTRATIVE EXAMPLE

> **ILLUSTRATIVE ONLY. No real figures are included in this example.**

This directory should contain the figure files referenced in `main.tex`. In the illustrative example, figures are represented by placeholder `\fbox{}` commands in the `.tex` files.

## Expected figure files (for a complete example)

| File | Description | Referenced in |
|---|---|---|
| `fig_feature_importance.pdf` | Feature importance bar chart (GBR, 8 variables) | §3.3, Figure 1 |
| `fig_parity.pdf` | Predicted vs. observed parity plot (test set) | SM, Figure S1 |

## Creating placeholder figures

To run the integrity checker without missing-figure hard errors, create empty placeholder files:

```bash
touch example/manuscript/figures/fig_feature_importance.pdf
touch example/manuscript/figures/fig_parity.pdf
```

Or simply run the checker with the `--no-numerical` flag and note that figure path errors are expected in the example.

## CC0 note

Any figures added to this directory for the example should be clearly labeled as synthetic and dedicated to CC0 (public domain).
