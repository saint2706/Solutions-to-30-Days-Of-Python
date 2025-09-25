# Day 48: Recurrent Neural Networks (RNNs) for Sequence Data

Welcome to Day 48! Today, we explore **Recurrent Neural Networks (RNNs)**, a class of neural networks designed specifically for handling **sequential data**, such as time series, text, or audio.

## Key Concepts

### What are RNNs?
Unlike feedforward networks (like ANNs and CNNs), which process inputs independently, RNNs have **loops** in them, allowing information to persist. This "memory" lets them use information from prior inputs to influence the current input and output.

-   **The Loop:** An RNN processes a sequence one element at a time. At each step, the output from the previous step is fed back as an input to the current step. This creates a hidden state that acts as a memory of the sequence seen so far.

### The Vanishing Gradient Problem
Simple RNNs struggle to learn long-range dependencies (patterns over long sequences). This is due to the **vanishing gradient problem**, where the gradients used to update the network's weights become very small during backpropagation, effectively stopping the learning process for earlier time steps.

### Advanced RNN Architectures
To solve this problem, more sophisticated RNN variants were developed:

1.  **Long Short-Term Memory (LSTM)**
    -   LSTMs are a special kind of RNN that are explicitly designed to avoid the long-term dependency problem.
    -   They have a more complex internal structure called a **cell**, which includes three **gates** (forget, input, and output gates). These gates regulate the flow of information, allowing the network to remember or forget information over long periods.

2.  **Gated Recurrent Unit (GRU)**
    -   GRUs are a simplified version of LSTMs. They combine the forget and input gates into a single "update gate" and have fewer parameters.
    -   They often perform similarly to LSTMs but are computationally more efficient.

### Typical RNN Architecture for Classification
1.  **Input / Embedding Layer:** For text data, an `Embedding` layer is often used first to convert integer indices (representing words) into dense vectors.
2.  **Recurrent Layer (LSTM or GRU):** This layer processes the sequence of vectors.
3.  **Dense Layer:** A standard fully connected layer for classification.
4.  **Output Layer:** Produces the final prediction.

---

## Practice Exercise

-   The `solutions.py` file demonstrates how to build and train a simple RNN (using an LSTM layer) for **sentiment analysis** on the **IMDB movie review dataset**.
-   The goal is to classify a review as either `positive` or `negative`.
-   The code covers:
    1.  Loading and preprocessing the IMDB text data. (Reviews are pre-processed into sequences of integers).
    2.  Padding the sequences to ensure they all have the same length.
    3.  Building a sequential model with an `Embedding` layer, an `LSTM` layer, and `Dense` layers.
    4.  Compiling and training the RNN.
    5.  Evaluating its performance on the test set.

Review the code to see how RNNs can be used to understand and classify sequential text data.