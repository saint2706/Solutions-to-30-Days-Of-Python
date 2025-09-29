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

```bash
pytest
```

Run a single test module with:

```bash
pytest tests/test_day_37.py
```

## 🗺️ Repository overview

- `Day_01_Introduction` through `Day_50_MLOps`: daily lesson content.
- `Day_37_Conclusion/conclusion.py`: recap data structures and CLI entry point.
- `tests/`: unit tests for selected lessons.

## 🙌 Contributing

Have ideas to expand the business analytics focus? Open an issue or submit a
pull request—we welcome community contributions that keep the curriculum
practical and accessible.
