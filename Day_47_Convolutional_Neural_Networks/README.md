# Day 47: Convolutional Neural Networks (CNNs) for Computer Vision

Welcome to Day 47! Today, we dive into **Convolutional Neural Networks (CNNs)**, a specialized type of neural network that has revolutionized the field of **Computer Vision**.

> **Prerequisites:** Ensure TensorFlow is installed with `pip install tensorflow` (CPU build by default; use TensorFlow's GPU installation guide if you have compatible hardware). Need to review package installation basics? Revisit the Day 20 Python Package Manager lesson.

## Key Concepts

### What are CNNs?
CNNs are designed to automatically and adaptively learn spatial hierarchies of features from images. Unlike standard neural networks, which treat inputs as flat vectors, CNNs preserve the spatial relationship between pixels.

### Core Components of a CNN

1.  **Convolutional Layer (`Conv2D`)**
    -   This is the main building block of a CNN. It uses **filters** (or kernels) to slide over the input image and perform a convolution operation.
    -   This process creates **feature maps** that highlight specific patterns like edges, corners, or textures in the image. The network learns the optimal values for these filters during training.

2.  **Pooling Layer (`MaxPooling2D`)**
    -   The pooling layer is used to downsample the feature maps, reducing their spatial dimensions.
    -   This reduces the number of parameters and computation in the network, helping to control overfitting.
    -   **Max Pooling** is the most common type, where a filter slides over the feature map and takes the maximum value from each region.

3.  **Flatten Layer**
    -   After the convolutional and pooling layers have extracted features, the resulting multi-dimensional feature maps are flattened into a single one-dimensional vector.
    -   This vector is then fed into a standard fully connected neural network (like the one from Day 46) for classification.

### A Typical CNN Architecture
A common CNN architecture consists of a stack of `Conv2D` and `MaxPooling2D` layers, followed by one or more `Dense` layers for classification.

1.  **Input Image**
2.  **[Conv2D -> ReLU Activation -> MaxPooling2D]** (This block can be repeated multiple times)
3.  **Flatten Layer**
4.  **Dense Layer (with ReLU)**
5.  **Output Dense Layer (with Softmax for classification)**

---

## Practice Exercise

-   The `solutions.py` file demonstrates how to build and train a simple CNN to classify handwritten digits from the famous **MNIST dataset**.
-   The code covers:
    1.  Loading and preprocessing the MNIST image data. (Images are normalized to be between 0 and 1).
    2.  Building a sequential CNN model with `Conv2D`, `MaxPooling2D`, `Flatten`, and `Dense` layers.
    3.  Compiling and training the CNN.
    4.  Evaluating its performance on the test set. A well-trained CNN can achieve very high accuracy on this task.

Review the code to see how these specialized layers are combined to create a powerful image classifier.