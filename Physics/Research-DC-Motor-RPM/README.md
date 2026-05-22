# DC Motor RPM Research

**How does current affect the operational RPM of the coil of a simple motor?**

This research was conducted as part of undergraduate studies at the **University of Washington**, under the supervision of **Benjamin Grossman**.

---

## Overview

This project investigates the relationship between electrical current and the rotational speed (RPM) of a simple DC motor coil. By systematically varying current input and measuring motor RPM, this study aims to characterize and model the current–RPM relationship.

---

## Repository Contents

| File | Description |
|------|-------------|
| `README.md` | Project overview and documentation |
| `analyze_motor.py` | Python script for data analysis and visualization |
| `raw_data_template.csv` | Template for recording experimental measurements |
| `sample_data.csv` | Sample dataset used for testing and analysis |
| `theory_notes.md` | Theoretical background and physics principles |
| `lab_report_template.md` | Template for the formal lab report |
| `safety_checklist.md` | Lab safety guidelines and checklist |
| `rpm_vs_current.png` | Plot of RPM vs. current (averaged across runs) |
| `rpm_vs_current_runs.png` | Plot of RPM vs. current (individual runs) |
| `residuals.png` | Residuals plot from regression analysis |
| `IMG_0299.HEIC` | Experimental setup photo |
| `Photos/` | Additional lab photos |

---

## Methodology

1. Assembled a simple DC motor with a coil in a magnetic field
2. Varied the input current across multiple controlled values
3. Measured RPM at each current level across repeated trials
4. Analyzed data using linear regression (`analyze_motor.py`)
5. Visualized results and residuals to evaluate the model fit

---

## Key Findings

See `rpm_vs_current.png` and the lab report for results. Preliminary analysis suggests a positive linear relationship between current and RPM under the tested conditions.

---

## How to Run the Analysis

```bash
pip install pandas matplotlib numpy scipy
python analyze_motor.py
```

---

## Acknowledgments

Research conducted under the guidance of **Benjamin Grossman** at the **University of Washington**.
