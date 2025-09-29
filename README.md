# Coding for MBA

A guided collection of Python, data, and machine learning exercises designed for business-minded learners. Each `Day_XX_*` folder contains short lessons, scripts, and notebooks that build on one another.

## 1. Installation

```bash
git clone https://github.com/your-username/Coding-For-MBA.git
cd Coding-For-MBA
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`
pip install -r requirements.txt
```

## 2. Day 29 resources

### Run the interactive visualization script

Execute the refactored script to load the bundled `sales_data.csv` file and open the figures:

```bash
python Day_29_Interactive_Visualization/interactive_visualization.py
```

### Explore the interactive notebook

Launch Jupyter and open the new walkthrough notebook:

```bash
jupyter notebook Day_29_Interactive_Visualization/interactive_visualization.ipynb
```

### Execute the automated tests

Pytest checks validate the figure construction helpers:

```bash
pytest tests/test_day_29.py
```

## 3. Repository layout

- `Day_01_Introduction` ... `Day_50_MLOps` – daily folders covering Python, analytics, and machine learning topics.
- `tests/` – lightweight unit tests for selected lessons.
- `requirements.txt` – Python dependencies used across the curriculum.

## 4. Contributing

Issues and pull requests are welcome. Please include tests and documentation updates alongside code changes.
