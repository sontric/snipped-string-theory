from sympy import symbols, exp, I, simplify, Eq, solve, diff, simplify, Function
from sympy.abc import t, x

def test_klein_gordon_plane_wave():
    m, k, omega = symbols("m k omega", real=True, positive=True)
    phi = exp(-I * (omega * t - k * x))

    d2_phi_dt2 = phi.diff(t, 2)
    d2_phi_dx2 = phi.diff(x, 2)

    kg_expr = d2_phi_dt2 - d2_phi_dx2 + m**2 * phi
    kg_expr_sub = kg_expr.subs(omega**2, k**2 + m**2)

    assert simplify(kg_expr_sub) == 0

def test_e_equals_mc2_waveform():
    hbar, omega, m, c = symbols("hbar omega m c", positive=True, real=True)
    k = 0  # particle at rest

    # Dispersion relation: from Klein-Gordon
    # Dispersion relation: omega^2 = k^2 + (m*c^2/hbar)^2
    dispersion_eq = Eq(omega**2, (m * c**2 / hbar)**2)

    # Solve for omega
    omega_solutions = solve(dispersion_eq, omega)

    # Filter for the positive solution (omega > 0 by assumption)
    omega_solution = [sol for sol in omega_solutions if sol.is_positive]
    assert len(omega_solution) == 1  # make sure we got a unique positive result

    # E = hbar * omega
    E = hbar * omega_solution[0]
    expected = m * c**2

from core import generate_waveform
def test_mass_energy_waveform_agrees_with_E_equals_mc2():
    waveform = generate_waveform(mass=1.0, c=1.0, hbar=1.0, at_rest=True)
    energy = waveform.energy
    assert abs(energy - 1.0) < 1e-6  # since E = mc² = 1*1²


    assert simplify(E - expected) == 0
