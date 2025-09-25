# Day 40: Introduction to Machine Learning & Core Concepts

Welcome to Day 40! Today, we'll introduce the field of Machine Learning (ML) and discuss some of the core concepts that are essential for understanding how ML models are trained and evaluated.

## What is Machine Learning?

Machine Learning is a subfield of artificial intelligence that gives computers the ability to learn from data without being explicitly programmed. Instead of writing rules, we provide an algorithm with a large amount of data and let it learn the patterns itself.

### Types of Machine Learning

1.  **Supervised Learning:** The algorithm learns from a labeled dataset, meaning each data point is tagged with a correct output. The goal is to learn a mapping function that can predict the output for new, unseen data.
    *   **Examples:** Spam detection (classification), house price prediction (regression).

2.  **Unsupervised Learning:** The algorithm learns from an unlabeled dataset, discovering hidden patterns or structures on its own.
    *   **Examples:** Customer segmentation (clustering), anomaly detection.

3.  **Reinforcement Learning:** An agent learns to make decisions by taking actions in an environment to maximize a cumulative reward.
    *   **Examples:** Training a bot to play a game, self-driving cars.

---

## Core Concepts

### 1. Bias-Variance Tradeoff

This is a fundamental dilemma in supervised learning that involves balancing two types of errors:

-   **Bias:** The error from incorrect assumptions in the learning algorithm. High bias can cause a model to miss relevant relations between features and target outputs (**underfitting**).
-   **Variance:** The error from sensitivity to small fluctuations in the training set. High variance can cause a model to capture random noise in the training data (**overfitting**).

**The Tradeoff:**
- A simple model (like linear regression) usually has **high bias** and **low variance**.
- A complex model (like a deep neural network) usually has **low bias** and **high variance**.
- The goal is to find a sweet spot that minimizes the total error.

### 2. Cross-Validation

Cross-validation is a resampling technique used to evaluate a machine learning model on a limited data sample. It helps to ensure that the model's performance is independent of the particular partitioning of the data into training and testing sets.

**How it works (k-fold cross-validation):**
1.  Split the dataset into *k* equal parts (or "folds").
2.  Use *k-1* folds for training the model.
3.  Use the remaining 1 fold for testing the model.
4.  Repeat this process *k* times, with each fold used exactly once as the test set.
5.  The final performance is the average of the results from the *k* iterations.

This provides a more robust estimate of the model's performance on unseen data.

---

## Practice Exercises

1.  **Conceptual Questions:**
    *   Explain in your own words the difference between supervised and unsupervised learning.
    *   Why is the bias-variance tradeoff important in model selection?
    *   What problem does k-fold cross-validation solve?

2.  **Code Example:**
    *   The `solutions.py` file demonstrates how to perform k-fold cross-validation using `scikit-learn` on a sample dataset. Review the code to understand the implementation.