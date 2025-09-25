import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# --- Building a Simple Neural Network with TensorFlow/Keras ---

# Set random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

print("--- Neural Network for Iris Classification ---")

# 1. Load and Prepare the Data
iris = load_iris()
X, y = iris.data, iris.target

# a. Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# b. One-hot encode the target variable
# Neural networks for multi-class classification require the target to be in a binary matrix format.
encoder = OneHotEncoder(sparse_output=False)
y_onehot = encoder.fit_transform(y.reshape(-1, 1))

# c. Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_onehot, test_size=0.2, random_state=42)

print(f"Data loaded and prepared. Training set shape: {X_train.shape}")
print(f"One-hot encoded target shape: {y_train.shape}")
print("-" * 30)

# 2. Build the Neural Network Model
# We use a Sequential model, which is a linear stack of layers.
model = tf.keras.Sequential([
    # Input layer and first hidden layer
    # Dense layer means every neuron is connected to every neuron in the previous layer.
    # `input_shape` is only needed for the first layer.
    tf.keras.layers.Dense(10, activation='relu', input_shape=(X_train.shape[1],)),

    # Second hidden layer
    tf.keras.layers.Dense(10, activation='relu'),

    # Output layer
    # 3 neurons for the 3 classes.
    # 'softmax' activation is used for multi-class classification to get probability distribution.
    tf.keras.layers.Dense(3, activation='softmax')
])

# 3. Compile the Model
# This step configures the model for training.
model.compile(
    optimizer='adam',  # Adam is a popular and effective optimization algorithm.
    loss='categorical_crossentropy',  # Loss function for multi-class classification.
    metrics=['accuracy']  # We want to monitor the accuracy during training.
)

# Print a summary of the model architecture
print("Model Summary:")
model.summary()
print("-" * 30)

# 4. Train the Model
# We 'fit' the model to the training data.
print("Training the model...")
history = model.fit(
    X_train,
    y_train,
    epochs=50,  # An epoch is one complete pass through the entire training dataset.
    batch_size=8, # The number of samples to process before updating the model's weights.
    validation_split=0.2, # Use 20% of training data for validation during training.
    verbose=0  # Set to 0 to hide the lengthy training output for this example.
)
print("Model training complete.")
print("-" * 30)

# 5. Evaluate the Model
# We evaluate the trained model on the unseen test data.
print("Evaluating the model on the test set...")
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print(f"Test Accuracy: {accuracy * 100:.2f}%")
print(f"Test Loss: {loss:.4f}")
print("-" * 30)

# 6. Make a prediction
# Let's predict the class for a new, unseen sample.
# We need to scale it first.
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]]) # An example of Iris-setosa
new_sample_scaled = scaler.transform(new_sample)

prediction = model.predict(new_sample_scaled)
predicted_class = np.argmax(prediction, axis=1)

print("Prediction for a new sample:")
print(f"Probabilities: {prediction[0]}")
print(f"Predicted class index: {predicted_class[0]}")
print(f"Predicted class name: {iris.target_names[predicted_class][0]}")
print("-" * 30)