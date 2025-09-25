# Day 44: Unsupervised Learning

Welcome to Day 44! Today, we shift our focus to **Unsupervised Learning**, where we work with unlabeled data to discover hidden patterns and structures. We'll explore two fundamental techniques: **K-Means Clustering** for grouping data and **Principal Component Analysis (PCA)** for dimensionality reduction.

## Key Concepts

### What is Unsupervised Learning?
In unsupervised learning, the algorithm is given a dataset without explicit labels and must find patterns or relationships on its own. The goal is not to predict an output but to understand the data's underlying structure.

### 1. K-Means Clustering
K-Means is an algorithm that groups a dataset into a pre-specified number of clusters (`k`). It aims to partition the data points into `k` clusters in which each data point belongs to the cluster with the nearest mean (cluster centroid).

- **How it works:**
  1.  **Initialize:** Randomly select `k` initial centroids from the data.
  2.  **Assign:** Assign each data point to the closest centroid.
  3.  **Update:** Recalculate the centroids as the mean of all data points assigned to that cluster.
  4.  **Repeat:** Repeat the assignment and update steps until the centroids no longer change significantly.
- **Use Case:** Customer segmentation, document clustering, image compression.

### 2. Principal Component Analysis (PCA)
PCA is a dimensionality reduction technique used to reduce the number of features in a dataset while preserving as much of the original information (variance) as possible.

- **How it works:**
  - PCA identifies new, uncorrelated variables called **principal components**. These components are linear combinations of the original features.
  - The first principal component accounts for the largest possible variance in the data, the second component accounts for the second largest, and so on.
  - By keeping only the first few principal components, we can reduce the dimensionality of the data with minimal loss of information.
- **Use Case:** Speeding up model training, data visualization (by reducing data to 2D or 3D).

---

## Practice Exercises

1.  **Conceptual Questions:**
    *   What is the primary goal of clustering?
    *   How do you choose the value of `k` in K-Means? (Hint: Research the "Elbow Method").
    *   What is the main benefit of using PCA?

2.  **Code Implementation:**
    *   The `solutions.py` file demonstrates how to implement both K-Means and PCA using `scikit-learn`.
    *   The code covers:
        1.  Generating synthetic data suitable for clustering.
        2.  Applying K-Means to find clusters in the data.
        3.  Loading the Iris dataset and applying PCA to reduce its dimensionality from 4 to 2.
        4.  Visualizing the results of both algorithms.

Review the code to understand these powerful unsupervised techniques.