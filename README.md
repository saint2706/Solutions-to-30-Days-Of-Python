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
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

### Optional database extras

Some lessons showcase connectors that live in optional packages:

- MySQL: `pip install mysql-connector-python`
- PostgreSQL: `pip install psycopg2-binary`
- MongoDB: `pip install pymongo`

Installing these extras is only necessary if you want to run the examples
against live services; the test suite uses mocks and runs without them.

## Lesson scripts

- [Day 31 – Relational Databases](Day_31_Databases/databases.py): builds and
  queries a SQLite database, mirroring production-ready analysis workflows.
- [Day 32 – Other Databases](Day_32_Other_Databases/other_databases.py):
  demonstrates dependency-injected connection patterns for SQL and MongoDB
  clients so that data access logic remains testable.

Run a lesson directly with `python <path-to-script>`. For example, Day 31 can
be executed via:

```bash
python Day_31_Databases/databases.py
```

## Running Pytest

Automated tests cover key helpers from the curriculum. Execute the entire test
suite with:

```bash
pytest
```

To focus on specific lessons:

```bash
pytest tests/test_day_31.py
pytest tests/test_day_32.py
```

The Day 32 tests rely solely on the dependency-injected stubs so they can run
without provisioning database services.
