import numpy as np
import sympy as sp

# --- Practice Exercises ---

# 1. Symbolic Differentiation with SymPy
print("--- Symbolic Differentiation ---")
# Define the symbol and the function
x_sym = sp.Symbol('x')
f_sym = x_sym**3 - 2*x_sym**2 + 5

# Differentiate the function with respect to x
f_prime_sym = sp.diff(f_sym, x_sym)

print(f"Original function f(x): {f_sym}")
print(f"Derivative f'(x): {f_prime_sym}")
print("-" * 30)


# 2. Numerical Gradient
print("\n--- Numerical Gradient ---")
# Define the function
def f(x, y):
    return x**2 * y + y**3

# Point at which to calculate the gradient
x_val, y_val = 2, 3
# A small value for h (for numerical approximation)
h = 1e-6

# Calculate partial derivative with respect to x
# (f(x+h, y) - f(x, y)) / h
df_dx = (f(x_val + h, y_val) - f(x_val, y_val)) / h

# Calculate partial derivative with respect to y
# (f(x, y+h) - f(x, y)) / h
df_dy = (f(x_val, y_val + h) - f(x_val, y_val)) / h

gradient = [df_dx, df_dy]

print(f"Function f(x, y) = x^2 * y + y^3")
print(f"Numerical gradient at ({x_val}, {y_val}): {gradient}")
# Analytical solution for verification:
# ∂f/∂x = 2xy = 2*2*3 = 12
# ∂f/∂y = x^2 + 3y^2 = 2^2 + 3*3^2 = 4 + 27 = 31
print("Analytical gradient: [12, 31]")
print("-" * 30)


# 3. Chain Rule Application with SymPy
print("\n--- Chain Rule Application ---")
# Define symbols
u_sym = sp.Symbol('u')
x_sym_chain = sp.Symbol('x')

# Define the functions
y_func = u_sym**2
u_func = 2*x_sym_chain + 1

# Substitute u into y
y_composite = y_func.subs(u_sym, u_func)

# Differentiate the composite function with respect to x
dy_dx_chain = sp.diff(y_composite, x_sym_chain)

print(f"y = u^2, u = 2x + 1")
print(f"Composite function y(x): {y_composite}")
print(f"Derivative dy/dx: {dy_dx_chain}")

# Verification using the chain rule formula:
# dy/du = 2u
# du/dx = 2
# dy/dx = (dy/du) * (du/dx) = 2u * 2 = 4u = 4(2x + 1) = 8x + 4
print(f"Verification (8x + 4): {sp.expand(dy_dx_chain)}")
print("-" * 30)