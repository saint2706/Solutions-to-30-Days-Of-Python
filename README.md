# Coding for MBA

A 67-day applied Python, analytics, and machine learning curriculum designed
for business professionals. Each `Day_XX_*` directory is a self-contained
lesson that builds end-to-end data fluency—from programming fundamentals to
modern ML operations and monitoring.

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

Lessons are organised chronologically. Start with the [Machine Learning Curriculum Roadmap](docs/ml_curriculum.md) to see how the upper-level ML sequence layers onto the Python and analytics foundations built in Days 01–39.

**Phases at a glance**

- **Phase 1 – Python and analytics foundations (Days 01–20):** Core Python syntax, data structures, file handling, and early automation skills.
- **Phase 2 – Data workflows and statistics (Days 21–39):** Data ingestion, databases, APIs, statistics, and visualisation for business-ready analysis.
- **Phase 3 – Machine learning fundamentals (Days 40–54):** Regression, classification, unsupervised learning, feature engineering, and neural networks.
- **Phase 4 – Advanced ML & operations (Days 55–67):** Time series, recommenders, transformers, generative models, graph learning, reinforcement learning, modern NLP, and production-grade MLOps.

## Working with notebooks and scripts

Each lesson folder ships with a Jupyter notebook that mirrors the original
Python script. Launch Jupyter from the project root and open the notebook for
the topic you want to explore:

```bash
jupyter notebook
```

Navigate to a `Day_*` directory and select the relevant `.ipynb` file—for
instance, `Day_31_Databases/databases.ipynb` walks through the SQLite example
in an interactive notebook environment.

## Lessons

Use the table below to jump straight into any lesson in the 67-day journey.

| Day | Lesson |
| --- | --- |
| Day 01 | [📘 Day 1: Python for Business Analytics - First Steps](./lessons/day-01-introduction.md) |
| Day 02 | [📘 Day 2: Storing and Analyzing Business Data](./lessons/day-02-variables-builtin-functions.md) |
| Day 03 | [📘 Day 3: Operators - The Tools for Business Calculation and Logic](./lessons/day-03-operators.md) |
| Day 04 | [📘 Day 4: Working with Text Data - Strings](./lessons/day-04-strings.md) |
| Day 05 | [📘 Day 5: Managing Collections of Business Data with Lists](./lessons/day-05-lists.md) |
| Day 06 | [📘 Day 6: Tuples - Storing Immutable Business Data](./lessons/day-06-tuples.md) |
| Day 07 | [📘 Day 7: Sets - Managing Unique Business Data](./lessons/day-07-sets.md) |
| Day 08 | [📘 Day 8: Dictionaries - Structuring Complex Business Data](./lessons/day-08-dictionaries.md) |
| Day 09 | [📘 Day 9: Conditionals - Implementing Business Logic](./lessons/day-09-conditionals.md) |
| Day 10 | [📘 Day 10: Loops - Automating Repetitive Business Tasks](./lessons/day-10-loops.md) |
| Day 11 | [📘 Day 11: Functions - Creating Reusable Business Tools](./lessons/day-11-functions.md) |
| Day 12 | [📘 Day 12: List Comprehension - Elegant Data Manipulation](./lessons/day-12-list-comprehension.md) |
| Day 13 | [📘 Day 13: Higher-Order Functions & Lambda](./lessons/day-13-higher-order-functions.md) |
| Day 14 | [📘 Day 14: Modules - Organizing Your Business Logic](./lessons/day-14-modules.md) |
| Day 15 | [📘 Day 15: Exception Handling - Building Robust Business Logic](./lessons/day-15-exception-handling.md) |
| Day 16 | [📘 Day 16: File Handling for Business Analytics](./lessons/day-16-file-handling.md) |
| Day 17 | [📘 Day 17: Regular Expressions for Text Pattern Matching](./lessons/day-17-regular-expressions.md) |
| Day 18 | [📘 Day 18: Classes and Objects - Modeling Business Concepts](./lessons/day-18-classes-and-objects.md) |
| Day 19 | [📘 Day 19: Working with Dates and Times](./lessons/day-19-python-date-time.md) |
| Day 20 | [📘 Day 20: Python Package Manager (pip) & Third-Party Libraries](./lessons/day-20-python-package-manager.md) |
| Day 21 | [📘 Day 21: Virtual Environments - Professional Project Management](./lessons/day-21-virtual-environments.md) |
| Day 22 | [📘 Day 22: NumPy - The Foundation of Numerical Computing](./lessons/day-22-numpy.md) |
| Day 23 | [📘 Day 23: Pandas - Your Data Analysis Superpower](./lessons/day-23-pandas.md) |
| Day 24 | [📘 Day 24: Advanced Pandas - Working with Real Data](./lessons/day-24-pandas-advanced.md) |
| Day 25 | [📘 Day 25: Data Cleaning - The Most Important Skill in Analytics](./lessons/day-25-data-cleaning.md) |
| Day 26 | [📘 Day 26: Practical Statistics for Business Analysis](./lessons/day-26-statistics.md) |
| Day 27 | [📘 Day 27: Data Visualization - Communicating Insights](./lessons/day-27-visualization.md) |
| Day 28 | [📘 Day 28: Advanced Visualization & Customization](./lessons/day-28-advanced-visualization.md) |
| Day 29 | [📘 Day 29: Interactive Visualization with Plotly](./lessons/day-29-interactive-visualization.md) |
| Day 30 | [📘 Day 30: Web Scraping - Extracting Data from the Web](./lessons/day-30-web-scraping.md) |
| Day 31 | [📘 Day 31: Working with Databases in Python](./lessons/day-31-databases.md) |
| Day 32 | [📘 Day 32: Connecting to Other Databases (MySQL & MongoDB)](./lessons/day-32-other-databases.md) |
| Day 33 | [📘 Day 33: Accessing Web APIs with `requests`](./lessons/day-33-api.md) |
| Day 34 | [📘 Day 34: Building a Simple API with Flask](./lessons/day-34-building-an-api.md) |
| Day 35 | [🌐 Day 35: Flask Web Framework](./lessons/day-35-flask-web-framework.md) |
| Day 36 | [📊 Day 36 – Capstone Case Study](./lessons/day-36-case-study.md) |
| Day 37 | [🎉 Day 37: Conclusion & Your Journey Forward 🎉](./lessons/day-37-conclusion.md) |
| Day 38 | [Day 38: Math Foundations - Linear Algebra](./lessons/day-38-linear-algebra.md) |
| Day 39 | [Day 39: Math Foundations - Calculus](./lessons/day-39-calculus.md) |
| Day 40 | [Day 40: Introduction to Machine Learning & Core Concepts](./lessons/day-40-intro-to-ml.md) |
| Day 41 | [Day 41 · Supervised Learning – Regression](./lessons/day-41-supervised-learning-regression.md) |
| Day 42 | [Day 42 · Supervised Learning – Classification (Part 1)](./lessons/day-42-supervised-learning-classification-part-1.md) |
| Day 43 | [Day 43 · Supervised Learning – Classification (Part 2)](./lessons/day-43-supervised-learning-classification-part-2.md) |
| Day 44 | [Day 44: Unsupervised Learning](./lessons/day-44-unsupervised-learning.md) |
| Day 45 | [Day 45: Feature Engineering & Model Evaluation](./lessons/day-45-feature-engineering-and-evaluation.md) |
| Day 46 | [Day 46: Introduction to Neural Networks & Frameworks](./lessons/day-46-intro-to-neural-networks.md) |
| Day 47 | [Day 47: Convolutional Neural Networks (CNNs) for Computer Vision](./lessons/day-47-convolutional-neural-networks.md) |
| Day 48 | [Day 48: Recurrent Neural Networks (RNNs) for Sequence Data](./lessons/day-48-recurrent-neural-networks.md) |
| Day 49 | [Day 49: Natural Language Processing (NLP)](./lessons/day-49-nlp.md) |
| Day 50 | [Day 50: MLOps - Model Deployment](./lessons/day-50-mlops.md) |
| Day 51 | [Day 51 – Regularised Models](./lessons/day-51-regularized-models.md) |
| Day 52 | [Day 52 – Ensemble Methods](./lessons/day-52-ensemble-methods.md) |
| Day 53 | [Day 53 – Model Tuning and Feature Selection](./lessons/day-53-model-tuning-and-feature-selection.md) |
| Day 54 | [Day 54 – Probabilistic Modeling](./lessons/day-54-probabilistic-modeling.md) |
| Day 55 | [Day 55 – Advanced Unsupervised Learning](./lessons/day-55-advanced-unsupervised-learning.md) |
| Day 56 | [Day 56 – Time Series and Forecasting](./lessons/day-56-time-series-and-forecasting.md) |
| Day 57 | [Day 57 – Recommender Systems](./lessons/day-57-recommender-systems.md) |
| Day 58 | [Day 58 – Transformers and Attention](./lessons/day-58-transformers-and-attention.md) |
| Day 59 | [Day 59 – Generative Models](./lessons/day-59-generative-models.md) |
| Day 60 | [Day 60 – Graph and Geometric Learning](./lessons/day-60-graph-and-geometric-learning.md) |
| Day 61 | [Day 61 – Reinforcement and Offline Learning](./lessons/day-61-reinforcement-and-offline-learning.md) |
| Day 62 | [Day 62 – Model Interpretability and Fairness](./lessons/day-62-model-interpretability-and-fairness.md) |
| Day 63 | [Day 63 – Causal Inference and Uplift Modeling](./lessons/day-63-causal-inference-and-uplift.md) |
| Day 64 | [Day 64 – Modern NLP Pipelines](./lessons/day-64-modern-nlp-pipelines.md) |
| Day 65 | [Day 65 – MLOps Pipelines and CI/CD Automation](./lessons/day-65-mlops-pipelines-and-ci.md) |
| Day 66 | [Day 66 – Model Deployment and Serving Patterns](./lessons/day-66-model-deployment-and-serving.md) |
| Day 67 | [Day 67 – Model Monitoring and Reliability Engineering](./lessons/day-67-model-monitoring-and-reliability.md) |

## ♿ Accessible lesson exports

Run `python tools/convert_lessons_to_notebooks.py` to regenerate the notebooks
alongside screen-reader-friendly HTML and Markdown exports. The static
artifacts are written to `docs/lessons/Day_*/*.html` and
`docs/lessons/Day_*/*.md`, complete with skip-navigation links, a structured
heading hierarchy, and placeholder alt text for every figure. These exports are
perfect for learners who prefer assistive technology or need an offline copy of
the curriculum.

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
Markdown documents. After installing `requirements-dev.txt`, run the unified
command from the project root before opening a pull request:

```bash
make format
```

This wraps the standard sequence—`ruff check --fix`, `ruff format`, notebook
formatting via `nbqa`, and `mdformat` for Markdown—so that Python modules,
Jupyter notebooks, and documentation stay in sync with the shared
configuration defined in `pyproject.toml`. To check formatting without making
changes (the command used in CI), run `make lint` instead.

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

- `Day_01_Introduction` – `Day_20_Python_Package_Manager`: Python foundations, data structures, files, and automation basics.
- `Day_21_Virtual_Environments` – `Day_39_Calculus`: analytics stack, databases, APIs, statistics, visualisation, and core maths refreshers.
- `Day_40_Intro_to_ML` – `Day_49_NLP`: supervised and unsupervised ML progression, neural networks, NLP, and evaluation tooling.
- `Day_50_MLOps` – `Day_57_Recommender_Systems`: production workflows, time series, recommenders, and end-to-end project scaffolds.
- `Day_58_Transformers_and_Attention` – `Day_64_Modern_NLP_Pipelines`: modern deep learning techniques, generative models, and advanced NLP pipelines.
- `Day_65_MLOps_Pipelines_and_CI` – `Day_67_Model_Monitoring_and_Reliability`: CI/CD, deployment, monitoring, and reliability engineering for ML systems.
- `docs/`: curriculum roadmaps, dependency reviews, and additional guidance.
- `tools/`: utilities such as `convert_lessons_to_notebooks.py` for maintaining dual script/notebook workflows.
- `tests/`: unit tests for selected lessons and pipelines.

## 🙌 Contributing

Have ideas to expand the business analytics focus? Open an issue or submit a
pull request—we welcome community contributions that keep the curriculum
practical and accessible.
