# GitHub Copilot Instructions for Coding-For-MBA

This repository contains a comprehensive 67-day Python, analytics, and machine learning curriculum designed for business professionals. When contributing to this project, please follow these guidelines.

## Repository Structure

This is an educational curriculum organized into daily lessons:

- **Days 01-20**: Python foundations (syntax, data structures, file handling)
- **Days 21-39**: Data workflows (NumPy, Pandas, databases, APIs, visualization, statistics)
- **Days 40-54**: ML fundamentals (regression, classification, neural networks)
- **Days 55-67**: Advanced ML & MLOps (time series, transformers, deployment, monitoring)

Each `Day_XX_*` directory is a self-contained lesson with:

- `README.md` - Lesson content and explanations
- Python scripts (`.py`) - Executable lesson code
- Jupyter notebooks (`.ipynb`) - Interactive versions
- `solutions.py` - Reference implementations for advanced lessons

Additional directories:

- `docs/` - MkDocs documentation site sources
- `tools/` - Build scripts for documentation and notebooks
- `tests/` - Unit tests for key lessons
- `data/` - Sample datasets

## Development Environment

- **Python version**: 3.12 (primary), 3.11 (docs)
- **Package manager**: pip with `requirements.txt` and `requirements-dev.txt`
- **Virtual environment**: Use `python -m venv .venv` for isolation

### Quick Setup

```bash
git clone https://github.com/saint2706/Coding-For-MBA.git
cd Coding-For-MBA
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Code Style and Formatting

This project uses strict formatting standards defined in `pyproject.toml`:

- **Black**: Line length 88, Python 3.12 target
- **Ruff**: Linting and formatting (rules: E, F, I; ignore E501)
- **Line endings**: LF (Unix-style)
- **Quote style**: Double quotes

### Commands

```bash
# Auto-format all code
make format

# Check formatting without changes (CI check)
make lint
```

Always run `make format` before committing to ensure consistency across Python modules, Jupyter notebooks (via `nbqa`), and Markdown files (via `mdformat`).

## Testing

Tests are located in `tests/` and cover representative helpers from lessons.

### Running Tests

```bash
# Install test dependencies
pip install -r requirements-dev.txt

# Run all tests with coverage
pytest

# Run specific test files
pytest tests/test_day_31.py
pytest tests/test_day_37.py
pytest tests/test_day_50.py
```

### Coverage Requirements

The project enforces a 40% minimum coverage across:

- `Day_24_Pandas_Advanced.pandas_adv`
- `Day_25_Data_Cleaning.data_cleaning`
- `Day_26_Statistics.stats`

See `pytest.ini` for configuration.

### Writing Tests

When adding new lessons or refactoring existing code:

1. Add tests to `tests/` directory following the pattern `test_day_XX.py`
1. Use dependency injection for database/API tests (see `tests/test_day_32.py`)
1. Ensure deterministic behavior (fixed random seeds for ML code)
1. Test edge cases and business-relevant scenarios

## Documentation

Documentation is built with MkDocs and Material theme, deployed to GitHub Pages.

### Building Documentation

```bash
# Install docs dependencies
pip install -r docs/requirements.txt

# Generate lesson pages from Day_* READMEs
python tools/build_docs.py

# Preview locally
mkdocs serve
# Visit http://127.0.0.1:8000/

# Build static site
mkdocs build --strict
```

### Documentation Guidelines

1. **Lesson READMEs**: Each `Day_XX_*/README.md` is the source of truth
1. **Generated files**: Don't edit `docs/lessons/day-*.md` directly
1. **Link rewriting**: The build script rewrites relative links to GitHub
1. **Material files**: Scripts append download links for `.py` and `.ipynb` files
1. **Navigation**: Updated automatically in `mkdocs.yml` by build script

## AGENTS.md Commands

The repository includes custom commands in `AGENTS.md`:

- `setup`: Install dependencies (apt packages, pip requirements)
- `run`: Execute the latest lesson script automatically
- `test`: Run pytest suite
- `lint`: Check code quality with black and ruff
- `format`: Auto-format Python files
- `notebook`: Launch Jupyter Notebook server

These commands are primarily for automation and CI/CD workflows.

## Contribution Guidelines

When making changes:

1. **Minimal modifications**: Change only what's necessary to address the issue
1. **Lesson integrity**: Each lesson should remain self-contained
1. **Backwards compatibility**: Don't break existing lesson code
1. **Test coverage**: Add tests for new functionality
1. **Documentation**: Update READMEs when changing lesson behavior
1. **Formatting**: Run `make format` before committing

### Pull Request Checklist

- [ ] Code follows Black/Ruff formatting standards
- [ ] Tests pass locally (`pytest`)
- [ ] Documentation updated if needed
- [ ] No breaking changes to existing lessons
- [ ] Lesson READMEs are clear and accurate

## Common Patterns

### Lesson Code Structure

```python
"""Module docstring explaining the lesson focus."""

from __future__ import annotations

# Standard library imports
from typing import List, Dict, Optional

# Third-party imports
import numpy as np
import pandas as pd

# Function definitions with clear docstrings
def example_function(data: pd.DataFrame) -> Dict[str, float]:
    """
    Brief description of what the function does.
    
    Parameters
    ----------
    data : pd.DataFrame
        Description of the input parameter
        
    Returns
    -------
    Dict[str, float]
        Description of the return value
    """
    # Implementation
    pass

# CLI or main execution
if __name__ == "__main__":
    # Demo code for standalone execution
    pass
```

### Testing Pattern

```python
"""Test module for Day XX lesson."""

import pytest
from Day_XX_Topic.module import function_to_test


def test_function_basic_case():
    """Test function with standard input."""
    result = function_to_test(input_data)
    assert result == expected_output


def test_function_edge_case():
    """Test function handles edge cases correctly."""
    result = function_to_test(edge_case_input)
    assert result is not None
```

### ML Code Reproducibility

For machine learning lessons:

- Use fixed random seeds (`np.random.seed(42)`)
- Document hyperparameters clearly
- Provide deterministic train/test splits
- Include evaluation metrics in docstrings

## Key Dependencies

Core libraries (see `requirements.txt`):

- **Data**: numpy, pandas, scipy
- **ML**: scikit-learn, statsmodels
- **Visualization**: matplotlib, seaborn, plotly
- **Web**: requests, beautifulsoup4, flask
- **Databases**: pymongo, psycopg2-binary, mysql-connector-python

Development tools (see `requirements-dev.txt`):

- **Testing**: pytest, pytest-cov
- **Formatting**: black, ruff, nbqa, mdformat
- **Docs**: mkdocs, mkdocs-material

## CI/CD Workflows

Two GitHub Actions workflows:

1. **Python CI** (`.github/workflows/ci.yml`):

   - Runs on push/PR to main
   - Checks formatting with `make format`
   - Runs pytest suite

1. **Documentation** (`.github/workflows/docs.yml`):

   - Runs on push to main
   - Generates lesson pages with `tools/build_docs.py`
   - Builds and deploys MkDocs site to GitHub Pages

## Need Help?

- Check existing lessons for patterns and examples
- Review `README.md` for project overview
- See `docs/ml_curriculum.md` for curriculum roadmap
- Look at `tools/build_docs.py` for documentation build logic
- Examine tests in `tests/` for testing patterns

## Educational Context

Remember that this is a teaching repository:

- Code should be clear and educational, not just efficient
- Comments should explain "why," not just "what"
- Examples should be business-relevant when possible
- Complexity should build gradually across lessons
- Each lesson should stand alone while building on previous concepts
