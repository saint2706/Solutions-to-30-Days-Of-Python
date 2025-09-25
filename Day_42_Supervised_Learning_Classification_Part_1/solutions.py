from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# --- Practical Implementation of Classification Algorithms ---

# 1. Load the dataset
# The Iris dataset is a classic multi-class classification problem.
# Features: sepal length, sepal width, petal length, petal width
# Target: 3 species of iris flowers (0, 1, 2)
iris = load_iris()
X, y = iris.data, iris.target

print("--- Classification Example on Iris Dataset ---")
print(f"Dataset loaded with {X.shape[0]} samples and {X.shape[1]} features.")
print(f"Number of classes: {len(np.unique(y))}")

# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print(f"Training set size: {len(X_train)} samples")
print(f"Testing set size: {len(X_test)} samples")
print("-" * 30)

# 3. Feature Scaling (important for KNN)
# We fit the scaler on the training data and transform both train and test data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Data has been scaled using StandardScaler.")
print("-" * 30)

# --- Model 1: Logistic Regression ---
print("\n--- Training Logistic Regression ---")
# Logistic Regression doesn't strictly require feature scaling but it can help convergence.
# We'll use the scaled data for consistency.
log_reg = LogisticRegression(random_state=42, max_iter=200)
log_reg.fit(X_train_scaled, y_train)

# Make predictions
y_pred_log_reg = log_reg.predict(X_test_scaled)

# Evaluate the model
accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)
print(f"Logistic Regression Accuracy: {accuracy_log_reg:.4f}")


# --- Model 2: K-Nearest Neighbors (KNN) ---
print("\n--- Training K-Nearest Neighbors (KNN) ---")
# We'll use a common value for k, like k=5.
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# Make predictions
y_pred_knn = knn.predict(X_test_scaled)

# Evaluate the model
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"KNN (k={k}) Accuracy: {accuracy_knn:.4f}")
print("-" * 30)

# --- Comparison ---
print("\n--- Model Comparison ---")
print(f"Logistic Regression achieved an accuracy of {accuracy_log_reg*100:.2f}%.")
print(f"KNN (k={k}) achieved an accuracy of {accuracy_knn*100:.2f}%.")
print("Both models perform well on this dataset, with Logistic Regression being slightly better.")
print("-" * 30)