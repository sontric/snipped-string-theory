import numpy as np
import allure
from spiral_unification.core import harmony_score, energy_from_frequency, mass_from_energy

@allure.title("Test Harmony Score")
@allure.description("""
This test compares two sinusoidal signals:
- Ref  signal:   r(t) = sin(t)
- Test signal:   s(t) = sin(t + 0.1)
The harmony score is expected to be close to 1.0 for a small phase shift.
Equation:
Harmony = 1 - avg(|s(t) - r(t)|) / max(|r(t)|)
""")
def test_harmony():
    t = np.linspace(0, 2*np.pi, 1000)
    golden = np.sin(t)
    test_signal = np.sin(t + 0.1)
    score = harmony_score(test_signal, golden)
    allure.attach(str(score), name="Harmony Score", attachment_type=allure.attachment_type.TEXT)
    assert 0.9 < score < 1.0

@allure.title("Test Breaks If Disharmonic")
@allure.description("""
Disharmonic Signal Test
This test compares noise to a sin, and should return a harmony score of < 0.5:
- Ref  signal:   r(t) = sin(t)
- Test signal:   s(t) = random_noise
The harmony score is expected to be less than 0.5.
Equation:
Harmony = 1 - avg(|s(t) - r(t)|) / max(|r(t)|)
""")
def test_disharmony():
    t = np.linspace(0, 2*np.pi, 1000)
    broken_signal = np.random.rand(1000)
    golden = np.sin(t)
    score = harmony_score(broken_signal, golden)
    allure.attach(str(score), name="Disharmony Score", attachment_type=allure.attachment_type.TEXT)
    assert score < 0.5

@allure.title("Test Energy to Mass Conversion")
@allure.description("""
Energy-Mass Conversion Test
Verifies that mass computed from frequency via Planck's and Einstein's equations is in expected range.
- Planck’s relation: E = h * f
- Einstein’s mass-energy equivalence:  m = E / c^2
- For f = [FIX ME]
""")
def test_energy_to_mass():
    frequency = 5e14  # Hz
    E = energy_from_frequency(frequency)
    m = mass_from_energy(E)
    allure.attach(f"Energy: {E} J\nMass: {m} kg", name="Energy & Mass", attachment_type=allure.attachment_type.TEXT)
    assert 0 < m < 1e-30
