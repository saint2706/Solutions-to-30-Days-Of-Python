import numpy as np
from importlib import import_module


day47 = import_module("Day_47_Convolutional_Neural_Networks.solutions")


def _fake_mnist_load_data():
    rng = np.random.default_rng(123)

    def build_split(num_samples: int):
        images = rng.random((num_samples, 28, 28), dtype=np.float32)
        labels = rng.integers(0, 10, size=(num_samples,), dtype=np.int64)
        return images, labels

    train_split = build_split(24)
    test_split = build_split(12)
    return train_split, test_split


def test_cnn_training_with_synthetic_data(monkeypatch):
    day47.set_global_seed(7)
    monkeypatch.setattr(day47.datasets.mnist, "load_data", _fake_mnist_load_data)

    (train_images, train_labels), (test_images, test_labels) = (
        day47.prepare_mnist_data()
    )
    model = day47.build_cnn_model(input_shape=train_images.shape[1:])
    day47.compile_cnn_model(model)
    history = day47.train_cnn_model(
        model,
        train_images,
        train_labels,
        epochs=1,
        batch_size=6,
        validation_data=(test_images, test_labels),
        verbose=0,
        shuffle=False,
    )
    metrics = day47.evaluate_cnn_model(model, test_images, test_labels, verbose=0)

    assert len(history.history["loss"]) == 1
    assert set(metrics.keys()) == {"loss", "accuracy"}
