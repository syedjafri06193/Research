#!/usr/bin/env python3
"""
analyze_motor.py
================
Analyzes the effect of current on DC motor coil RPM.

Usage:
    python analyze_motor.py <path_to_data.csv>

Example:
    python analyze_motor.py ../data/sample_data.csv

Outputs:
    - Console summary statistics
    - figures/rpm_vs_current.png      — main scatter + fit plot
    - figures/rpm_vs_current_runs.png — individual run comparison
    - figures/residuals.png           — residuals from linear fit
    - analysis_results.txt            — numerical results summary
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats
from scipy.optimize import curve_fit

# ── Output directory ────────────────────────────────────────────────────────
FIGURES_DIR = os.path.join(os.path.dirname(__file__), '..', 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)

# ── Plotting style ───────────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': '#0f0f1a',
    'axes.facecolor':   '#1a1a2e',
    'axes.edgecolor':   '#444466',
    'axes.labelcolor':  '#e0e0ff',
    'xtick.color':      '#aaaacc',
    'ytick.color':      '#aaaacc',
    'text.color':       '#e0e0ff',
    'grid.color':       '#2a2a4a',
    'grid.linestyle':   '--',
    'grid.alpha':       0.5,
    'font.family':      'monospace',
    'axes.titlepad':    14,
})

RUN_COLORS = ['#00d4ff', '#ff6b9d', '#a8ff78']
ACCENT     = '#ffd700'


# ── Helper functions ─────────────────────────────────────────────────────────

def load_data(filepath):
    """Load and validate the CSV data file."""
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower()

    # Auto-calculate mean & stddev if columns are empty / missing
    rpm_cols = ['rpm_1', 'rpm_2', 'rpm_3', 'rpm_4', 'rpm_5']
    if all(c in df.columns for c in rpm_cols):
        df['rpm_mean']   = df[rpm_cols].mean(axis=1)
        df['rpm_stddev'] = df[rpm_cols].std(axis=1, ddof=1)

    return df


def aggregate_runs(df):
    """
    Average across all runs for each current_set level.
    Returns a clean DataFrame with one row per current value.
    """
    agg = df.groupby('current_set_a').agg(
        rpm_mean_all=('rpm_mean', 'mean'),
        rpm_sem=('rpm_mean', lambda x: x.std(ddof=1) / np.sqrt(len(x))),
        current_actual_mean=('current_actual_a', 'mean'),
    ).reset_index()
    return agg


def linear_model(x, m, b):
    return m * x + b


def saturation_model(x, rpm_max, k, x0):
    """Logistic-style saturation model for high-current nonlinearity."""
    return rpm_max / (1 + np.exp(-k * (x - x0)))


def fit_models(current, rpm, rpm_err):
    """Fit linear and saturation models; return fit parameters."""
    # Mask out zero-RPM (below-threshold) points for fitting
    mask = rpm > 0
    x = current[mask]
    y = rpm[mask]
    w = 1.0 / (rpm_err[mask] + 1e-6)   # weights = 1/uncertainty

    # Linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    lin_params = {'slope': slope, 'intercept': intercept,
                  'r2': r_value**2, 'p': p_value, 'slope_err': std_err}

    # Polynomial (degree 2) fit
    poly_coeffs = np.polyfit(x, y, 2)
    poly_fn = np.poly1d(poly_coeffs)
    poly_r2 = 1 - np.sum((y - poly_fn(x))**2) / np.sum((y - np.mean(y))**2)

    # Saturation fit (try/except in case it doesn't converge)
    try:
        p0 = [max(y)*1.2, 5.0, np.median(x)]
        sat_params, _ = curve_fit(saturation_model, x, y, p0=p0, maxfev=5000)
        sat_y = saturation_model(x, *sat_params)
        sat_r2 = 1 - np.sum((y - sat_y)**2) / np.sum((y - np.mean(y))**2)
    except Exception:
        sat_params = None
        sat_r2 = None

    return lin_params, (poly_coeffs, poly_r2), (sat_params, sat_r2)


# ── Plot 1: RPM vs Current (main result) ─────────────────────────────────────

def plot_main(agg, lin_params, poly_info, sat_info):
    poly_coeffs, poly_r2 = poly_info
    sat_params, sat_r2   = sat_info

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#0f0f1a')

    current = agg['current_set_a'].values
    rpm     = agg['rpm_mean_all'].values
    err     = agg['rpm_sem'].values

    # Scatter with error bars
    ax.errorbar(current, rpm, yerr=err, fmt='o', color=ACCENT,
                ecolor='#888888', elinewidth=1.2, capsize=4,
                markersize=6, zorder=5, label='Measured RPM (mean ± SEM)')

    x_fit = np.linspace(current[current > 0].min(), current.max(), 300)

    # Linear fit line
    y_lin = lin_params['slope'] * x_fit + lin_params['intercept']
    ax.plot(x_fit, y_lin, color='#00d4ff', linewidth=2,
            label=f"Linear fit  (R²={lin_params['r2']:.4f})\n"
                  f"  RPM = {lin_params['slope']:.1f}·I + {lin_params['intercept']:.1f}")

    # Polynomial fit
    poly_fn = np.poly1d(poly_coeffs)
    ax.plot(x_fit, poly_fn(x_fit), color='#ff6b9d', linewidth=1.5,
            linestyle='--', label=f'Quadratic fit (R²={poly_r2:.4f})')

    # Saturation fit (if converged)
    if sat_params is not None:
        ax.plot(x_fit, saturation_model(x_fit, *sat_params),
                color='#a8ff78', linewidth=1.5, linestyle=':',
                label=f'Saturation fit (R²={sat_r2:.4f})')

    ax.set_xlabel('Current (A)', fontsize=12)
    ax.set_ylabel('RPM', fontsize=12)
    ax.set_title('Effect of Current on DC Motor Coil RPM', fontsize=14, fontweight='bold')
    ax.legend(fontsize=9, loc='upper left', framealpha=0.3,
              facecolor='#1a1a2e', edgecolor='#444466')
    ax.grid(True)

    # Annotation box
    info = (f"Slope: {lin_params['slope']:.1f} RPM/A\n"
            f"p-value: {lin_params['p']:.2e}\n"
            f"R²: {lin_params['r2']:.4f}")
    ax.text(0.97, 0.05, info, transform=ax.transAxes, fontsize=9,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='#0f0f1a', alpha=0.8,
                      edgecolor='#444466'), color='#e0e0ff')

    plt.tight_layout()
    out = os.path.join(FIGURES_DIR, 'rpm_vs_current.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"  ✔ Saved: {out}")
    plt.close()


# ── Plot 2: Individual runs ───────────────────────────────────────────────────

def plot_runs(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#0f0f1a')

    runs = sorted(df['run'].unique())
    for i, run in enumerate(runs):
        sub = df[df['run'] == run].sort_values('current_set_a')
        ax.plot(sub['current_set_a'], sub['rpm_mean'],
                color=RUN_COLORS[i % len(RUN_COLORS)],
                marker='o', markersize=4, linewidth=1.8,
                label=f'Run {run}')

    ax.set_xlabel('Current (A)', fontsize=12)
    ax.set_ylabel('Mean RPM', fontsize=12)
    ax.set_title('RPM vs Current — Individual Experimental Runs', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, framealpha=0.3, facecolor='#1a1a2e', edgecolor='#444466')
    ax.grid(True)

    plt.tight_layout()
    out = os.path.join(FIGURES_DIR, 'rpm_vs_current_runs.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"  ✔ Saved: {out}")
    plt.close()


# ── Plot 3: Residuals ────────────────────────────────────────────────────────

def plot_residuals(agg, lin_params):
    current = agg['current_set_a'].values
    rpm     = agg['rpm_mean_all'].values
    mask    = rpm > 0

    y_pred    = lin_params['slope'] * current[mask] + lin_params['intercept']
    residuals = rpm[mask] - y_pred

    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor('#0f0f1a')

    ax.scatter(current[mask], residuals, color=ACCENT, s=60, zorder=5)
    ax.axhline(0, color='#00d4ff', linewidth=1.5, linestyle='--')
    ax.fill_between(current[mask], residuals, 0,
                    where=(residuals > 0), alpha=0.15, color='#00d4ff')
    ax.fill_between(current[mask], residuals, 0,
                    where=(residuals < 0), alpha=0.15, color='#ff6b9d')

    ax.set_xlabel('Current (A)', fontsize=12)
    ax.set_ylabel('Residual RPM', fontsize=12)
    ax.set_title('Residuals from Linear Fit (Observed − Predicted)', fontsize=13, fontweight='bold')
    ax.grid(True)

    plt.tight_layout()
    out = os.path.join(FIGURES_DIR, 'residuals.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"  ✔ Saved: {out}")
    plt.close()


# ── Text results summary ─────────────────────────────────────────────────────

def save_results(agg, lin_params, poly_info, sat_info):
    poly_coeffs, poly_r2 = poly_info
    sat_params, sat_r2   = sat_info

    lines = [
        "=" * 60,
        "  DC MOTOR RPM vs CURRENT — ANALYSIS RESULTS",
        "=" * 60,
        "",
        "AGGREGATED DATA (averaged across all runs):",
        f"{'Current (A)':>12}  {'Mean RPM':>10}  {'SEM':>8}",
        "-" * 35,
    ]
    for _, row in agg.iterrows():
        lines.append(f"{row['current_set_a']:>12.2f}  {row['rpm_mean_all']:>10.1f}  {row['rpm_sem']:>8.1f}")

    lines += [
        "",
        "LINEAR FIT  (RPM = slope·I + intercept)",
        f"  Slope     : {lin_params['slope']:.2f} RPM/A  (±{lin_params['slope_err']:.2f})",
        f"  Intercept : {lin_params['intercept']:.2f} RPM",
        f"  R²        : {lin_params['r2']:.4f}",
        f"  p-value   : {lin_params['p']:.4e}",
        "",
        "QUADRATIC FIT",
        f"  Coefficients: {poly_coeffs}",
        f"  R²          : {poly_r2:.4f}",
        "",
    ]
    if sat_params is not None:
        lines += [
            "SATURATION MODEL  (logistic)",
            f"  RPM_max : {sat_params[0]:.1f}",
            f"  k       : {sat_params[1]:.3f}",
            f"  x0      : {sat_params[2]:.3f} A",
            f"  R²      : {sat_r2:.4f}",
            "",
        ]

    lines += ["=" * 60, ""]

    result_text = "\n".join(lines)
    print("\n" + result_text)

    out = os.path.join(os.path.dirname(__file__), '..', 'analysis_results.txt')
    with open(out, 'w') as f:
        f.write(result_text)
    print(f"  ✔ Saved: {out}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_motor.py <data_file.csv>")
        print("Example: python analyze_motor.py ../data/sample_data.csv")
        sys.exit(1)

    filepath = sys.argv[1]
    print(f"\n📂 Loading data from: {filepath}")
    df = load_data(filepath)
    print(f"   Rows loaded: {len(df)}, Runs: {df['run'].nunique()}")

    print("\n📊 Aggregating runs...")
    agg = aggregate_runs(df)

    current = agg['current_set_a'].values
    rpm     = agg['rpm_mean_all'].values
    err     = agg['rpm_sem'].values

    print("🔢 Fitting models...")
    lin_params, poly_info, sat_info = fit_models(current, rpm, err)

    print("\n🖼  Generating figures...")
    plot_main(agg, lin_params, poly_info, sat_info)
    plot_runs(df)
    plot_residuals(agg, lin_params)

    save_results(agg, lin_params, poly_info, sat_info)
    print("\n✅ Analysis complete.\n")


if __name__ == '__main__':
    main()
