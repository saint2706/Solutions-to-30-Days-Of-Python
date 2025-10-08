# Coding for MBA

A 53-day applied Python and analytics curriculum designed for business
professionals. Each `Day_XX_*` directory contains a self-contained lesson that
walks through practical data skills, from programming fundamentals to
introductory machine learning.

## 🚀 Quick start

```bash
git clone https://github.com/your-username/Coding-For-MBA.git
cd Coding-For-MBA
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`
pip install -r requirements.txt
```

Optional extras for database-focused lessons:

- MySQL: `pip install mysql-connector-python`
- PostgreSQL: `pip install psycopg2-binary`
- MongoDB: `pip install pymongo`

## 📚 Navigating the lessons

Lessons are organised chronologically. Start with the [Machine Learning Curriculum Roadmap](docs/ml_curriculum.md) if you want to understand how the Day 40–53 sequence grows into an end-to-end ML capability.

**Phases at a glance**

- **Phase 1 – Classic ML foundations:** Day 40–53 walk through supervised/unsupervised learning, neural networks, NLP, and an MLOps primer.
- **Phase 2 – Modern deep learning:** Continue into transformers, transfer learning, and representation learning.
- **Phase 3 – Responsible AI:** Build governance, fairness, and explainability practices into every deployment.
- **Phase 4 – MLOps & lifecycle:** Automate experimentation, deployment, and monitoring for production systems.

When you are ready to run a specific topic, jump to the lesson and execute the corresponding script:

## Running the lessons

Each lesson folder now ships with Jupyter notebooks that mirror the original
Python scripts. Launch Jupyter from the project root and open the notebook for
the topic you want to explore:

```bash
jupyter notebook
```

Navigate to a `Day_*` directory and select the relevant `.ipynb` file—for
instance, `Day_31_Databases/databases.ipynb` walks through the SQLite example
in an interactive notebook environment.

## Featured lessons

- **Day 31 – Relational Databases** (`Day_31_Databases/databases.py`): builds and
  queries a SQLite database, mirroring production-ready analysis workflows.
- **Day 32 – Other Databases** (`Day_32_Other_Databases/other_databases.py`):
  demonstrates dependency-injected connection patterns for SQL and MongoDB
  clients so that data access logic remains testable.
- **Day 51 – Regularised Models** (`Day_51_Regularized_Models/solutions.py`):
  compares ridge, lasso, and elastic net pipelines while introducing Poisson
  regression as a generalised linear model.
- **Day 52 – Ensemble Methods** (`Day_52_Ensemble_Methods/solutions.py`): trains
  random forests, gradient boosting, and stacking ensembles with calibration
  utilities for trustworthy probabilities.
- **Day 53 – Model Tuning & Feature Selection**
  (`Day_53_Model_Tuning_and_Feature_Selection/solutions.py`): demonstrates grid
  search, Bayesian optimisation (via `skopt`), permutation importance, and
  recursive feature elimination on a reproducible dataset.
- **Day 50 – MLOps** (`Day_50_MLOps/solutions.py`): exposes reusable helpers for
  training, saving, loading, and predicting with a Logistic Regression Iris
  classifier.

### Day 50 quick start

The Day 50 helpers can be orchestrated from the command line or imported into
notebooks and other Python modules.

Run the bundled CLI demo:

```bash
python Day_50_MLOps/solutions.py
```

Use the functions programmatically:

```python
from Day_50_MLOps.solutions import (
    load_model,
    predict_sample,
    save_model,
    train_iris_model,
)

model, accuracy, X_test, y_test, target_names = train_iris_model()
model_path = save_model(model, "iris_model.joblib")
reloaded = load_model(model_path)
prediction, label = predict_sample(reloaded, X_test[0], target_names)
```

## Working with notebooks and scripts

Notebooks are generated from the original lesson scripts via
`tools/convert_lessons_to_notebooks.py`. If you update a `.py` lesson, rerun the
converter to refresh the paired notebook:

```bash
python tools/convert_lessons_to_notebooks.py
```

You can still execute the scripts directly—`python Day_31_Databases/databases.py`
remains valid—but notebooks are the recommended path for hands-on exploration.

## ✅ Testing the curriculum

Automated tests live under `tests/` and cover representative helpers from the
lessons, including the Day 37 recap.

Install the optional development dependencies to enable the coverage tooling:

```bash
pip install -r requirements-dev.txt
```

Running `pytest` now enables coverage reporting and enforces a 40% minimum
across the Day 24–26 analytics modules via `pytest.ini`:

```bash
pytest
```

## 🧹 Code formatting

The repository standardises formatting across Python modules, notebooks, and
Markdown documents. After installing `requirements-dev.txt`, run the following
commands from the project root before opening a pull request:

```bash
ruff check --fix .
ruff format .
nbqa black $(git ls-files '*.ipynb')
nbqa ruff --fix $(git ls-files '*.ipynb')
mdformat $(git ls-files '*.md')
```

## 🔄 Dependency reviews

The library stack is reviewed periodically. See [`docs/dependency-review.md`](docs/dependency-review.md)
for the latest upgrade log (most recent review: 2025-09-29).

- `tests/test_data_pipeline.py` chains the refactored functions from Days 24–26
  to ensure messy CSV extracts can be cleaned, aggregated, and transformed into
  plot-ready tables for the Day 27 visualisations.

- Individual lessons can still be executed directly, for example:

  ```bash
  pytest tests/test_day_31.py
  pytest tests/test_day_32.py
  pytest tests/test_day_37.py
  pytest tests/test_day_50.py
  ```

The Day 32 tests rely solely on dependency-injected stubs, so they can run
without provisioning database services. The Day 50 test trains a seeded subset
of the Iris dataset, persists the model to a temporary location, reloads it, and
verifies that predictions remain consistent.

## 🗺️ Repository overview

- `Day_01_Introduction` through `Day_50_MLOps`: daily lesson content.
- `Day_37_Conclusion/conclusion.py`: recap data structures and CLI entry point.
- `tests/`: unit tests for selected lessons.

## 🙌 Contributing

Have ideas to expand the business analytics focus? Open an issue or submit a
pull request—we welcome community contributions that keep the curriculum
practical and accessible.
