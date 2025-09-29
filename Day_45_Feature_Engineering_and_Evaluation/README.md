# Day 45: Feature Engineering & Model Evaluation

## Overview

Day 45 demonstrates how thoughtful preprocessing and rigorous evaluation
combine to build trustworthy models:

- **Feature engineering pipelines** clean, scale, and encode raw columns so
  downstream estimators receive consistent numeric inputs.
- **Evaluation workflows** compare predictions against held-out data using
  confusion matrices and rich classification reports.

Install scikit-learn before exploring the examples:

```bash
pip install scikit-learn
```

## What's inside

- `solutions.py` – helper functions for assembling preprocessing pipelines,
  transforming the toy dataset, training a logistic regression model, and
  returning evaluation metrics.
- `README.md` – lesson overview (this document).

## Running the lesson script

Execute the end-to-end walkthrough, which prints processed feature arrays,
confusion matrix details, and a classification report:

```bash
python Day_45_Feature_Engineering_and_Evaluation/solutions.py
```

## Running the tests

Run the dedicated Day 45 tests to validate the preprocessing and evaluation
utilities:

```bash
pytest tests/test_day_45.py
```

To execute the entire project test suite, run `pytest` from the repository
root.

## Further exploration

- Swap in additional categorical columns and confirm that the preprocessing
  pipeline scales automatically.
- Replace the logistic regression classifier in `build_model_pipeline` with
  another estimator (e.g., RandomForestClassifier) and compare the resulting
  confusion matrix.
