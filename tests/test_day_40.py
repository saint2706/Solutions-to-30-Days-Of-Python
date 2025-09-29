import numpy as np

from Day_40_Intro_to_ML import solutions


def test_cross_validation_metrics_are_reproducible():
    X, y = solutions.generate_dataset(random_state=0)
    kfold = solutions.setup_kfold(n_splits=5, shuffle=True, random_state=42)
    mse_scores, average_mse = solutions.cross_validate_model(X, y, kfold)

    expected_scores = np.array(
        [
            6.908501643070158,
            9.559462256104291,
            7.341246071999068,
            12.317042475211291,
            7.118892997796716,
        ]
    )

    np.testing.assert_allclose(mse_scores, expected_scores)
    assert average_mse == np.mean(expected_scores)
