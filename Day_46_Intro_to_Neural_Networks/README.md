# Day 46: Introduction to Neural Networks & Frameworks

Welcome to Day 46! Today, we begin our exploration of **Deep Learning** by introducing the fundamental building block: the **Artificial Neural Network (ANN)**. We'll also discuss the major frameworks used to build these powerful models.

> **Prerequisites:** Install TensorFlow with `pip install tensorflow` to run today's neural-network examples (this installs the CPU build; GPU acceleration requires following TensorFlow's CUDA setup). You'll also need scikit-learn for data prep with `pip install scikit-learn`. Need a refresher on using `pip`? Revisit the Day 20 Python Package Manager lesson.

## Key Concepts

### What is a Neural Network?
An Artificial Neural Network is a computational model inspired by the structure and function of the human brain. It consists of interconnected nodes, called **neurons**, organized in layers.

### Structure of a Neural Network

1.  **Input Layer:** Receives the initial data or features. The number of neurons in this layer corresponds to the number of features in the dataset.

2.  **Hidden Layers:** These are the intermediate layers between the input and output layers. A neural network can have zero or more hidden layers. A "deep" neural network has multiple hidden layers.
    -   Each neuron in a hidden layer receives inputs from the previous layer, applies a mathematical operation (a weighted sum followed by an **activation function**), and passes the result to the next layer.

3.  **Output Layer:** Produces the final result.
    -   For a **regression** task, it might have a single neuron with a linear activation.
    -   For a **classification** task, it might have multiple neurons (one for each class) with a softmax activation function to output probabilities.

### Activation Functions
Activation functions introduce non-linearity into the network, allowing it to learn complex patterns. Without them, a neural network would just be a linear regression model.
-   **Common Examples:**
    -   **ReLU (Rectified Linear Unit):** `f(x) = max(0, x)`. The most widely used activation function.
    -   **Sigmoid:** `f(x) = 1 / (1 + e^(-x))`. Used in the output layer for binary classification.
    -   **Softmax:** Generalizes the sigmoid function for multi-class classification.

### How Neural Networks Learn
They learn through a process called **backpropagation** and **gradient descent**.
1.  The network makes a prediction (forward pass).
2.  The prediction error is calculated using a **loss function**.
3.  The backpropagation algorithm calculates the gradient of the loss function with respect to the network's weights.
4.  The weights are updated using gradient descent to minimize the error.

## Deep Learning Frameworks

Building neural networks from scratch is complex. We use specialized libraries to handle the heavy lifting.
-   **TensorFlow:** Developed by Google, it's a powerful and flexible ecosystem for machine learning. It's known for its production-readiness and scalability.
-   **PyTorch:** Developed by Facebook's AI Research lab, it's known for its simplicity, ease of use, and Pythonic nature, making it a favorite in the research community.

---

## Practice Exercise

-   The `solutions.py` file demonstrates how to build a simple neural network for a classification task using **TensorFlow with the Keras API**.
-   The code covers:
    1.  Loading and preparing the Iris dataset.
    2.  Building a sequential model with dense (fully connected) layers.
    3.  Compiling the model (specifying the optimizer, loss function, and metrics).
    4.  Training the model.
    5.  Evaluating its performance.

Review the code to understand the basic workflow of building and training a neural network.