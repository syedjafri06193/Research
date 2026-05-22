# Lab Report: Effect of Current on DC Motor Coil RPM

**Student Name:** ___________________________  
**Student ID:** ___________________________  
**Course:** ___________________________  
**Instructor:** ___________________________  
**Date:** ___________________________  
**Lab Partner(s):** ___________________________  

---

## 1. Abstract

*(~150 words. Write after all other sections are complete.)*

Briefly summarize: the research question, the experimental method, the key quantitative result (slope, R²), and whether the hypothesis was supported. Do not include figures in the abstract.

---

## 2. Introduction

### 2.1 Background and Motivation

*(Why does this experiment matter? What real-world applications does DC motor speed control have?)*

### 2.2 Theory

Present the relevant equations:

- Lorentz force: `F = IL × B`
- Motor torque: `τ = NBIA·sin(θ)`
- Expected RPM relationship: `RPM ∝ I`
- Back-EMF: `ε_back = kω`

Explain in your own words how these lead to the prediction that RPM increases with current.

### 2.3 Research Question

> **How does the current supplied to a simple DC motor coil affect its operational RPM?**

### 2.4 Hypothesis

State your specific, testable hypothesis with predicted direction and form of relationship.

---

## 3. Method

### 3.1 Materials

List all equipment used with specifications (see README.md Materials section for template).

### 3.2 Experimental Setup

Include a diagram or photograph of your setup. Label key components.

### 3.3 Variables

| Variable | Description |
|----------|-------------|
| **Independent** | Current (A), varied from ___ to ___ A in ___ A steps |
| **Dependent** | RPM of motor coil |
| **Controlled** | Motor identity, magnetic field, load, ambient temperature |

### 3.4 Procedure

Describe step-by-step what you did (refer to the procedure in README.md, but write in past tense for your report).

### 3.5 Data Collection Protocol

- Number of trials per current value: ___
- Number of experimental runs: ___
- Cool-down time between trials: ___ seconds
- Tachometer sampling method: ___

---

## 4. Results

### 4.1 Raw Data Summary

*(Insert your completed data table here, or reference the CSV file.)*

### 4.2 Calculated Values

For each current level, report:

| Current (A) | Mean RPM (all runs) | SEM | 95% CI |
|------------|---------------------|-----|--------|
| 0.10 | | | |
| ... | | | |

### 4.3 Figures

**Figure 1:** RPM vs Current (main scatter plot with regression lines)

*(Insert `figures/rpm_vs_current.png` here)*

**Figure 2:** Individual Runs Comparison

*(Insert `figures/rpm_vs_current_runs.png` here)*

**Figure 3:** Residuals from Linear Fit

*(Insert `figures/residuals.png` here)*

### 4.4 Regression Results

| Model | Equation | R² | p-value |
|-------|----------|-----|---------|
| Linear | RPM = ___ · I + ___ | | |
| Quadratic | RPM = ___I² + ___I + ___ | | |
| Saturation | RPM_max = ___, k = ___ | | |

---

## 5. Discussion

### 5.1 Interpretation of Results

- Was the relationship between current and RPM linear? Over what range?
- What does the slope (RPM/A) tell you about your specific motor?
- Was there a threshold current before the motor began spinning? What does this imply?

### 5.2 Comparison with Theory

- How do your results compare to the theoretical prediction (`RPM ∝ I`)?
- At high currents, does the RPM plateau? What physical mechanism explains this?

### 5.3 Reproducibility

- How well did the three runs agree with each other? Report the average SEM as a percentage of mean RPM.
- What factors might explain any run-to-run variation?

### 5.4 Sources of Error

*(Fill in the error analysis table from README.md with your actual observed magnitudes.)*

### 5.5 Improvements

Suggest at least two specific improvements to the experimental design that would reduce uncertainty or extend the investigation.

---

## 6. Conclusion

*(~100–150 words.)*

State clearly:
1. Whether your hypothesis was supported
2. The quantitative relationship found (include the equation and R²)
3. The physical explanation for any observed nonlinearity
4. The significance of the finding in the context of motor design

---

## 7. References

*(Use APA or the format specified by your instructor. Minimum 3 sources.)*

1. 
2. 
3. 

*(See README.md for suggested references.)*

---

## Appendix

### A. Raw Data Tables

*(Attach or paste full raw data CSV.)*

### B. Sample Calculations

Show one worked example of:
- Mean RPM calculation
- SEM calculation
- Linear regression by hand (for one pair of points, as a check)

### C. Equipment Calibration Notes

*(Record any calibration steps taken, tachometer model, ammeter model, supply model.)*
