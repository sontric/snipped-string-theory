import numpy as np
from spiral_unification.core import harmony_score, energy_from_frequency, mass_from_energy

def test_harmony_score():
    t = np.linspace(0, 2*np.pi, 1000)
    golden = np.sin(t)
    test_signal = np.sin(t + 0.1)
    score = harmony_score(test_signal, golden)
    assert 0.9 < score < 1.0

def test_energy_to_mass():
    frequency = 5e14  # visible light
    E = energy_from_frequency(frequency)
    m = mass_from_energy(E)
    assert 0 < m < 1e-30

def test_breaks_if_disharmonic():
    t = np.linspace(0, 2*np.pi, 1000)
    broken_signal = np.random.rand(1000)
    golden = np.sin(t)
    score = harmony_score(broken_signal, golden)
    assert score < 0.5
