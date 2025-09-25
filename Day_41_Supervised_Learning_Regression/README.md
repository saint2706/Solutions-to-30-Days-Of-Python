# Day 41: Supervised Learning - Regression

Welcome to Day 41! Today, we focus on **Regression**, a type of supervised learning where the goal is to predict a continuous numerical value.

## Key Concepts

### What is Regression?
Regression analysis is a set of statistical processes for estimating the relationships between a dependent variable (often called the 'outcome' or 'target') and one or more independent variables (often called 'predictors' or 'features'). The most common form of regression analysis is **Linear Regression**.

### Linear Regression
Linear Regression is a simple yet powerful algorithm that models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data.

- **Simple Linear Regression:** Involves one independent variable.
  - **Formula:** `y = β₀ + β₁x + ε`
    - `y`: The predicted value (dependent variable).
    - `x`: The input value (independent variable).
    - `β₀`: The y-intercept (a constant).
    - `β₁`: The slope or coefficient of `x`.
    - `ε`: The error term.

- **Multiple Linear Regression:** Involves more than one independent variable.
  - **Formula:** `y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε`

The goal of the algorithm is to find the best-fit line (i.e., the optimal values for the coefficients `β`) that minimizes the sum of squared differences between the actual and predicted values. This is known as the **Ordinary Least Squares (OLS)** method.

---

## Practice Exercises

1.  **Conceptual Questions:**
    *   What is the main goal of a regression model?
    *   Explain the difference between simple and multiple linear regression.
    *   What does the coefficient (`β₁`) represent in a simple linear regression model?

2.  **Code Implementation:**
    *   The `solutions.py` file demonstrates how to implement a simple linear regression model using `scikit-learn`.
    *   The code involves:
        1.  Creating a sample dataset.
        2.  Splitting the data into training and testing sets.
        3.  Training a linear regression model.
        4.  Making predictions and evaluating the model's performance using Mean Squared Error (MSE) and R-squared.

Review the code to understand the practical application of linear regression.