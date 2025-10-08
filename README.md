# Coding for MBA

A 57-day applied Python and analytics curriculum designed for business
professionals. Each `Day_XX_*` directory contains a self-contained lesson that
walks through practical data skills, from programming fundamentals to
introductory machine learning.

## 🚀 Quick start

```bash
git clone https://github.com/saint2706/Coding-For-MBA.git
cd Coding-For-MBA
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`
pip install -r requirements.txt
```

Optional extras for database-focused lessons:

- MySQL: `pip install mysql-connector-python`
- PostgreSQL: `pip install psycopg2-binary`
- MongoDB: `pip install pymongo`

## 📖 Documentation site

An MkDocs site styled with the **Material** theme (including a light/dark mode toggle) is published automatically from `main` at
[`https://saint2706.github.io/Coding-For-MBA/`](https://saint2706.github.io/Coding-For-MBA/).

### Preview the docs locally

```bash
pip install -r docs/requirements.txt
python tools/build_docs.py
mkdocs serve
```

The build script ingests every `Day_*` README, rewrites internal links so they
point back to GitHub, and appends quick links to each lesson's notebooks or
Python scripts before the MkDocs build runs.

## 📚 Navigating the lessons

Lessons are organised chronologically. Start with the [Machine Learning Curriculum Roadmap](docs/ml_curriculum.md) if you want to understand how the Day 40–57 sequence grows into an end-to-end ML capability.

**Phases at a glance**

- **Phase 1 – Classic ML foundations:** Day 40–57 walk through supervised/unsupervised learning, neural networks, probabilistic modelling, time series, recommenders, NLP, and an MLOps primer.
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

## 🤝 Contributing to the docs

1. Install the documentation dependencies with `pip install -r docs/requirements.txt`.
2. Run `python tools/build_docs.py` to regenerate the lesson pages from the
   latest READMEs.
3. Preview locally with `mkdocs serve` and open `http://127.0.0.1:8000/`.
4. Commit changes to source files (`README.md`, lesson READMEs, notebooks, etc.)
   rather than the generated `docs/lessons/day-*.md` pages.

The GitHub Actions workflow builds the MkDocs site on every push to `main` and deploys
it to GitHub Pages.

## Featured lessons

- **Day 58 – Transformers and Attention** (`Day_58_Transformers_and_Attention/solutions.py`):
  builds encoder–decoder stacks, deterministic transformer text classifiers,
  Hugging Face fine-tuning playbooks, and attention visualisations for rapid
  experimentation.
- **Day 59 – Generative Models** (`Day_59_Generative_Models/solutions.py`):
  contrasts autoencoders, VAEs, GAN dynamics, and diffusion denoisers with
  synthetic training loops that log reconstruction improvements.
- **Day 60 – Graph and Geometric Learning**
  (`Day_60_Graph_and_Geometric_Learning/solutions.py`): implements GraphSAGE
  and graph attention message passing for toy node-classification graphs with
  interpretable attention matrices.
- **Day 61 – Reinforcement and Offline Learning**
  (`Day_61_Reinforcement_and_Offline_Learning/solutions.py`): simulates
  policy-gradient bandits, tabular value iteration, contextual bandits, and
  offline evaluation with deterministic reward thresholds for regression
  testing.
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
- **Day 54 – Probabilistic Modeling** (`Day_54_Probabilistic_Modeling/solutions.py`):
  provides Gaussian mixtures, expectation-maximisation, Bayesian classifiers,
  and hidden Markov model log-likelihood utilities for reasoning under
  uncertainty.
- **Day 55 – Advanced Unsupervised Learning**
  (`Day_55_Advanced_Unsupervised_Learning/solutions.py`): explores DBSCAN,
  agglomerative clustering, t-SNE embeddings, autoencoders, and anomaly
  detection baselines.
- **Day 56 – Time Series & Forecasting**
  (`Day_56_Time_Series_and_Forecasting/solutions.py`): fits ARIMA/SARIMAX,
  Holt-Winters, and Prophet-style models with rolling-origin evaluation
  helpers.
- **Day 57 – Recommender Systems**
  (`Day_57_Recommender_Systems/solutions.py`): implements collaborative
  filtering, matrix factorisation, and ranking metrics for implicit-feedback
  aware recommenders.
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
