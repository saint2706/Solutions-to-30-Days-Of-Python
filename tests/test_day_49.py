import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_49_NLP.solutions import build_count_matrix, build_tfidf_matrix


def test_build_count_matrix_vocab_and_counts():
    corpus = [
        "Apple banana apple",
        "Banana carrot"
    ]

    df = build_count_matrix(corpus)

    assert list(df.columns) == ["apple", "banana", "carrot"]
    assert df.shape == (2, 3)

    expected = np.array(
        [
            [2, 1, 0],
            [0, 1, 1]
        ]
    )
    np.testing.assert_array_equal(df.to_numpy(), expected)


def test_build_tfidf_matrix_vocab_shape_and_values():
    corpus = [
        "Cat sat",
        "Cat sat sat"
    ]

    df = build_tfidf_matrix(corpus)

    assert list(df.columns) == ["cat", "sat"]
    assert df.shape == (2, 2)

    expected = np.array(
        [
            [0.70710678, 0.70710678],
            [0.4472136, 0.89442719]
        ]
    )
    np.testing.assert_allclose(df.to_numpy(), expected, rtol=1e-5, atol=1e-8)
