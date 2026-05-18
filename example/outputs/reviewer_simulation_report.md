# Reviewer Simulation Report

Date: 2026-05-18
Scope: current concrete compressive-strength worked example, including manuscript, generated artifacts, registries, and audit reports.

## Overall Simulated Outcome

**Major revision as a demonstration package; not suitable as a standalone empirical research article.**

The manuscript is candid about deterministic fallback provenance and avoids benchmark claims. The example is useful as a quality-control demonstration, but several improvements are needed before it should be presented as a completed package.

## Methodology Reviewer

Major concerns:

- Final test metrics come from a single 80/20 split. Five-fold cross-validation is used for ridge-penalty selection, not for a full uncertainty estimate of final performance.
- Ridge and OLS have nearly identical rounded performance, so ridge-specific framing should stay modest.
- Fallback provenance prevents claims about official UCI benchmark performance.

Minor concerns:

- The manuscript should state the random seed in Methods, not only in the generation log.
- The alpha grid is small, which is acceptable for a demonstration but not a broad model-selection study.

Verdict: acceptable as a transparent modelling demonstration after documentation polish; not acceptable as a benchmark-performance study.

## Concrete/Materials Reviewer

Major concerns:

- Cement ablation/correlation findings are clearly local but could still be misread as concrete-science conclusions if provenance language is weakened.
- Generated tables now include units for mixture quantities, age, strength, and errors; final PDF layout should still be reviewed.

Minor concerns:

- Add one limitation sentence about linear models missing nonlinear mixture and curing-age interactions.
- Harmonize display names such as `blast_furnace_slag` and "blast furnace slag".

Verdict: domain framing is conservative and usable for a worked example, with unit and terminology polish needed.

## General Scientific Reader

Major concerns:

- The example clearly says what it is not claiming, which is good, but the abstract is metric-dense for a demonstration.
- Some manuscript phrases still sound like internal workflow notes rather than reader-facing prose.

Minor concerns:

- Consider framing the contribution as an auditable linear-baseline workflow rather than only a ridge-regression example.
- Keep process documentation in README/reports rather than in manuscript prose where possible.

Verdict: readable and honest, but still needs final editorial polish.

## Data Integrity Reviewer

Major concerns:

- Current core numbers agree across manuscript, generation log, tables, and numerical registry after the registry refresh.
- The deterministic fallback label is correctly central to interpretation.
- Remaining mechanical warnings should be rechecked after table-unit revisions and manuscript polish.

Minor concerns:

- Overfull LaTeX boxes remain in some tables and long file-path text.

Verdict: substantially improved traceability, with remaining table polish and final checker refresh needed after edits.

## Editorial Reviewer

Major concerns:

- The package works as a framework demonstration, not as an empirical concrete research article.
- The final release should decide whether fallback data are acceptable or whether official UCI provenance must be verified.

Minor concerns:

- Remove unused bibliography entries or cite them for specific claims.
- Ensure the refreshed PDF is generated after final table and wording revisions.

Verdict: major revision before calling the example complete; acceptable to publish as a transparent work-in-progress demonstration if limitations remain visible.

## Summary

Remaining human decisions:

- Keep deterministic fallback data or verify official UCI observations.
- Keep ridge-specific framing or broaden to a linear-baseline workflow framing.
- Decide how much internal workflow language belongs in manuscript prose versus supporting documentation.

Priority fixes before final completion:

1. Review remaining LaTeX overfull/underfull warnings.
2. Remove or cite unused bibliography entries.
3. Decide whether fallback data are sufficient for the public example.
4. Rebuild the PDF after any final prose polish.
