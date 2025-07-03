import numpy as np

def harmony_score(signal, golden):
    return 1 - np.mean(np.abs(signal - golden)) / np.max(np.abs(golden))

def energy_from_frequency(frequency, score=1.0):
    h = 6.626e-34  # Planck constant
    return h * frequency * score

def mass_from_energy(E):
    c = 3e8
    return E / c**2
