# Coding for MBA

## Overview

Coding for MBA is a curated set of fifty daily lessons that blend Python,
analytics, and introductory machine learning skills for business-minded
learners. Each `Day_XX_*` directory contains self-contained scripts or
notebooks that build progressively toward data fluency.

## Environment Setup

Use the following steps to create a local development environment:

```bash
git clone https://github.com/your-username/Coding-For-MBA.git
cd Coding-For-MBA
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`
pip install -r requirements.txt
```

### Optional database extras

Some lessons showcase connectors that live in optional packages:

- MySQL: `pip install mysql-connector-python`
- PostgreSQL: `pip install psycopg2-binary`
- MongoDB: `pip install pymongo`

Installing these extras is only necessary if you want to run the examples
against live services; the test suite uses mocks and runs without them.

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

Automated tests cover key helpers from the curriculum. Execute the entire test
suite with:

```bash
pytest
```

To focus on specific lessons:

```bash
pytest tests/test_day_31.py
pytest tests/test_day_32.py
pytest tests/test_day_50.py
```

The Day 32 tests rely solely on dependency-injected stubs, so they can run
without provisioning database services. The Day 50 test trains a seeded subset
of the Iris dataset, persists the model to a temporary location, reloads it, and
verifies that predictions remain consistent.
