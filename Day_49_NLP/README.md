# Day 49: Natural Language Processing (NLP)

## Overview

Day 49 introduces the classic feature-extraction techniques that turn raw
text into numeric matrices. Bag-of-words counts and TF-IDF scores are the
foundations for many traditional NLP pipelines and remain useful for quick
baselines or lightweight models.

## What's in this folder?

- `solutions.py` – exposes `build_count_matrix` and `build_tfidf_matrix`
  helper functions plus a small demo script that prints both
  representations for a sample corpus.

## Running the lesson script

Ensure the lesson dependencies are installed (in particular
`scikit-learn`, `pandas`, and `numpy`). Then execute the walkthrough:

```bash
python Day_49_NLP/solutions.py
```

## Running the tests

The automated checks validate the helper functions against a miniature
corpus. Run them with:

```bash
pytest tests/test_day_49.py
```

All tests expect to be run from the repository root so that imports
resolve correctly.
