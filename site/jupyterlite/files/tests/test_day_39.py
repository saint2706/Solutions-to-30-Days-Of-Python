import numpy as np
import sympy as sp

from Day_39_Calculus import solutions


def test_symbolic_derivative():
    polynomial, derivative = solutions.symbolic_derivative()
    x = sp.Symbol("x")

    assert polynomial == x**3 - 2 * x**2 + 5
    assert derivative == sp.diff(polynomial, x)


def test_numerical_gradient_matches_analytical():
    gradient = solutions.numerical_gradient()
    np.testing.assert_allclose(gradient, np.array([12.0, 31.0]), rtol=1e-5, atol=1e-5)


def test_chain_rule_derivative():
    composite, derivative = solutions.chain_rule_derivative()
    x = sp.Symbol("x")

    assert composite == sp.expand((2 * x + 1) ** 2)
    assert derivative == sp.diff(composite, x)
