import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# --- Part 1: Feature Engineering Pipeline ---
print("--- Feature Engineering Example ---")

# Create a sample dataset with missing values and categorical data
data = {
    'age': [25, 30, 35, 40, np.nan, 45, 50],
    'salary': [50000, 60000, np.nan, 80000, 90000, 100000, 110000],
    'city': ['New York', 'London', 'Paris', 'New York', 'London', 'Tokyo', 'Paris'],
    'purchased': [0, 1, 0, 1, 1, 0, 1] # Target variable
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("-" * 30)

# Separate features and target
X = df.drop('purchased', axis=1)
y = df['purchased']

# Identify numeric and categorical features
numeric_features = ['age', 'salary']
categorical_features = ['city']

# Create preprocessing pipelines for numeric and categorical data
# For numeric data: impute missing values with the mean, then scale.
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# For categorical data: one-hot encode.
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Create a preprocessor object using ColumnTransformer to apply different transformations
# to different columns.
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Apply the preprocessing pipeline
X_processed = preprocessor.fit_transform(X)

print("Shape of data after preprocessing:", X_processed.shape)
print("Note: 'city' was expanded into 3 columns by OneHotEncoder.")
print("Transformed data (first 3 rows):")
print(X_processed[:3])
print("-" * 30)


# --- Part 2: Advanced Model Evaluation ---
print("\n--- Model Evaluation Example ---")

# Split the processed data
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.3, random_state=42)

# Train a simple model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# 1. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
print("TN | FP")
print("FN | TP")
print(f"True Negatives (TN): {cm[0, 0]} | False Positives (FP): {cm[0, 1]}")
print(f"False Negatives (FN): {cm[1, 0]} | True Positives (TP): {cm[1, 1]}")
print("-" * 30)

# 2. Classification Report (Precision, Recall, F1-Score)
report = classification_report(y_test, y_pred, zero_division=0)
print("Classification Report:")
print(report)
print("This report provides a breakdown of precision, recall, and f1-score for each class.")
print("-" * 30)