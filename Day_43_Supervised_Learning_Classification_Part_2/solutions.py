from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# --- Practical Implementation of Advanced Classification Algorithms ---

# 1. Load the dataset
iris = load_iris()
X, y = iris.data, iris.target

print("--- Advanced Classification on Iris Dataset ---")
print(f"Dataset loaded with {X.shape[0]} samples and {X.shape[1]} features.")

# 2. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print(f"Training set size: {len(X_train)} samples")
print(f"Testing set size: {len(X_test)} samples")
print("-" * 30)

# 3. Feature Scaling (Important for SVM)
# Decision Trees do not require feature scaling, but SVMs do.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Data has been scaled using StandardScaler.")
print("-" * 30)


# --- Model 1: Support Vector Machine (SVM) ---
print("\n--- Training Support Vector Machine (SVM) ---")
# We'll use the Radial Basis Function (RBF) kernel, which is good for non-linear data.
svm_classifier = SVC(kernel='rbf', random_state=42)
svm_classifier.fit(X_train_scaled, y_train)

# Make predictions
y_pred_svm = svm_classifier.predict(X_test_scaled)

# Evaluate the model
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f"SVM (RBF Kernel) Accuracy: {accuracy_svm:.4f}")


# --- Model 2: Decision Tree ---
print("\n--- Training Decision Tree Classifier ---")
# We'll use the unscaled data for the Decision Tree, as it's not affected by feature scale.
tree_classifier = DecisionTreeClassifier(random_state=42)
tree_classifier.fit(X_train, y_train) # Using original, unscaled data

# Make predictions
y_pred_tree = tree_classifier.predict(X_test) # Using original, unscaled data

# Evaluate the model
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print(f"Decision Tree Accuracy: {accuracy_tree:.4f}")
print("-" * 30)

# --- Comparison ---
print("\n--- Model Comparison ---")
print(f"SVM (RBF Kernel) achieved an accuracy of {accuracy_svm*100:.2f}%.")
print(f"Decision Tree achieved an accuracy of {accuracy_tree*100:.2f}%.")
print("Both models perform very well, showcasing their effectiveness on this dataset.")
print("-" * 30)