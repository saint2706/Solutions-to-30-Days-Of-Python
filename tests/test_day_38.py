import numpy as np

from Day_38_Linear_Algebra.solutions import (
    eigen_analysis,
    matrix_operations,
    vector_operations,
)


def test_vector_operations_defaults():
    vector_sum, vector_difference, dot_product = vector_operations()

    np.testing.assert_array_equal(vector_sum, np.array([5, 7, 9]))
    np.testing.assert_array_equal(vector_difference, np.array([-3, -3, -3]))
    assert dot_product == 32


def test_matrix_operations_defaults():
    matrix_sum, matrix_product = matrix_operations()

    np.testing.assert_array_equal(matrix_sum, np.array([[6, 8], [10, 12]]))
    np.testing.assert_array_equal(matrix_product, np.array([[19, 22], [43, 50]]))


def test_eigen_analysis_defaults():
    eigenvalues, eigenvectors = eigen_analysis()

    expected_eigenvalues = np.array([5.0, 2.0])
    expected_eigenvectors = np.array(
        [[0.70710678, -0.4472136], [0.70710678, 0.89442719]]
    )

    np.testing.assert_allclose(eigenvalues, expected_eigenvalues)
    np.testing.assert_allclose(np.abs(eigenvectors), np.abs(expected_eigenvectors))
