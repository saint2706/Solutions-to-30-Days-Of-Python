# Day 45: Feature Engineering & Model Evaluation

Welcome to Day 45! Today, we cover two critical aspects of the machine learning workflow: **Feature Engineering**, the art of creating better input features, and **Model Evaluation**, the science of assessing a model's performance beyond simple accuracy.

> **Prerequisites:** Install scikit-learn with `pip install scikit-learn` so you can follow the preprocessing and evaluation walkthroughs. Need a reminder on managing packages? Revisit the Day 20 Python Package Manager lesson.

## 1. Feature Engineering

Feature engineering is the process of using domain knowledge to create features that make machine learning algorithms work better. Good features can make the difference between a poor model and a highly accurate one.

### Key Techniques

-   **Feature Scaling:**
    -   **Standardization:** Rescales features to have a mean of 0 and a standard deviation of 1. (Used in `StandardScaler`).
    -   **Normalization:** Rescales features to a range of [0, 1]. (Used in `MinMaxScaler`).
    -   **Why?** Essential for distance-based algorithms (like KNN, SVM) and gradient-based algorithms.

-   **Encoding Categorical Variables:**
    -   **One-Hot Encoding:** Creates a new binary column for each category. Best for nominal data (categories with no intrinsic order).
    -   **Label Encoding:** Assigns a unique integer to each category. Suitable for ordinal data (categories with a clear order).

-   **Handling Missing Values:**
    -   **Imputation:** Filling in missing values (e.g., with the mean, median, or mode of the column).

## 2. Advanced Model Evaluation

While accuracy is a common metric, it can be misleading, especially for imbalanced datasets (where one class is much more frequent than others).

### Key Metrics for Classification

-   **Confusion Matrix:** A table that summarizes the performance of a classification model.

|                | Predicted: NO  | Predicted: YES |
|----------------|----------------|----------------|
| **Actual: NO** | True Negative  | False Positive |
| **Actual: YES**| False Negative | True Positive  |

-   **Precision:** Measures the accuracy of positive predictions.
    -   `Precision = TP / (TP + FP)`
    -   *Of all the times the model predicted YES, how many were actually YES?*

-   **Recall (Sensitivity):** Measures the ability of the model to find all the positive samples.
    -   `Recall = TP / (TP + FN)`
    -   *Of all the actual YES instances, how many did the model correctly identify?*

-   **F1-Score:** The harmonic mean of precision and recall. It provides a single score that balances both concerns.
    -   `F1-Score = 2 * (Precision * Recall) / (Precision + Recall)`

---

## Practice Exercises

1.  **Conceptual Questions:**
    *   Why is feature scaling important? Name one algorithm that requires it and one that doesn't.
    *   When would you use One-Hot Encoding versus Label Encoding?
    *   Explain a scenario where high accuracy might be a misleading metric.

2.  **Code Implementation:**
    *   The `solutions.py` file demonstrates:
        1.  A simple feature engineering pipeline including imputation, scaling, and one-hot encoding.
        2.  How to calculate and interpret a confusion matrix, precision, recall, and F1-score using `scikit-learn`.

Review the code to understand how to prepare data and properly evaluate a model.