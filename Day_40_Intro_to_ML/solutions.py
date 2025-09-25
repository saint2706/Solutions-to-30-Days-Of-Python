import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# --- Conceptual Example for Core ML Concepts ---

# This script demonstrates k-fold cross-validation, a technique to assess
# a model's performance more robustly. It also touches upon the bias-variance
# tradeoff by using a simple model (Linear Regression) which typically has
# high bias but low variance.

# 1. Generate a sample dataset
# Let's create a simple dataset where the relationship is approximately linear.
# y = 3x + 5 + noise
X = np.linspace(0, 10, 100).reshape(-1, 1)  # Features (100 samples, 1 feature)
y = 3 * X.flatten() + 5 + np.random.normal(0, 3, 100) # Target variable with some noise

print(f"Generated a dataset with {X.shape[0]} samples.")
print("-" * 30)

# 2. K-Fold Cross-Validation
# We will use 5-fold cross-validation.
k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)

# Store the performance metric (e.g., Mean Squared Error) for each fold
mse_scores = []

print(f"Performing {k}-fold cross-validation...")

# Loop through each fold
for fold, (train_index, test_index) in enumerate(kf.split(X)):
    # Split the data into training and testing sets for this fold
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Initialize and train the model
    # We use Linear Regression, a simple model. If it fails to capture the true
    # relationship, it's said to have high bias.
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mse_scores.append(mse)

    print(f"Fold {fold+1}: MSE = {mse:.4f}")

# 3. Final Performance
# The average MSE across all folds gives a more reliable estimate of the model's performance.
average_mse = np.mean(mse_scores)

print("-" * 30)
print(f"Average MSE across {k} folds: {average_mse:.4f}")
print("This average score is a more robust estimate of how the model will perform on unseen data.")
print("-" * 30)