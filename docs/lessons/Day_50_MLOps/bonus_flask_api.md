# Day 50: MLOps - Model Deployment

Welcome to our final day, Day 50! Today, we touch upon **MLOps (Machine Learning Operations)**, which focuses on the practical side of deploying, monitoring, and maintaining machine learning models in production environments. Our focus will be on a crucial first step: **saving and loading a trained model**. Later lessons deepen each pillar:

- **Day 65 – MLOps Pipelines and CI/CD** scales persistence into feature stores, model registries, and GitHub Actions workflows.
- **Day 66 – Model Deployment and Serving** compares REST, gRPC, batch, streaming, and edge endpoints with FastAPI/BentoML-inspired adapters.
- **Day 67 – Model Monitoring and Reliability** adds drift detection, retraining triggers, and observability instrumentation.

## Key Concepts

### What is MLOps?

MLOps is a set of practices that aims to deploy and maintain machine learning models in production reliably and efficiently. It's the intersection of Machine Learning, DevOps, and Data Engineering.

**Key MLOps concerns include:**

- **Model Deployment:** How do you make your trained model available to users or other systems?
- **Automation:** Automating the ML workflow from data ingestion to model training and deployment.
- **Monitoring:** Tracking the model's performance in production to detect degradation or drift.
- **Scalability & Reproducibility:** Ensuring your system can handle load and that your experiments can be reproduced.

### Saving and Loading Models

Before you can deploy a model, you need to save its learned state (the weights, parameters, etc.). This process is often called **serialization**. Once saved, the model can be loaded into another environment (like a web server) to make predictions without needing to be retrained.

- **For Scikit-learn:** The standard way is to use Python's `pickle` module or the more efficient `joblib` library. `joblib` is often preferred for objects that carry large NumPy arrays.

- **For TensorFlow/Keras:** TensorFlow has its own built-in saving and loading functionality (`model.save()` and `tf.keras.models.load_model()`). It can save the model's architecture, weights, and training configuration all in one place.

### Serving a Model via a Web API

A common way to deploy a model is to wrap it in a web API.

1. A client (e.g., a web or mobile app) sends a POST request with new data to an API endpoint (e.g., `/predict`).
1. The server, running a web framework like **Flask** or **FastAPI**, receives the data.
1. The server loads the saved model and uses it to make a prediction on the data.
1. The prediction is sent back to the client in the API response (usually in JSON format).

______________________________________________________________________

## Practice Exercise

- The `solutions.py` file demonstrates the basic workflow of saving and loading a `scikit-learn` model using `joblib`.
- The `bonus_flask_api.py` file provides a simple example of how you could serve this saved model using the Flask web framework.
- The code covers:
  1. Training a simple model on the Iris dataset.
  1. Saving the trained model to a file (`iris_model.joblib`).
  1. Loading the model back from the file and using it to make a new prediction.
  1. (Bonus) A minimal Flask app that loads the model and exposes a `/predict` endpoint.

Review the code to understand the fundamental step of model persistence, which is the gateway to model deployment. When you are ready to automate full pipelines, deploy APIs, and monitor production behaviour, continue into Days 65–67 for the dedicated deep dives.

```python
import joblib
from flask import Flask, jsonify, request

# NOTE: To run this script, you need to install Flask:
# pip install Flask

# 1. Initialize the Flask app
app = Flask(__name__)

# 2. Load the trained model
# This is done once when the app starts.
model_filename = "iris_model.joblib"
try:
    model = joblib.load(model_filename)
    print(f"Model '{model_filename}' loaded successfully.")
except FileNotFoundError:
    print(
        f"Error: Model file '{model_filename}' not found. Please run solutions.py first."
    )
    model = None


# 3. Define the prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    """
    Receives a POST request with JSON data and returns a prediction.
    """
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    # Get the JSON data from the request
    data = request.get_json()

    # Basic validation
    if not data or "features" not in data:
        return jsonify({"error": "Invalid input: 'features' key not found"}), 400

    try:
        # Extract features and convert to a list of lists for prediction
        features = [data["features"]]

        # Make a prediction
        prediction_index = model.predict(features)

        # Get the class name from the index
        iris_target_names = [
            "setosa",
            "versicolor",
            "virginica",
        ]  # In a real app, load this properly
        predicted_class = iris_target_names[prediction_index[0]]

        # Return the result as JSON
        return jsonify(
            {
                "prediction": predicted_class,
                "prediction_index": int(prediction_index[0]),
            }
        )

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# --- How to Run This API ---
# 1. Make sure 'iris_model.joblib' exists by running solutions.py.
# 2. Run this script from your terminal: `python bonus_flask_api.py`
# 3. The server will start, usually on http://127.0.0.1:5000.
#
# --- How to Test This API ---
# You can use a tool like 'curl' from another terminal:
#
# curl -X POST http://127.0.0.1:5000/predict \
# -H "Content-Type: application/json" \
# -d '{"features": [6.0, 2.5, 4.5, 1.5]}'
#
# Expected Response:
# {
#   "prediction": "versicolor",
#   "prediction_index": 1
# }

if __name__ == "__main__":
    # The `debug=True` flag allows for auto-reloading when you save changes.
    # Do not use `debug=True` in a production environment.
    app.run(debug=True)

```
