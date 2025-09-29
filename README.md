# Coding for MBA

## Overview

Coding for MBA is a curated set of fifty daily lessons that blend Python, data
analysis, and introductory machine learning skills for business-minded
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

## Script Usage

Every lesson can be executed individually. For example, Day 31 demonstrates how
to build and query a SQLite database:

```bash
python Day_31_Databases/databases.py
```

The script creates a temporary `company_data.db` file, prints query results, and
cleans up the database once it finishes.

## Running Pytest

Automated tests cover selected lessons, including Day 31's database helpers.
Run the full suite with:

```bash
pytest
```

To focus on the Day 31 tests only, use:

```bash
pytest tests/test_day_31.py
```

