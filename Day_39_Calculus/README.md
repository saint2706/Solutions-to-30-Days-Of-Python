# Day 39: Math Foundations - Calculus

Welcome to Day 39! Today, we explore the essential concepts of calculus that are fundamental to training machine learning models, particularly in the context of optimization.

## Key Concepts

### 1. Derivatives
A derivative measures the sensitivity to change of a function's output with respect to a change in its input. In machine learning, derivatives tell us how to change a model's parameters to reduce its error.

- **Concept:** The derivative of a function `f(x)` at a point `x` is the slope of the tangent line to the graph of the function at that point.
- **Notation:** `f'(x)` or `df/dx`.

### 2. Gradients
A gradient is a multi-variable generalization of the derivative. For a function with multiple inputs (e.g., a model with multiple weights), the gradient is a vector of partial derivatives. It points in the direction of the steepest ascent of the function.

- **Concept:** To minimize a function, we move in the direction opposite to the gradient. This is the core idea behind **Gradient Descent**.
- **Formula:** For a function `f(x, y)`, the gradient is `∇f = [∂f/∂x, ∂f/∂y]`.

### 3. Chain Rule
The chain rule is a formula to compute the derivative of a composite function. In deep learning, neural networks are essentially deeply nested functions, and the chain rule is the foundation for the **backpropagation** algorithm, which is used to train them.

- **Formula:** If `h(x) = f(g(x))`, then `h'(x) = f'(g(x)) * g'(x)`.

---

## Practice Exercises

1. **Symbolic Differentiation:**
   - Consider the function `f(x) = x^3 - 2x^2 + 5`.
   - Find the derivative of this function symbolically.

2. **Numerical Gradient:**
   - Consider the function `f(x, y) = x^2 * y + y^3`.
   - Calculate the numerical gradient of this function at the point `(2, 3)`.

3. **Chain Rule Application:**
   - Let `y = u^2` and `u = 2x + 1`.
   - Use the chain rule to find `dy/dx`.

Check the `solutions.py` file for the Python implementation of these exercises using libraries like `sympy` and `numpy`.