# Day 38: Math Foundations - Linear Algebra

Welcome to Day 38! Today, we'll dive into the fundamental concepts of Linear Algebra that form the mathematical backbone of many machine learning algorithms. Understanding these concepts is crucial for building a strong foundation in ML.

## Key Concepts

### 1. Vectors
A vector is a mathematical object that has both magnitude and direction. In machine learning, vectors are used to represent data points or features. A vector is often represented as an array of numbers.

- **Example:** A vector `v` in a 2D space can be represented as `v = [x, y]`.

### 2. Matrices
A matrix is a rectangular array of numbers arranged in rows and columns. In machine learning, matrices are used to represent datasets, where rows correspond to data points and columns correspond to features.

- **Example:** A 2x3 matrix `A`:
  ```
  A = [[1, 2, 3],
       [4, 5, 6]]
  ```

### 3. Dot Product
The dot product of two vectors is a scalar value that represents the projection of one vector onto another. It is a measure of similarity between two vectors.

- **Formula:** For two vectors `a = [a1, a2, ..., an]` and `b = [b1, b2, ..., bn]`, the dot product is `a · b = a1*b1 + a2*b2 + ... + an*bn`.

### 4. Eigenvectors and Eigenvalues
Eigenvectors and eigenvalues are special properties of a square matrix. An eigenvector of a matrix is a non-zero vector that, when multiplied by the matrix, results in a scaled version of the eigenvector. The scaling factor is the eigenvalue.

- **Formula:** For a square matrix `A`, a non-zero vector `v` is an eigenvector if `Av = λv`, where `λ` is the eigenvalue.
- **Importance:** They are fundamental to dimensionality reduction techniques like Principal Component Analysis (PCA).

---

## Practice Exercises

1. **Vector Operations:**
   - Create two vectors, `v1 = [1, 2, 3]` and `v2 = [4, 5, 6]`.
   - Calculate their sum, difference, and dot product.

2. **Matrix Operations:**
   - Create a 2x2 matrix `M1 = [[1, 2], [3, 4]]` and another 2x2 matrix `M2 = [[5, 6], [7, 8]]`.
   - Calculate their sum and product.

3. **Eigen-analysis:**
   - Find the eigenvalues and eigenvectors of the matrix `A = [[4, 1], [2, 3]]`.

Check the `solutions.py` file for the Python implementation of these exercises.