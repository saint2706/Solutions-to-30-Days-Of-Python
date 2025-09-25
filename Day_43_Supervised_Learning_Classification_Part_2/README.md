# Day 43: Supervised Learning - Classification (Part 2)

Welcome to Day 43! We continue our journey into classification algorithms by exploring two more powerful and widely used models: **Support Vector Machines (SVMs)** and **Decision Trees**.

> **Prerequisites:** Install scikit-learn with `pip install scikit-learn` before diving into the code examples. For a quick refresher on `pip`, revisit the Day 20 Python Package Manager lesson.

## Key Concepts

### 1. Support Vector Machines (SVM)
SVM is a powerful and versatile supervised machine learning algorithm capable of performing linear or non-linear classification, regression, and outlier detection. The core idea is to find a hyperplane that best separates the classes in the feature space.

- **How it works:**
  - An SVM finds the optimal hyperplane that has the maximum margin (distance) between the data points of different classes. These data points on the edge of the margin are called "support vectors."
  - For non-linear data, SVMs use the **kernel trick**. This technique implicitly maps the input data into a higher-dimensional space where it can be linearly separated. Common kernels include:
    - **Polynomial Kernel:** For polynomial relationships.
    - **Radial Basis Function (RBF) Kernel:** A popular default choice for complex, non-linear data.

- **Use Case:** Very effective in high-dimensional spaces and for complex but small-to-medium sized datasets.

### 2. Decision Trees
Decision Trees are non-parametric models that build a tree-like structure of decisions and their possible consequences. Each internal node represents a "test" on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label.

- **How it works:**
  - The algorithm recursively splits the data based on the feature that provides the most "information gain" (i.e., the best separation of classes).
  - The process continues until a stopping criterion is met (e.g., maximum depth is reached or nodes are pure).
- **Advantages:** Very intuitive and easy to interpret ("white-box" model).
- **Disadvantage:** Prone to overfitting. This can be mitigated by "pruning" the tree or using them in an ensemble (like Random Forests).

---

## Practice Exercises

1.  **Conceptual Questions:**
    *   What is the "margin" in the context of an SVM? Why is a larger margin generally better?
    *   Explain the purpose of the kernel trick in SVMs.
    *   What are the main advantages and disadvantages of Decision Trees?

2.  **Code Implementation:**
    *   The `solutions.py` file demonstrates how to implement SVM and Decision Tree classifiers on the same Iris dataset from the previous day.
    *   The code covers:
        1.  Loading and splitting the data.
        2.  Training and evaluating an SVM classifier (using the RBF kernel).
        3.  Training and evaluating a Decision Tree classifier.
        4.  Comparing their performance against each other.

Review the code to see these advanced classifiers in action.