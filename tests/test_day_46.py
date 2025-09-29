import importlib.util
from pathlib import Path
import sys


def _load_day46_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "Day_46_Intro_to_Neural_Networks"
        / "solutions.py"
    )
    spec = importlib.util.spec_from_file_location("day46_solutions", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


day46 = _load_day46_module()


def test_iris_training_single_epoch():
    day46.set_global_seed(123)
    data = day46.prepare_iris_data(random_state=123)

    model = day46.build_iris_model(data.X_train.shape[1], data.y_train.shape[1])
    history = day46.train_iris_model(
        model,
        data.X_train,
        data.y_train,
        epochs=1,
        batch_size=16,
        validation_split=0.2,
        verbose=0,
        shuffle=False,
    )
    metrics = day46.evaluate_iris_model(model, data.X_test, data.y_test, verbose=0)

    assert history.params["epochs"] == 1
    assert len(history.history["loss"]) == 1
    assert set(metrics.keys()) == {"loss", "accuracy"}
    assert 0.0 <= metrics["accuracy"] <= 1.0
