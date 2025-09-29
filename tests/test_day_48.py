import importlib.util
from pathlib import Path
import sys

import numpy as np


def _load_day48_module():
    module_path = Path(__file__).resolve().parents[1] / "Day_48_Recurrent_Neural_Networks" / "solutions.py"
    spec = importlib.util.spec_from_file_location("day48_solutions", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day48 = _load_day48_module()


def _fake_imdb_load_data(num_words=None):
    rng = np.random.default_rng(321)

    def build_split(num_samples: int):
        lengths = rng.integers(5, 15, size=num_samples)
        sequences = [rng.integers(1, 100, size=int(length)).tolist() for length in lengths]
        labels = rng.integers(0, 2, size=num_samples, dtype=np.int64)
        return sequences, labels

    train_split = build_split(32)
    test_split = build_split(16)
    return train_split, test_split


def test_rnn_training_with_stubbed_dataset(monkeypatch):
    day48.set_global_seed(11)
    monkeypatch.setattr(day48.datasets.imdb, "load_data", _fake_imdb_load_data)

    (train_data, train_labels), (test_data, test_labels) = day48.prepare_imdb_data(
        vocab_size=100, max_length=32
    )
    model = day48.build_rnn_model(
        vocab_size=100,
        embedding_dim=8,
        max_length=32,
        lstm_units=16,
        dense_units=16,
    )
    history = day48.train_rnn_model(
        model,
        train_data,
        train_labels,
        epochs=1,
        batch_size=8,
        validation_split=0.2,
        verbose=0,
        shuffle=False,
    )
    metrics = day48.evaluate_rnn_model(model, test_data, test_labels, verbose=0)

    assert len(history.history["loss"]) == 1
    assert set(metrics.keys()) == {"loss", "accuracy"}
