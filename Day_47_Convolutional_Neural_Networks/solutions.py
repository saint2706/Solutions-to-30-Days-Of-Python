import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# --- Building a CNN for Handwritten Digit Recognition ---

print("--- CNN for MNIST Classification ---")

# 1. Load and Preprocess the MNIST Dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Add a channel dimension. MNIST images are grayscale, so the channel is 1.
# Keras Conv2D layers expect inputs in the shape (batch, height, width, channels).
train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

print(f"Training data shape: {train_images.shape}")
print(f"Test data shape: {test_images.shape}")
print("-" * 30)

# 2. Build the Convolutional Neural Network Model
model = models.Sequential([
    # First Convolutional Block
    # 32 filters of size 3x3. 'relu' activation introduces non-linearity.
    # `input_shape` is specified for the first layer.
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    # Max pooling layer reduces dimensionality.
    layers.MaxPooling2D((2, 2)),

    # Second Convolutional Block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third Convolutional Block
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Flatten the 3D output to 1D to feed into Dense layers
    layers.Flatten(),

    # Dense Classifier Head
    layers.Dense(64, activation='relu'),
    # Output layer with 10 neurons (for 10 digits) and softmax activation
    layers.Dense(10, activation='softmax')
])

# 3. Compile the Model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy', # Use this for integer labels
    metrics=['accuracy']
)

# Print model summary
print("Model Summary:")
model.summary()
print("-" * 30)

# 4. Train the Model
print("Training the CNN...")
# We train for 5 epochs, which is enough for high accuracy on MNIST.
history = model.fit(
    train_images,
    train_labels,
    epochs=5,
    batch_size=64,
    validation_data=(test_images, test_labels),
    verbose=1 # Show training progress
)
print("Model training complete.")
print("-" * 30)

# 5. Evaluate the Model
print("Evaluating the model on the test set...")
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

print(f"\nTest Accuracy: {test_acc * 100:.2f}%")
print(f"Test Loss: {test_loss:.4f}")
print("CNNs are highly effective for image tasks, often achieving >99% accuracy on MNIST.")
print("-" * 30)

# 6. Visualize Training History (Optional)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label = 'Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.9, 1])
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label = 'Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.savefig('cnn_training_history.png')
print("Saved training history plot to 'cnn_training_history.png'")
print("-" * 30)