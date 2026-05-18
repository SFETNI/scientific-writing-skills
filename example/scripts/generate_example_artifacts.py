#!/usr/bin/env python3
"""Generate deterministic data, figures, tables, and log files for the example."""

from __future__ import annotations

import io
import math
import sys
import textwrap
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


SEED = 20260518
UCI_ZIP_URL = "https://archive.ics.uci.edu/static/public/165/concrete+compressive+strength.zip"
SOURCE_UCI = "UCI_CC_BY_4_0"
SOURCE_FALLBACK = "DETERMINISTIC_FALLBACK_NOT_UCI"

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "manuscript" / "figures"
TABLE_DIR = ROOT / "manuscript" / "tables"
OUTPUT_DIR = ROOT / "outputs"
DATA_CSV = DATA_DIR / "concrete_compressive_strength.csv"
LOG_PATH = OUTPUT_DIR / "example_generation_log.txt"
GENERATED_FIGURES = [
    "fig_dataset_overview.pdf",
    "fig_parity_ridge.pdf",
    "fig_residuals.pdf",
    "fig_coefficients.pdf",
    "fig_age_response.pdf",
]
GENERATED_TABLES = [
    "table_dataset_summary.tex",
    "table_model_performance.tex",
    "table_ablation.tex",
    "table_error_by_age.tex",
    "table_supplementary_cv.tex",
]

FEATURES = [
    "cement",
    "blast_furnace_slag",
    "fly_ash",
    "water",
    "superplasticizer",
    "coarse_aggregate",
    "fine_aggregate",
    "age",
]
TARGET = "compressive_strength"


@dataclass(frozen=True)
class FitResult:
    name: str
    alpha: float
    beta: np.ndarray
    train_metrics: dict[str, float]
    test_metrics: dict[str, float]


def ensure_dirs() -> None:
    for path in (DATA_DIR, FIG_DIR, TABLE_DIR, OUTPUT_DIR):
        path.mkdir(parents=True, exist_ok=True)


def normalise_columns(df: pd.DataFrame) -> pd.DataFrame:
    mapping = {
        "Cement (component 1)(kg in a m^3 mixture)": "cement",
        "Blast Furnace Slag (component 2)(kg in a m^3 mixture)": "blast_furnace_slag",
        "Fly Ash (component 3)(kg in a m^3 mixture)": "fly_ash",
        "Water  (component 4)(kg in a m^3 mixture)": "water",
        "Superplasticizer (component 5)(kg in a m^3 mixture)": "superplasticizer",
        "Coarse Aggregate  (component 6)(kg in a m^3 mixture)": "coarse_aggregate",
        "Fine Aggregate (component 7)(kg in a m^3 mixture)": "fine_aggregate",
        "Age (day)": "age",
        "Concrete compressive strength(MPa, megapascals) ": "compressive_strength",
        "Cement": "cement",
        "Blast Furnace Slag": "blast_furnace_slag",
        "Fly Ash": "fly_ash",
        "Water": "water",
        "Superplasticizer": "superplasticizer",
        "Coarse Aggregate": "coarse_aggregate",
        "Fine Aggregate": "fine_aggregate",
        "Age": "age",
        "Concrete compressive strength": "compressive_strength",
    }
    cleaned = df.rename(columns={c: mapping.get(str(c).strip(), str(c).strip()) for c in df.columns})
    missing = [c for c in FEATURES + [TARGET] if c not in cleaned.columns]
    if missing:
        raise ValueError(f"UCI file did not contain expected columns: {missing}")
    out = cleaned[FEATURES + [TARGET]].copy()
    for col in FEATURES + [TARGET]:
        out[col] = pd.to_numeric(out[col], errors="raise")
    out["source_label"] = SOURCE_UCI
    return out


def try_load_uci() -> tuple[pd.DataFrame | None, str]:
    try:
        with urllib.request.urlopen(UCI_ZIP_URL, timeout=20) as response:
            archive_bytes = response.read()
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as zf:
            names = zf.namelist()
            xls_name = next((name for name in names if name.lower().endswith(".xls")), None)
            if xls_name is None:
                raise ValueError(f"No .xls file in UCI archive: {names}")
            with zf.open(xls_name) as handle:
                raw = handle.read()
        df = pd.read_excel(io.BytesIO(raw))
        return normalise_columns(df), "Downloaded and parsed official UCI archive."
    except (
        urllib.error.URLError,
        urllib.error.HTTPError,
        TimeoutError,
        ValueError,
        ImportError,
        ModuleNotFoundError,
    ) as exc:
        return None, f"Official UCI download/parsing unavailable: {type(exc).__name__}: {exc}"


def deterministic_fallback() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    n = 1030
    ages = np.array([1, 3, 7, 14, 28, 56, 90, 100, 180, 365])
    age_probs = np.array([0.04, 0.07, 0.11, 0.10, 0.38, 0.10, 0.08, 0.04, 0.04, 0.04])

    cement = rng.uniform(102, 540, n)
    slag = np.where(rng.random(n) < 0.45, 0, rng.uniform(15, 359, n))
    fly_ash = np.where(rng.random(n) < 0.55, 0, rng.uniform(20, 200, n))
    water = rng.uniform(122, 247, n)
    superplasticizer = np.where(rng.random(n) < 0.35, 0, rng.uniform(1.5, 32, n))
    coarse = rng.uniform(801, 1145, n)
    fine = rng.uniform(594, 993, n)
    age = rng.choice(ages, size=n, p=age_probs)

    binder = cement + 0.72 * slag + 0.55 * fly_ash
    water_binder = water / np.maximum(binder, 1)
    maturity = np.log1p(age) / np.log1p(365)
    scm_late = maturity * (0.010 * slag + 0.007 * fly_ash)
    aggregate_balance = -0.006 * np.abs(coarse - 975) - 0.004 * np.abs(fine - 775)
    admixture = 0.23 * superplasticizer
    noise = rng.normal(0, 4.2 + 2.0 * (age < 14), n)

    strength = (
        7.5
        + 0.072 * cement
        + scm_late
        - 42.0 * water_binder
        + 31.0 * maturity
        + admixture
        + aggregate_balance
        + noise
    )
    strength = np.clip(strength, 2.3, 82.6)

    return pd.DataFrame(
        {
            "cement": cement,
            "blast_furnace_slag": slag,
            "fly_ash": fly_ash,
            "water": water,
            "superplasticizer": superplasticizer,
            "coarse_aggregate": coarse,
            "fine_aggregate": fine,
            "age": age,
            "compressive_strength": strength,
            "source_label": SOURCE_FALLBACK,
        }
    ).round(3)


def load_or_create_dataset() -> tuple[pd.DataFrame, list[str]]:
    messages: list[str] = []
    if DATA_CSV.exists():
        df = pd.read_csv(DATA_CSV)
        messages.append(f"Loaded existing local dataset: {DATA_CSV}")
        return df, messages

    df, msg = try_load_uci()
    messages.append(msg)
    if df is None:
        df = deterministic_fallback()
        messages.append("Created deterministic fallback dataset; this is not UCI data.")
    df.to_csv(DATA_CSV, index=False)
    messages.append(f"Wrote dataset CSV: {DATA_CSV}")
    return df, messages


def split_indices(n: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(SEED)
    indices = rng.permutation(n)
    n_train = int(round(0.8 * n))
    return np.sort(indices[:n_train]), np.sort(indices[n_train:])


def design_matrix(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mean = x.mean(axis=0)
    scale = x.std(axis=0, ddof=0)
    scale[scale == 0] = 1.0
    z = (x - mean) / scale
    return np.column_stack([np.ones(len(z)), z]), mean, scale


def apply_design(x: np.ndarray, mean: np.ndarray, scale: np.ndarray) -> np.ndarray:
    return np.column_stack([np.ones(len(x)), (x - mean) / scale])


def fit_ridge(x_design: np.ndarray, y: np.ndarray, alpha: float) -> np.ndarray:
    penalty = np.eye(x_design.shape[1])
    penalty[0, 0] = 0.0
    return np.linalg.solve(x_design.T @ x_design + alpha * penalty, x_design.T @ y)


def metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    residual = y_true - y_pred
    ss_res = float(np.sum(residual**2))
    ss_tot = float(np.sum((y_true - y_true.mean()) ** 2))
    return {
        "RMSE": float(np.sqrt(np.mean(residual**2))),
        "MAE": float(np.mean(np.abs(residual))),
        "R2": float(1.0 - ss_res / ss_tot) if ss_tot else float("nan"),
        "Bias": float(np.mean(y_pred - y_true)),
    }


def kfold_cv(x: np.ndarray, y: np.ndarray, alphas: list[float], k: int = 5) -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    folds = np.array_split(rng.permutation(len(y)), k)
    rows: list[dict[str, float]] = []
    for alpha in alphas:
        fold_metrics = []
        for fold_id in range(k):
            valid_idx = folds[fold_id]
            train_idx = np.concatenate([folds[j] for j in range(k) if j != fold_id])
            xtr, mean, scale = design_matrix(x[train_idx])
            xva = apply_design(x[valid_idx], mean, scale)
            beta = fit_ridge(xtr, y[train_idx], alpha)
            fold_metrics.append(metrics(y[valid_idx], xva @ beta))
        rows.append(
            {
                "alpha": alpha,
                "cv_rmse_mean": np.mean([m["RMSE"] for m in fold_metrics]),
                "cv_rmse_sd": np.std([m["RMSE"] for m in fold_metrics], ddof=1),
                "cv_mae_mean": np.mean([m["MAE"] for m in fold_metrics]),
                "cv_r2_mean": np.mean([m["R2"] for m in fold_metrics]),
            }
        )
    return pd.DataFrame(rows)


def fit_models(df: pd.DataFrame) -> tuple[dict[str, object], list[str]]:
    x = df[FEATURES].to_numpy(float)
    y = df[TARGET].to_numpy(float)
    train_idx, test_idx = split_indices(len(df))
    x_train, y_train = x[train_idx], y[train_idx]
    x_test, y_test = x[test_idx], y[test_idx]
    xtr, mean, scale = design_matrix(x_train)
    xte = apply_design(x_test, mean, scale)

    alphas = [0.0, 0.1, 1.0, 10.0, 100.0]
    cv = kfold_cv(x_train, y_train, alphas)
    best_alpha = float(cv.sort_values(["cv_rmse_mean", "alpha"]).iloc[0]["alpha"])

    baseline_pred_train = np.repeat(y_train.mean(), len(y_train))
    baseline_pred_test = np.repeat(y_train.mean(), len(y_test))
    baseline = FitResult(
        name="Training-mean baseline",
        alpha=float("nan"),
        beta=np.array([y_train.mean()]),
        train_metrics=metrics(y_train, baseline_pred_train),
        test_metrics=metrics(y_test, baseline_pred_test),
    )
    ols_beta = fit_ridge(xtr, y_train, 0.0)
    ols = FitResult(
        name="Standardized OLS",
        alpha=0.0,
        beta=ols_beta,
        train_metrics=metrics(y_train, xtr @ ols_beta),
        test_metrics=metrics(y_test, xte @ ols_beta),
    )
    ridge_beta = fit_ridge(xtr, y_train, best_alpha)
    ridge = FitResult(
        name="Standardized ridge",
        alpha=best_alpha,
        beta=ridge_beta,
        train_metrics=metrics(y_train, xtr @ ridge_beta),
        test_metrics=metrics(y_test, xte @ ridge_beta),
    )

    return {
        "train_idx": train_idx,
        "test_idx": test_idx,
        "mean": mean,
        "scale": scale,
        "cv": cv,
        "fits": [baseline, ols, ridge],
        "ridge": ridge,
        "x_train_design": xtr,
        "x_test_design": xte,
        "y_train": y_train,
        "y_test": y_test,
        "ridge_pred_test": xte @ ridge.beta,
    }, [f"Selected ridge alpha by 5-fold CV: {best_alpha:g}"]


def write_latex_table(df: pd.DataFrame, path: Path, caption: str, label: str, float_format: str = "%.3f") -> None:
    latex = df.to_latex(index=False, escape=True, float_format=float_format, caption=caption, label=label)
    path.write_text(latex, encoding="utf-8")


def make_tables(df: pd.DataFrame, model: dict[str, object]) -> dict[str, pd.DataFrame]:
    source = str(df["source_label"].iloc[0])
    summary = (
        df[FEATURES + [TARGET]]
        .agg(["count", "mean", "std", "min", "median", "max"])
        .T.reset_index()
        .rename(
            columns={
                "index": "Variable",
                "count": "N",
                "mean": "Mean",
                "std": "SD",
                "min": "Min",
                "median": "Median",
                "max": "Max",
            }
        )
    )
    summary["N"] = summary["N"].astype(int)

    fits: list[FitResult] = model["fits"]  # type: ignore[assignment]
    performance = pd.DataFrame(
        [
            {
                "Model": fit.name,
                "Alpha": fit.alpha if math.isfinite(fit.alpha) else "--",
                "Train RMSE (MPa)": fit.train_metrics["RMSE"],
                "Test RMSE (MPa)": fit.test_metrics["RMSE"],
                "Test MAE (MPa)": fit.test_metrics["MAE"],
                "Test R2": fit.test_metrics["R2"],
                "Test Bias (MPa)": fit.test_metrics["Bias"],
            }
            for fit in fits
        ]
    )

    ridge: FitResult = model["ridge"]  # type: ignore[assignment]
    train_idx: np.ndarray = model["train_idx"]  # type: ignore[assignment]
    test_idx: np.ndarray = model["test_idx"]  # type: ignore[assignment]
    ablation_rows = []
    for feature in FEATURES:
        kept = [f for f in FEATURES if f != feature]
        sub_train = df.iloc[train_idx][kept].to_numpy(float)
        sub_test = df.iloc[test_idx][kept].to_numpy(float)
        y_train: np.ndarray = model["y_train"]  # type: ignore[assignment]
        y_test: np.ndarray = model["y_test"]  # type: ignore[assignment]
        xtr, mean, scale = design_matrix(sub_train)
        xte = apply_design(sub_test, mean, scale)
        beta = fit_ridge(xtr, y_train, ridge.alpha)
        test_rmse = metrics(y_test, xte @ beta)["RMSE"]
        ablation_rows.append(
            {
                "Removed feature": feature.replace("_", " "),
                "Test RMSE (MPa)": test_rmse,
                "Delta RMSE (MPa)": test_rmse - ridge.test_metrics["RMSE"],
            }
        )
    ablation = pd.DataFrame(ablation_rows).sort_values("Delta RMSE (MPa)", ascending=False)

    test_df = df.iloc[test_idx].copy()
    y_test = model["y_test"]  # type: ignore[assignment]
    pred_test = model["ridge_pred_test"]  # type: ignore[assignment]
    test_df["absolute_error"] = np.abs(y_test - pred_test)
    test_df["signed_error"] = pred_test - y_test
    bins = [-np.inf, 7, 28, 90, np.inf]
    labels = ["<=7 days", "8-28 days", "29-90 days", ">90 days"]
    test_df["age_bin"] = pd.cut(test_df["age"], bins=bins, labels=labels)
    error_by_age = (
        test_df.groupby("age_bin", observed=False)
        .agg(
            N=("absolute_error", "size"),
            **{
                "Mean age (days)": ("age", "mean"),
                "MAE (MPa)": ("absolute_error", "mean"),
                "Bias (MPa)": ("signed_error", "mean"),
                "Mean strength (MPa)": ("compressive_strength", "mean"),
            }
        )
        .reset_index()
        .rename(columns={"age_bin": "Age bin"})
    )

    cv = model["cv"].copy()  # type: ignore[assignment]
    cv = cv.rename(
        columns={
            "alpha": "Alpha",
            "cv_rmse_mean": "CV RMSE mean (MPa)",
            "cv_rmse_sd": "CV RMSE SD (MPa)",
            "cv_mae_mean": "CV MAE mean (MPa)",
            "cv_r2_mean": "CV R2 mean",
        }
    )

    write_latex_table(
        summary,
        TABLE_DIR / "table_dataset_summary.tex",
        f"Dataset summary statistics. Mixture variables are kg/m3, age is days, and compressive strength is MPa. Source label: {source}.",
        "tab:dataset-summary",
    )
    write_latex_table(
        performance,
        TABLE_DIR / "table_model_performance.tex",
        "Train and test performance for baseline, ordinary least squares, and ridge models. Error and bias values are in MPa.",
        "tab:model-performance",
    )
    write_latex_table(
        ablation,
        TABLE_DIR / "table_ablation.tex",
        "Single-feature ablation using the selected ridge penalty. RMSE values are in MPa.",
        "tab:ablation",
    )
    write_latex_table(
        error_by_age,
        TABLE_DIR / "table_error_by_age.tex",
        "Ridge-model test-set error stratified by curing-age group. Error and strength values are in MPa.",
        "tab:error-by-age",
    )
    write_latex_table(
        cv,
        TABLE_DIR / "table_supplementary_cv.tex",
        "Five-fold cross-validation results used to select the ridge penalty. RMSE and MAE values are in MPa.",
        "tab:supplementary-cv",
    )
    return {
        "summary": summary,
        "performance": performance,
        "ablation": ablation,
        "error_by_age": error_by_age,
        "cv": cv,
    }


def style_axes(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, color="#dddddd", linewidth=0.6, alpha=0.8)


def make_figures(df: pd.DataFrame, model: dict[str, object]) -> None:
    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "figure.dpi": 140,
            "savefig.bbox": "tight",
        }
    )

    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.5))
    axes[0, 0].hist(df[TARGET], bins=28, color="#4C78A8", edgecolor="white")
    axes[0, 0].set_xlabel("Compressive strength (MPa)")
    axes[0, 0].set_ylabel("Mixtures")
    axes[0, 0].set_title("Target distribution")
    style_axes(axes[0, 0])

    axes[0, 1].hist(df["age"], bins=[0, 2, 4, 8, 15, 29, 57, 91, 181, 366], color="#F58518", edgecolor="white")
    axes[0, 1].set_xlabel("Age (days)")
    axes[0, 1].set_ylabel("Mixtures")
    axes[0, 1].set_title("Curing-age distribution")
    style_axes(axes[0, 1])

    corr = df[FEATURES + [TARGET]].corr(numeric_only=True)
    im = axes[1, 0].imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
    axes[1, 0].set_xticks(range(len(corr.columns)), [c.replace("_", "\n") for c in corr.columns], rotation=45, ha="right")
    axes[1, 0].set_yticks(range(len(corr.index)), [c.replace("_", "\n") for c in corr.index])
    axes[1, 0].set_title("Correlation matrix")
    fig.colorbar(im, ax=axes[1, 0], fraction=0.046, pad=0.04)

    missing = df[FEATURES + [TARGET]].isna().sum()
    axes[1, 1].barh([c.replace("_", " ") for c in missing.index], missing.values, color="#54A24B")
    axes[1, 1].set_xlabel("Missing values")
    axes[1, 1].set_title("Completeness check")
    style_axes(axes[1, 1])
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_dataset_overview.pdf")
    plt.close(fig)

    y_test: np.ndarray = model["y_test"]  # type: ignore[assignment]
    pred: np.ndarray = model["ridge_pred_test"]  # type: ignore[assignment]
    fig, ax = plt.subplots(figsize=(4.9, 4.6))
    ax.scatter(y_test, pred, s=20, alpha=0.72, color="#4C78A8", edgecolor="none")
    lims = [min(y_test.min(), pred.min()) - 2, max(y_test.max(), pred.max()) + 2]
    ax.plot(lims, lims, color="#222222", linewidth=1.0)
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_xlabel("Observed strength (MPa)")
    ax.set_ylabel("Predicted strength (MPa)")
    ax.set_title("Ridge parity on held-out test set")
    style_axes(ax)
    fig.savefig(FIG_DIR / "fig_parity_ridge.pdf")
    plt.close(fig)

    residual = y_test - pred
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.2))
    axes[0].scatter(pred, residual, s=20, alpha=0.72, color="#B279A2", edgecolor="none")
    axes[0].axhline(0, color="#222222", linewidth=1.0)
    axes[0].set_xlabel("Predicted strength (MPa)")
    axes[0].set_ylabel("Residual, observed - predicted (MPa)")
    axes[0].set_title("Residual pattern")
    style_axes(axes[0])
    axes[1].hist(residual, bins=24, color="#B279A2", edgecolor="white")
    axes[1].set_xlabel("Residual (MPa)")
    axes[1].set_ylabel("Test mixtures")
    axes[1].set_title("Residual distribution")
    style_axes(axes[1])
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig_residuals.pdf")
    plt.close(fig)

    ridge: FitResult = model["ridge"]  # type: ignore[assignment]
    coef = pd.DataFrame({"feature": FEATURES, "coefficient": ridge.beta[1:]})
    coef = coef.reindex(coef["coefficient"].abs().sort_values().index)
    fig, ax = plt.subplots(figsize=(5.3, 3.7))
    colors = np.where(coef["coefficient"] >= 0, "#54A24B", "#E45756")
    ax.barh(coef["feature"].str.replace("_", " "), coef["coefficient"], color=colors)
    ax.axvline(0, color="#222222", linewidth=1.0)
    ax.set_xlabel("Standardized ridge coefficient (MPa)")
    ax.set_title("Model coefficients")
    style_axes(ax)
    fig.savefig(FIG_DIR / "fig_coefficients.pdf")
    plt.close(fig)

    mean = model["mean"]  # type: ignore[assignment]
    scale = model["scale"]  # type: ignore[assignment]
    age_grid = np.linspace(df["age"].min(), df["age"].max(), 120)
    template = np.tile(df[FEATURES].median().to_numpy(float), (len(age_grid), 1))
    template[:, FEATURES.index("age")] = age_grid
    age_pred = apply_design(template, mean, scale) @ ridge.beta
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    ax.plot(age_grid, age_pred, color="#4C78A8", linewidth=2.0)
    ax.scatter(df["age"], df[TARGET], s=9, alpha=0.18, color="#777777", edgecolor="none")
    ax.set_xlabel("Age (days)")
    ax.set_ylabel("Predicted strength at median mixture (MPa)")
    ax.set_title("Age-response profile")
    style_axes(ax)
    fig.savefig(FIG_DIR / "fig_age_response.pdf")
    plt.close(fig)


def write_log(df: pd.DataFrame, model: dict[str, object], tables: dict[str, pd.DataFrame], messages: list[str]) -> None:
    ridge: FitResult = model["ridge"]  # type: ignore[assignment]
    train_idx: np.ndarray = model["train_idx"]  # type: ignore[assignment]
    test_idx: np.ndarray = model["test_idx"]  # type: ignore[assignment]
    source_label = str(df["source_label"].iloc[0])
    corr = df[FEATURES + [TARGET]].corr(numeric_only=True)[TARGET].drop(TARGET)
    top_corr = corr.abs().sort_values(ascending=False).index[0]
    ablation = tables["ablation"]
    strongest_ablation = ablation.iloc[0]

    lines = [
        "Example artifact generation log",
        "================================",
        "",
        f"Command: python example/scripts/generate_example_artifacts.py",
        f"Seed: {SEED}",
        f"Dataset rows: {len(df)}",
        f"Dataset source_label: {source_label}",
        f"Train rows: {len(train_idx)}",
        f"Test rows: {len(test_idx)}",
        f"Missing numeric values: {int(df[FEATURES + [TARGET]].isna().sum().sum())}",
        "",
        "Dataset acquisition:",
        *[f"- {message}" for message in messages],
        "",
        "Selected model:",
        f"- Ridge alpha: {ridge.alpha:g}",
        f"- Test RMSE: {ridge.test_metrics['RMSE']:.3f} MPa",
        f"- Test MAE: {ridge.test_metrics['MAE']:.3f} MPa",
        f"- Test R2: {ridge.test_metrics['R2']:.3f}",
        f"- Test bias: {ridge.test_metrics['Bias']:.3f} MPa",
        "",
        "Registry candidates:",
        f"- n_rows = {len(df)}",
        f"- n_features = {len(FEATURES)}",
        f"- train_rows = {len(train_idx)}",
        f"- test_rows = {len(test_idx)}",
        f"- target_mean_mpa = {df[TARGET].mean():.3f}",
        f"- target_sd_mpa = {df[TARGET].std(ddof=1):.3f}",
        f"- target_min_mpa = {df[TARGET].min():.3f}",
        f"- target_max_mpa = {df[TARGET].max():.3f}",
        f"- selected_ridge_alpha = {ridge.alpha:g}",
        f"- ridge_test_rmse_mpa = {ridge.test_metrics['RMSE']:.3f}",
        f"- ridge_test_mae_mpa = {ridge.test_metrics['MAE']:.3f}",
        f"- ridge_test_r2 = {ridge.test_metrics['R2']:.3f}",
        f"- ridge_test_bias_mpa = {ridge.test_metrics['Bias']:.3f}",
        f"- strongest_abs_target_correlation = {top_corr} ({corr[top_corr]:.3f})",
        f"- largest_ablation_delta_rmse_mpa = {strongest_ablation['Removed feature']} ({strongest_ablation['Delta RMSE (MPa)']:.3f})",
        "",
        "Generated figures:",
        *[f"- {(FIG_DIR / name).relative_to(ROOT)} ({(FIG_DIR / name).stat().st_size} bytes)" for name in GENERATED_FIGURES],
        "",
        "Generated tables:",
        *[f"- {(TABLE_DIR / name).relative_to(ROOT)} ({(TABLE_DIR / name).stat().st_size} bytes)" for name in GENERATED_TABLES],
        "",
        "Notes:",
        "- All modelling used pandas, numpy, and matplotlib only.",
        "- Fallback data, if present, are a deterministic pipeline exercise and not UCI observations.",
    ]
    LOG_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ensure_dirs()
    df, acquisition_messages = load_or_create_dataset()
    required = FEATURES + [TARGET, "source_label"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise SystemExit(f"Dataset missing required columns: {missing}")
    df = df[required].copy()
    model, model_messages = fit_models(df)
    messages = acquisition_messages + model_messages
    tables = make_tables(df, model)
    make_figures(df, model)
    write_log(df, model, tables, messages)
    print(f"Wrote dataset: {DATA_CSV}")
    print(f"Wrote figures: {FIG_DIR}")
    print(f"Wrote tables: {TABLE_DIR}")
    print(f"Wrote log: {LOG_PATH}")
    print(textwrap.dedent(
        f"""
        source_label={df['source_label'].iloc[0]}
        rows={len(df)}
        ridge_test_rmse={model['ridge'].test_metrics['RMSE']:.3f}
        ridge_test_r2={model['ridge'].test_metrics['R2']:.3f}
        """
    ).strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
