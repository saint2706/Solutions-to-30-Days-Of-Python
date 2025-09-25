# Day 42: Supervised Learning - Classification (Part 1)

Welcome to Day 42! Today, we begin our exploration of **Classification**, a type of supervised learning where the goal is to predict a discrete class label. We'll start with two fundamental classification algorithms: Logistic Regression and K-Nearest Neighbors (KNN).

## Key Concepts

### What is Classification?
Classification is the task of assigning a predefined label or category to a given input data point. The output is a categorical value.
- **Examples:** Email is `spam` or `not spam`; a tumor is `benign` or `malignant`.

### 1. Logistic Regression
Despite its name, Logistic Regression is a classification algorithm, not a regression one. It models the probability that a given input point belongs to a certain class.

- **How it works:** It uses the **sigmoid function** (or logistic function) to transform the output of a linear equation into a probability value between 0 and 1.
  - **Sigmoid Function:** `σ(z) = 1 / (1 + e^(-z))`
  - A threshold (commonly 0.5) is then applied to this probability to assign the final class label.
- **Use Case:** It's a great, simple baseline model for binary classification problems.

### 2. K-Nearest Neighbors (KNN)
KNN is a simple, instance-based learning algorithm. It classifies a new data point based on the majority class of its "k" closest neighbors in the feature space.

- **How it works:**
  1.  Choose a value for `k` (the number of neighbors).
  2.  For a new data point, calculate the distance (e.g., Euclidean distance) to all other points in the training data.
  3.  Identify the `k` nearest neighbors.
  4.  Assign the new data point the class label that is most common among its `k` neighbors.
- **Important Note:** KNN requires feature scaling (e.g., normalization or standardization) because it is sensitive to the scale of the features.

---

## Practice Exercises

1.  **Conceptual Questions:**
    *   Why is Logistic Regression used for classification instead of Linear Regression?
    *   What is the role of `k` in the KNN algorithm? How does its value affect the model?
    *   Why is feature scaling important for KNN?

2.  **Code Implementation:**
    *   The `solutions.py` file provides a practical example of implementing both Logistic Regression and KNN on a sample dataset using `scikit-learn`.
    *   The code covers:
        1.  Loading the Iris dataset (a famous multi-class classification dataset).
        2.  Splitting the data.
        3.  Training and evaluating a Logistic Regression model.
        4.  Training and evaluating a KNN model.
        5.  Comparing their performance using an accuracy score.

Review the code to see these algorithms in action.