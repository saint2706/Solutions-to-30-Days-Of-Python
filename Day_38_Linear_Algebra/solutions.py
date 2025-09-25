import numpy as np

# --- Practice Exercises ---

# 1. Vector Operations
print("--- Vector Operations ---")
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Vector sum
vector_sum = v1 + v2
print(f"Sum of v1 and v2: {vector_sum}")

# Vector difference
vector_diff = v1 - v2
print(f"Difference of v1 and v2: {vector_diff}")

# Dot product
dot_product = np.dot(v1, v2)
print(f"Dot product of v1 and v2: {dot_product}")
print("-" * 25)


# 2. Matrix Operations
print("\n--- Matrix Operations ---")
M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[5, 6], [7, 8]])

# Matrix sum
matrix_sum = M1 + M2
print(f"Sum of M1 and M2:\n{matrix_sum}")

# Matrix product (dot product)
matrix_product = np.dot(M1, M2)
print(f"Product of M1 and M2:\n{matrix_product}")
print("-" * 25)


# 3. Eigen-analysis
print("\n--- Eigen-analysis ---")
A = np.array([[4, 1], [2, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"Matrix A:\n{A}")
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

# Verification: A * v = λ * v
# For the first eigenvector/eigenvalue
v1 = eigenvectors[:, 0]
lambda1 = eigenvalues[0]

print(f"\nVerifying for the first eigenvalue/eigenvector:")
print(f"A * v1 = {np.dot(A, v1)}")
print(f"λ1 * v1 = {lambda1 * v1}")
print("Note: The results should be approximately equal.")
print("-" * 25)