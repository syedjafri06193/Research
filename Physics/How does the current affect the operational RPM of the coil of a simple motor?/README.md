# ⚡ Effect of Current on RPM of a Simple DC Motor Coil

**Undergraduate Physics / Electrical Engineering Research Project**  
**Research Question:** *How does the supplied current affect the operational RPM of the coil in a simple DC motor?*

---

## Table of Contents

- [Overview](#overview)
- [Background Theory](#background-theory)
- [Hypothesis](#hypothesis)
- [Materials](#materials)
- [Experimental Setup](#experimental-setup)
- [Procedure](#procedure)
- [Data Collection](#data-collection)
- [Analysis](#analysis)
- [Results & Discussion](#results--discussion)
- [Sources of Error](#sources-of-error)
- [References](#references)
- [Project Structure](#project-structure)

---

## Overview

This experiment investigates the quantitative relationship between electrical current supplied to a simple DC motor and the resulting rotational speed (RPM) of its coil. A simple DC motor converts electrical energy into mechanical rotational motion using the interaction between a magnetic field and a current-carrying conductor. By systematically varying the input current and measuring the coil's RPM, we aim to establish whether this relationship is **linear**, **nonlinear**, or subject to saturation effects.

---

## Background Theory

### Lorentz Force & Motor Torque

The fundamental operation of a DC motor relies on the **Lorentz force law**:

```
F = I · L × B
```

Where:
- `F` = force on the conductor (N)
- `I` = current through the conductor (A)
- `L` = length of the conductor in the magnetic field (m)
- `B` = magnetic field strength (T)

The **torque** produced by the coil is:

```
τ = N · B · I · A · sin(θ)
```

Where:
- `τ` = torque (N·m)
- `N` = number of turns in the coil
- `A` = area of the coil (m²)
- `θ` = angle between coil plane and magnetic field

### RPM and Steady-State Equilibrium

At steady-state operation, motor torque equals the **load torque + friction torque**:

```
τ_motor = τ_load + τ_friction
```

Since `τ_motor ∝ I`, a higher current produces more torque, which — if friction and load remain constant — yields higher angular velocity ω (and thus higher RPM):

```
RPM = (60 · ω) / (2π)
```

For an **ideal** motor with no back-EMF consideration:

```
RPM ∝ I  (linear relationship expected)
```

In practice, back-EMF, coil resistance losses (I²R heating), and magnetic saturation introduce nonlinearities at higher currents.

### Back-EMF

As the motor spins, it generates a back-electromotive force (back-EMF):

```
ε_back = k · ω
```

This opposes the applied voltage and limits the net current at high speeds, creating a natural self-regulating behavior.

---

## Hypothesis

**If current supplied to the motor coil is increased, then the RPM will increase proportionally**, because the electromagnetic torque (τ = NBIA) is directly proportional to current. However, at higher currents, resistive heating and back-EMF may cause the RPM to plateau or deviate from linearity.

**Predicted relationship:** RPM = k · I + b (approximately linear for the range tested)

---

## Materials

| Item | Specification | Quantity |
|------|--------------|----------|
| Simple DC motor (hobby-grade) | 3–12V, single coil preferred | 1 |
| DC Power supply (variable) | 0–5A, 0–15V | 1 |
| Ammeter / Multimeter | ±0.01A precision | 1 |
| Digital tachometer | Non-contact (laser), ±1 RPM | 1 |
| Reflective tape | For tachometer target | 1 small strip |
| Connecting wires | Crocodile clips + banana plugs | As needed |
| Ruler / calipers | For coil dimension measurement | 1 |
| Compass or Gaussmeter | For B-field estimation (optional) | 1 |
| Cooling fan or heat sink | To manage resistive heating | 1 |
| Stopwatch | Backup timing | 1 |
| Graph paper / Laptop | For data logging | 1 |

---

## Experimental Setup

```
  [Variable DC Power Supply]
         |         |
      (+)           (-)
         \         /
          [Ammeter]
               |
           [DC Motor] ──── [Reflective tape on shaft]
                                      ↑
                             [Laser Tachometer]
                             reads RPM remotely
```

### Setup Steps

1. Mount the DC motor securely on a non-conducting surface (wood block or lab stand).
2. Attach a small strip of reflective tape to the motor shaft or a flywheel attached to it.
3. Position the laser tachometer 5–15 cm from the tape at a consistent angle.
4. Connect the ammeter **in series** with the motor and power supply.
5. Verify the voltmeter reads supply voltage **in parallel** with the motor terminals.
6. Begin with current at 0 A before any trial.

---

## Procedure

### Controlled Variables (must be kept constant)
- Motor identity (same motor throughout)
- Magnetic field strength (no external magnets altered)
- Ambient temperature (allow cooling between trials)
- Motor load (no additional mechanical load attached)
- Wire connections and resistance

### Independent Variable
- **Current (I)** supplied to the motor: varied from 0.1 A to 2.0 A in steps of 0.1 A (or as limited by motor specs)

### Dependent Variable
- **Rotational speed (RPM)** of the motor coil

### Trial Protocol

For each current setting:

1. Set the power supply to deliver the target current.
2. Allow the motor 30 seconds to reach **steady-state** operation.
3. Record RPM using the tachometer — take **5 readings** over 10 seconds.
4. Record the actual ammeter reading (may differ slightly from the set value).
5. Allow motor to cool for 60 seconds before the next trial (prevents thermal drift).
6. Increase current to the next step and repeat.
7. **Perform the entire sequence 3 times** (3 experimental runs total) for statistical reliability.

> ⚠️ **Safety Note:** Do not exceed the motor's rated voltage/current. Monitor motor temperature. If the casing becomes hot to touch, stop and allow cooling.

---

## Data Collection

Use the provided data template: [`data/raw_data_template.csv`](data/raw_data_template.csv)

### Data Table Format

| Trial | Run | Current_Set (A) | Current_Actual (A) | RPM_1 | RPM_2 | RPM_3 | RPM_4 | RPM_5 | RPM_Mean | RPM_StdDev |
|-------|-----|-----------------|--------------------|-------|-------|-------|-------|-------|----------|------------|
| 1 | 1 | 0.10 | — | — | — | — | — | — | — | — |
| 2 | 1 | 0.20 | — | ... | | | | | | |
| ... | | | | | | | | | | |

Fill in the CSV file as you collect data. The analysis script will calculate means and standard deviations automatically.

---

## Analysis

Run the provided Python analysis script after data collection:

```bash
cd scripts/
pip install -r requirements.txt
python analyze_motor.py ../data/raw_data.csv
```

The script will:
1. Calculate mean RPM and uncertainty for each current value
2. Plot **RPM vs. Current** with error bars
3. Perform a **linear regression** (and optional polynomial fit)
4. Output the slope (k), intercept, and R² value
5. Save figures to `figures/`

See [`scripts/README_scripts.md`](scripts/README_scripts.md) for full documentation.

---

## Results & Discussion

*(Fill in after experiment)*

### Expected Results

Based on theory, a roughly linear relationship is expected:

```
RPM = k · I + b
```

- **k** (slope) depends on motor construction (N, B, A, friction coefficient)
- **b** (intercept) may be slightly negative due to static friction requiring a threshold current to start spinning

### Discussion Points to Address

1. Is the relationship linear across all tested currents?
2. At what current does the motor reach maximum stable RPM?
3. Do you observe a **starting threshold** current below which the motor does not spin?
4. How do the three experimental runs compare? (Reproducibility)
5. How does back-EMF influence the results at higher currents?
6. What are the main sources of experimental uncertainty?

---

## Sources of Error

| Source | Type | Mitigation |
|--------|------|------------|
| Tachometer reading fluctuation | Random | Average 5 readings per trial |
| Motor heating (resistance increase) | Systematic | Cool-down periods between trials |
| Voltage/current supply fluctuation | Random | Read ammeter directly each trial |
| Reflective tape wobble | Random | Secure tape tightly; use flywheel |
| Friction variability (bearing wear) | Systematic | Use same motor; run in same direction |
| Magnetic field variation | Systematic | Use same motor; no external B-field sources nearby |

---

## References

1. Serway, R. A., & Jewett, J. W. (2018). *Physics for Scientists and Engineers* (10th ed.). Cengage Learning. Ch. 29–30.
2. Halliday, D., Resnick, R., & Krane, K. S. (2002). *Physics* (5th ed.). John Wiley & Sons. Ch. 32.
3. Hughes, A., & Drury, B. (2019). *Electric Motors and Drives: Fundamentals, Types and Applications* (5th ed.). Newnes.
4. Griffiths, D. J. (2017). *Introduction to Electrodynamics* (4th ed.). Cambridge University Press. Ch. 5, 7.
5. Mohan, N. (2012). *Power Electronics: Converters, Applications, and Design* (3rd ed.). Wiley.

---

## Project Structure

```
motor-rpm-research/
│
├── README.md                        ← This file
├── lab_report_template.md           ← Formal report template
│
├── data/
│   ├── raw_data_template.csv        ← Blank data sheet to fill in
│   ├── raw_data.csv                 ← Your filled-in data (add here)
│   └── sample_data.csv              ← Example dataset for testing scripts
│
├── scripts/
│   ├── analyze_motor.py             ← Main analysis & plotting script
│   ├── requirements.txt             ← Python dependencies
│   └── README_scripts.md            ← Script documentation
│
├── figures/                         ← Auto-generated plots saved here
│   └── (generated by scripts)
│
└── docs/
    ├── theory_notes.md              ← Extended theory and derivations
    └── safety_checklist.md          ← Pre-experiment safety checklist
```

---

*Last updated: May 2026 | Undergraduate Physics/EE Lab Research*
