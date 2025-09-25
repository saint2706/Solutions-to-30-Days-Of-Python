import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# --- Part 1: K-Means Clustering ---
print("--- K-Means Clustering Example ---")

# 1. Generate synthetic data
# We create 300 data points grouped into 4 distinct clusters.
X_blobs, y_blobs = make_blobs(n_samples=300, centers=4, cluster_std=0.7, random_state=42)

# 2. Apply K-Means
# We specify k=4, since we know there are 4 clusters.
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10) # n_init=10 to avoid bad initializations
kmeans.fit(X_blobs)
y_kmeans = kmeans.predict(X_blobs)
centroids = kmeans.cluster_centers_

print("K-Means applied to synthetic data with 4 clusters.")

# 3. Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(X_blobs[:, 0], X_blobs[:, 1], c=y_kmeans, s=50, cmap='viridis', label='Data Points')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.savefig('kmeans_clusters.png')
print("Saved K-Means visualization to 'kmeans_clusters.png'")
print("-" * 30)


# --- Part 2: Principal Component Analysis (PCA) ---
print("\n--- PCA Example ---")

# 1. Load the Iris dataset
iris = load_iris()
X_iris, y_iris = iris.data, iris.target

# 2. Standardize the data
# PCA is affected by scale, so it's important to scale the features first.
X_scaled = StandardScaler().fit_transform(X_iris)
print("Iris dataset loaded and scaled.")

# 3. Apply PCA
# We want to reduce the 4 dimensions to 2 for visualization.
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Original shape: {X_scaled.shape}")
print(f"Shape after PCA: {X_pca.shape}")

# Explained variance
explained_variance = pca.explained_variance_ratio_
print(f"Explained variance by component: {explained_variance}")
print(f"Total variance explained by 2 components: {sum(explained_variance)*100:.2f}%")
print("-" * 30)

# 4. Visualize the PCA results
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_iris, cmap='viridis', edgecolor='k', s=60)
plt.title('PCA of Iris Dataset')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend(handles=scatter.legend_elements()[0], labels=iris.target_names.tolist())
plt.grid(True)
plt.savefig('pca_iris.png')
print("Saved PCA visualization to 'pca_iris.png'")
print("-" * 30)