from sympy import symbols, Function, diff, simplify

from sympy import symbols, exp, I, simplify
from sympy.abc import t, x

def test_klein_gordon_plane_wave():
    m, k, omega = symbols("m k omega", real=True, positive=True)
    phi = exp(-I * (omega * t - k * x))

    d2_phi_dt2 = phi.diff(t, 2)
    d2_phi_dx2 = phi.diff(x, 2)

    kg_expr = d2_phi_dt2 - d2_phi_dx2 + m**2 * phi
    kg_expr_sub = kg_expr.subs(omega**2, k**2 + m**2)

    assert simplify(kg_expr_sub) == 0

