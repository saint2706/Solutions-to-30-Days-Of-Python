import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- MLOps: Saving and Loading a Scikit-learn Model ---

print("--- Model Persistence Example ---")

# 1. Load data and train a model
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Check its accuracy on the test set
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model trained with an accuracy of: {accuracy * 100:.2f}%")
print("-" * 30)

# 2. Save the trained model to a file
# We use joblib, which is efficient for scikit-learn models.
model_filename = 'iris_model.joblib'
joblib.dump(model, model_filename)

print(f"Model saved to '{model_filename}'")
print("-" * 30)

# 3. Load the model from the file in a "new session"
# In a real application, this would be in a separate script (like a web server).
print("Loading model from file...")
loaded_model = joblib.load(model_filename)
print("Model loaded successfully.")
print("-" * 30)

# 4. Use the loaded model to make a prediction
# Let's create a new data sample that the original model has never seen.
# This sample has features similar to an Iris-versicolor flower.
new_sample = [[6.0, 2.5, 4.5, 1.5]]

# Use the loaded model to predict the class of the new sample
prediction = loaded_model.predict(new_sample)
predicted_class_name = iris.target_names[prediction[0]]

print("--- Making a Prediction with the Loaded Model ---")
print(f"New sample data: {new_sample[0]}")
print(f"Predicted class index: {prediction[0]}")
print(f"Predicted class name: '{predicted_class_name}'")
print("This demonstrates that our saved model retains its knowledge.")
print("-" * 30)

print("\nCheck out 'bonus_flask_api.py' for an example of how to serve this model in a web API.")