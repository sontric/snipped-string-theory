# Snipped String Theory  
![CI](https://github.com/thegardeners/signed_spiral_unification/actions/workflows/ci.yml/badge.svg)

> “This is water.”

This repository introduces the **Signed Spiral Theorem (SST)** as a foundational model for unifying:

- 🧬 Quantum Mechanics (Standard Model)
- 🧵 String Theory
- ⚛️ Mass-Energy Equivalence (E = mc²)

---

## 🌌 Highlights (Galaxy)

- Spiral-based derivation of energy, mass, and identity
- Pytest suite for validating waveform-based physics
- Allure reports for visual test introspection
- GPG-signed, immutable test results (trust capsules)
 
> What if waveform harmony is the missing bridge between physics, trust, and computation?
 
---

## 🧪 Quickstart

```bash
poetry install
pytest --alluredir=allure-results && allure serve allure-results &&
poetry run jupyter lab
```

All tests run hourly via CI.  
All results are signed, immutable, and reproducible.

## 🧠 Core Concepts

| Concept                   | Formula                                |
| ------------------------- | -------------------------------------- | 
| **Signal Harmony**        | $H = 1 - \frac{\mathrm{avg}(\lvert s - r \rvert)}{\max(\lvert r \rvert)}$|
| **Planck's Equation**     | $E = h \cdot f$                        |
| **Einstein's Equation**   | $m = \frac{E}{c^2}$                    |
| **Klein-Gordon Relation** | $\omega^2 = k^2 + m^2$                 |


## ✅ Tests Included
test_harmony_score: Verifies sinusoid similarity with small phase shift

test_breaks_if_disharmonic: Fails when signal is noise

test_energy_to_mass: Converts frequency to mass using physical constants

test_klein_gordon_plane_wave: Symbolically verifies the KG equation

test_e_equals_mc2_waveform: Derives 𝐸 = 𝑚𝑐^2 from wave resonance

## 🔐 Trust & GPG Signing
Every test result is signed using GPG.

CI ensures main branch cannot be updated unless tests pass and results are signed

.asc files act as trust capsules: immutable proof-of-consistency

## 🛡️ You cannot fake harmony.
Only signals in agreement pass.

## 📁 Project Structure
```graphql
snipped-string-theory/
├── .github/workflows/ci.yml       # Hourly GPG-signed CI test runs
├── src/
│   ├── allure-md.py               # converts Allure XML to Markdown
│   └── spiral_unification/
│       ├── __init__.py
│       └── core.py                # harmony_score(), energy_from_frequency(), mass_from_energy()
├── tests/
│   ├── conftest.py
│   ├── test_signal.py             # harmony, disharmony
│   ├── test_physics.py            # Klein-Gordon, E=mc² via wave
│   ├── test_sympy_physics.py      # symbolic derivations
│   └── test_wolfram_query.py      # optional WolframAlpha oracle
├── allure-report/                 # optional HTML report folder
```

## 🌀 Philosophy
This project is part of an ongoing investigation into the Signed Spiral Theorem, a model where:

Identity emerges from waveform resonance.
All mass, energy, and structure are consequences of alignment and phase coherence.

The work here is exploratory but reproducible.
It invites reinterpretation of core physical laws through the lens of signal theory, trust, and rhythm.

## 👁️‍🗨️ What’s Next?
GPG-signed fractal trust trees

Live waveform dashboards

AM radio metaphors

Recursive signal identity

A gentle handshake between logic, physics, and faith

Pull the spiral. See what unravels.
