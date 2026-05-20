# Theory Notes: DC Motor Physics

## 1. The Simple DC Motor

A simple DC motor consists of:
- A **stator** — the fixed part containing permanent magnets producing field **B**
- A **rotor (armature)** — a coil of wire that rotates within the field
- A **commutator** — a split-ring that reverses current direction each half-turn, maintaining consistent torque direction

---

## 2. Force on a Current-Carrying Conductor

The **Lorentz force** on a current-carrying wire in a magnetic field:

```
F = I (L × B)
|F| = I · L · B · sin(α)
```

Where α is the angle between the wire direction and B.

For a rectangular coil of width `w` and height `h` in a uniform field:
- The two sides of length `h` parallel to the rotation axis experience force
- The two sides of length `w` perpendicular to the axis contribute to torque

---

## 3. Torque on a Current Loop

The torque on a single rectangular loop:

```
τ = I · A · B · sin(θ)
```

Where:
- `A = w × h` = area of the coil
- `θ` = angle between the coil's normal vector and B
- Maximum torque at θ = 90° (coil plane parallel to B)

For `N` turns:

```
τ = N · I · A · B · sin(θ)
```

The commutator ensures the average torque over a full rotation is non-zero by keeping the effective θ near 90°.

---

## 4. Equations of Motion

### Newton's Second Law (rotational):

```
τ_net = J · (dω/dt)
```

Where:
- `J` = moment of inertia of the rotor (kg·m²)
- `ω` = angular velocity (rad/s)

### At steady state (dω/dt = 0):

```
τ_motor = τ_friction + τ_load
N·I·A·B = τ_friction + τ_load
```

If τ_friction and τ_load are approximately constant:

```
I ∝ (τ_friction + τ_load) / (N·A·B) = constant
```

This means **I determines the torque**, but it's ω that balances back-EMF (see below).

---

## 5. Back-EMF and Speed Regulation

As the coil rotates, it acts as a generator and produces a **back-EMF**:

```
ε_back = N · B · A · ω = k_e · ω
```

The **net current** through the motor is:

```
I = (V_supply - ε_back) / R_armature
I = (V - k_e·ω) / R
```

At steady state, solving for ω:

```
ω = (V - I·R) / k_e
RPM = (60/2π) · (V - I·R) / k_e
```

Or equivalently, since `V = I·R + k_e·ω`:

```
ω = V/(k_e) - (R/k_e)·I
```

This shows a **linear decrease in RPM with increasing load current** (when voltage is fixed), and a **linear increase in RPM with voltage** (at fixed load). 

For our experiment (varying I through a variable supply at variable V, with no mechanical load beyond friction):

```
τ_motor = k_t · I   (k_t = torque constant)
At equilibrium: k_t · I = τ_friction
ω_steady = (V - I·R) / k_e
```

If we increase I by raising V:

```
Higher I → Higher V → Higher (V - IR) / k_e → Higher ω → Higher RPM
```

This is why **RPM increases with current** in our experiment (both I and V increase together through the supply).

---

## 6. Nonlinearities

### Resistive Heating (I²R)
- At high currents, the coil heats up: `P_heat = I²·R`
- Resistance increases with temperature: `R(T) = R₀[1 + α(T - T₀)]`
- This reduces net current for a given voltage, limiting RPM growth

### Magnetic Saturation
- The permanent magnet field B is fixed
- But in motors with iron cores, the iron can saturate at high B, reducing effective torque constant k_t

### Static & Dynamic Friction
- A minimum current (threshold) is needed to overcome static friction before the motor starts
- This explains the near-zero RPM at very low currents

---

## 7. Motor Constants Summary

| Symbol | Name | Unit | Typical Value (hobby motor) |
|--------|------|------|-----------------------------|
| k_t | Torque constant | N·m/A | 0.01 – 0.05 |
| k_e | Back-EMF constant | V·s/rad | 0.01 – 0.05 |
| R | Armature resistance | Ω | 1 – 10 |
| J | Rotor inertia | kg·m² | 10⁻⁶ – 10⁻⁴ |
| N | Number of turns | — | 50 – 500 |

Note: In SI units, `k_t = k_e` (they are the same constant, just expressed in different unit systems).

---

## 8. Expected Graph Shape

Given the theory, the RPM vs Current graph should show:

1. **Zero RPM** up to a threshold current I_min (overcoming static friction)
2. **Approximately linear rise** in the moderate current range
3. **Gradual plateau** at high currents due to back-EMF and resistive heating
4. Possibly a **maximum safe RPM** beyond which the motor overheats or bearings fail

This gives a characteristic **S-curve** shape, though for a narrow current range it often appears approximately linear.
