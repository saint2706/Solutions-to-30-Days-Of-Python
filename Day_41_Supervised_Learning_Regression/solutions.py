import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# --- Practical Implementation of Linear Regression ---

# 1. Generate a sample dataset
# We'll create a synthetic dataset where the relationship is linear.
# y = 2.5x + 10 + noise
np.random.seed(42) # for reproducibility
X = 2 * np.random.rand(100, 1) # Generate 100 random values for X
y = 10 + 2.5 * X.flatten() + np.random.randn(100) # Corresponding y with noise

print("--- Linear Regression Example ---")
print(f"Generated a dataset with {X.shape[0]} samples.")

# 2. Split the data into training and testing sets
# This is crucial to evaluate the model's performance on unseen data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {len(X_train)} samples")
print(f"Testing set size: {len(X_test)} samples")
print("-" * 30)

# 3. Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# The learned parameters (coefficients)
print(f"Learned Intercept (β₀): {model.intercept_:.4f}")
print(f"Learned Coefficient (β₁): {model.coef_[0]:.4f}")
print("The true values were 10.0 and 2.5, so the model learned them closely.")
print("-" * 30)

# 4. Make predictions on the test set
y_pred = model.predict(X_test)

# 5. Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- Model Evaluation ---")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R-squared (R²): {r2:.4f}")
print("R-squared is the proportion of variance in the dependent variable that is predictable from the independent variable(s).")
print("An R² of 1 indicates that the model perfectly predicts the data.")
print("-" * 30)

# 6. Visualize the results (Optional but recommended)
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual values')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
plt.title('Linear Regression Fit')
plt.xlabel('Independent Variable (X)')
plt.ylabel('Dependent Variable (y)')
plt.legend()
plt.grid(True)
# To run this script and see the plot, you might need to install matplotlib:
# pip install matplotlib
# Then, uncomment the line below:
# plt.show()
# For now, we'll save it to a file.
plt.savefig('regression_fit.png')
print("Saved a plot of the regression fit to 'regression_fit.png'")