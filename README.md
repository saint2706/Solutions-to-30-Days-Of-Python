# Coding for MBA

A 50-day applied Python and analytics curriculum designed for business
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

Lessons are organised chronologically. Jump to any topic by running the
corresponding script:

## Running the lessons

Each lesson folder provides a focused example that can be run directly with
Python. For instance, execute Day 31's SQLite walkthrough with:

```bash
python Day_31_Databases/databases.py
```

The pattern applies to every lesson—navigate to the desired directory and run
its script to explore the material interactively.

## Featured lessons

- **Day 31 – Relational Databases** (`Day_31_Databases/databases.py`): builds and
  queries a SQLite database, mirroring production-ready analysis workflows.
- **Day 32 – Other Databases** (`Day_32_Other_Databases/other_databases.py`):
  demonstrates dependency-injected connection patterns for SQL and MongoDB
  clients so that data access logic remains testable.
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

## Running tests

```bash
python Day_31_Databases/databases.py
python Day_34_Building_an_API/api_server.py
```

## 🧾 Day 37 recap CLI

Day 37 wraps up the journey with a recap script that generates reusable
artifacts:

- `get_recap_checklist()` summarises the core program outcomes.
- `get_next_steps()` recommends actions to continue your learning.
- The command-line interface renders either section or both.

Run the recap from the project root:

```bash
python -m Day_37_Conclusion.conclusion
# or specify a section
python -m Day_37_Conclusion.conclusion --section next-steps
```

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
