import tensorflow as tf
from tensorflow.keras import layers, models, datasets
from tensorflow.keras.preprocessing.sequence import pad_sequences

# --- Building an RNN for Sentiment Analysis ---

print("--- RNN (LSTM) for IMDB Sentiment Classification ---")

# 1. Load and Preprocess the IMDB Dataset
# The dataset contains 50,000 movie reviews from IMDB, labeled as positive (1) or negative (0).
# We'll limit the vocabulary to the top 10,000 most frequent words.
vocab_size = 10000
(train_data, train_labels), (test_data, test_labels) = datasets.imdb.load_data(num_words=vocab_size)

print(f"Number of training samples: {len(train_data)}")
print(f"Number of test samples: {len(test_data)}")

# Each review is a sequence of word indices. Let's look at one.
print(f"Example review (as word indices): {train_data[0][:15]}...")

# The reviews have different lengths. We need to pad them to a uniform length.
# We'll set a max length of 256. Reviews longer than this will be truncated.
max_length = 256
train_data_padded = pad_sequences(train_data, maxlen=max_length, padding='post')
test_data_padded = pad_sequences(test_data, maxlen=max_length, padding='post')

print(f"Padded training data shape: {train_data_padded.shape}")
print(f"Padded test data shape: {test_data_padded.shape}")
print("-" * 30)

# 2. Build the Recurrent Neural Network Model
# We will use an LSTM layer.
embedding_dim = 16

model = models.Sequential([
    # 1. Embedding Layer: Turns positive integers (word indices) into dense vectors of fixed size.
    # This layer learns word embeddings from the data.
    layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),

    # 2. LSTM Layer: The core of our RNN. 64 units in the LSTM cell.
    layers.LSTM(64),

    # 3. Dense Classifier Head
    layers.Dense(64, activation='relu'),
    # Output layer with 1 neuron and a sigmoid activation for binary classification.
    layers.Dense(1, activation='sigmoid')
])

# 3. Compile the Model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy', # Loss function for binary classification
    metrics=['accuracy']
)

# Print model summary
print("Model Summary:")
model.summary()
print("-" * 30)

# 4. Train the Model
print("Training the RNN (LSTM)...")
history = model.fit(
    train_data_padded,
    train_labels,
    epochs=5, # 5 epochs is sufficient for a good result
    batch_size=128,
    validation_split=0.2, # Use 20% of training data for validation
    verbose=1
)
print("Model training complete.")
print("-" * 30)

# 5. Evaluate the Model
print("Evaluating the model on the test set...")
test_loss, test_acc = model.evaluate(test_data_padded, test_labels, verbose=2)

print(f"\nTest Accuracy: {test_acc * 100:.2f}%")
print(f"Test Loss: {test_loss:.4f}")
print("RNNs with LSTM/GRU cells are very effective for sequence tasks like sentiment analysis.")
print("-" * 30)