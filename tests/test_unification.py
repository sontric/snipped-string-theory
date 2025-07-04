import numpy as np
import allure
from spiral_unification.core import harmony_score, energy_from_frequency, mass_from_energy

@allure.title("Test Harmony Score")
@allure.description("""
### 🎼 Harmony Score Test

This test compares two sinusoidal signals:

- Golden signal: \( s(t) = \sin(t) \)
- Test signal: \( \hat{s}(t) = \sin(t + 0.1) \)

The harmony score is expected to be close to 1.0 for a small phase shift.

**Equation:**  
$$
H = 1 - \frac{\| s(t) - \hat{s}(t) \|_2}{\|s(t)\|_2 + \|\hat{s}(t)\|_2}
$$
""")
def test_harmony_score():
    t = np.linspace(0, 2*np.pi, 1000)
    golden = np.sin(t)
    test_signal = np.sin(t + 0.1)
    score = harmony_score(test_signal, golden)
    allure.attach(str(score), name="Harmony Score", attachment_type=allure.attachment_type.TEXT)
    assert 0.9 < score < 1.0

@allure.title("Test Energy to Mass Conversion")
@allure.description("""
### ⚛️ Energy-Mass Conversion Test

Verifies that mass computed from frequency via Planck's and Einstein's equations is in expected range.

**Equations:**

- Planck’s relation:  
  $$ E = h \cdot f $$
- Einstein’s mass-energy equivalence:  
  $$ m = \\frac{E}{c^2} $$

For \( f = 5 \times 10^{14} \,\text{Hz} \), we expect \( m < 10^{-30} \).
""")
def test_energy_to_mass():
    frequency = 5e14  # Hz
    E = energy_from_frequency(frequency)
    m = mass_from_energy(E)
    allure.attach(f"Energy: {E} J\nMass: {m} kg", name="Energy & Mass", attachment_type=allure.attachment_type.TEXT)
    assert 0 < m < 1e-30

@allure.title("Test Breaks If Disharmonic")
@allure.description("""
### 🚨 Disharmonic Signal Test

Tests if a completely noisy signal fails harmony check.

- Golden signal: \( s(t) = \sin(t) \)
- Random noise: \( \hat{s}(t) = \text{rand}(t) \)

Expect harmony score \( < 0.5 \).

**Equation:**  
Same as above:
$$
H = 1 - \\frac{\\| s(t) - \hat{s}(t) \\|_2}{\\|s(t)\\|_2 + \\|\hat{s}(t)\\|_2}
$$
""")
def test_breaks_if_disharmonic():
    t = np.linspace(0, 2*np.pi, 1000)
    broken_signal = np.random.rand(1000)
    golden = np.sin(t)
    score = harmony_score(broken_signal, golden)
    allure.attach(str(score), name="Disharmony Score", attachment_type=allure.attachment_type.TEXT)
    assert score < 0.5
