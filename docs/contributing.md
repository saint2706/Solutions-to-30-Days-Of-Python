# Contributing Guide

Thank you for your interest in contributing to Coding for MBA! This guide will help you get started.

## 🤝 How to Contribute

We welcome contributions that:

- Expand the business analytics focus
- Improve lesson clarity and accessibility
- Fix bugs or improve code quality
- Enhance documentation
- Add or improve tests

## 📝 Contribution Workflow

1. **Fork the repository** and create a new branch
1. **Make your changes** following our coding standards
1. **Test your changes** thoroughly
1. **Submit a pull request** with a clear description

## 🧪 Testing

Automated tests live under `tests/` and cover representative helpers from the lessons.

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests with coverage
pytest

# Run specific test files
pytest tests/test_day_31.py
pytest tests/test_day_36.py
```

### Coverage Requirements

The project enforces a **40% minimum coverage** across:

- `Day_24_Pandas_Advanced.pandas_adv`
- `Day_25_Data_Cleaning.data_cleaning`
- `Day_26_Statistics.stats`

See `pytest.ini` for configuration.

### Writing Tests

When adding new lessons or refactoring code:

1. Add tests to `tests/` directory following the pattern `test_day_XX.py`
1. Use dependency injection for database/API tests (see `tests/test_day_32.py`)
1. Ensure deterministic behavior (fixed random seeds for ML code)
1. Test edge cases and business-relevant scenarios

Example test structure:

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

## 🧹 Code Formatting

The repository uses strict formatting standards defined in `pyproject.toml`:

- **Black**: Line length 88, Python 3.12 target
- **Ruff**: Linting and formatting (rules: E, F, I; ignore E501)
- **Line endings**: LF (Unix-style)
- **Quote style**: Double quotes

### Format Your Code

Before submitting a pull request, format your code:

```bash
# Auto-format all code
make format

# Check formatting without changes (CI check)
make lint
```

This command formats:

- Python modules with Black and Ruff
- Jupyter notebooks via `nbqa`
- Markdown files via `mdformat`

## 📖 Contributing to Documentation

### Building Documentation

1. Install documentation dependencies:

   ```bash
   pip install -r docs/requirements.txt
   ```

1. Generate lesson pages from Day\_\* READMEs:

   ```bash
   python tools/build_docs.py
   ```

1. Preview locally:

   ```bash
   mkdocs serve
   # Visit http://127.0.0.1:8000/
   ```

1. Build static site:

   ```bash
   mkdocs build --strict
   ```

### Documentation Guidelines

- **Lesson READMEs**: Each `Day_XX_*/README.md` is the source of truth
- **Generated files**: Don't edit `docs/lessons/day-*.md` directly
- **Link rewriting**: The build script rewrites relative links to GitHub
- **Material files**: Scripts append download links for `.py` and `.ipynb` files
- **Navigation**: Updated automatically in `mkdocs.yml` by build script

**Important:** Commit changes to source files (`README.md`, lesson READMEs, notebooks, etc.) rather than the generated `docs/lessons/day-*.md` pages.

The GitHub Actions workflow automatically builds and deploys the MkDocs site on every push to `main`.

## ♿ Accessible Exports

Generate screen-reader-friendly exports:

```bash
python tools/convert_lessons_to_notebooks.py
```

This creates:

- HTML exports with skip-navigation links
- Structured heading hierarchy
- Placeholder alt text for figures
- Markdown exports for offline use

Artifacts are written to `docs/lessons/Day_*/*.html` and `docs/lessons/Day_*/*.md`.

## 🔄 Dependency Management

### Core Dependencies

See `requirements.txt` for the full list. Key libraries:

- **Data**: numpy, pandas, scipy
- **ML**: scikit-learn, statsmodels
- **Visualization**: matplotlib, seaborn, plotly
- **Web**: requests, beautifulsoup4, flask
- **Databases**: pymongo, psycopg2-binary, mysql-connector-python

### Development Dependencies

See `requirements-dev.txt`:

- **Testing**: pytest, pytest-cov
- **Formatting**: black, ruff, nbqa, mdformat
- **Docs**: mkdocs, mkdocs-material

### Dependency Reviews

The library stack is reviewed periodically. See [`dependency-review.md`](dependency-review.md) for the latest upgrade log.

## 🏗️ Code Standards

### Lesson Code Structure

```python
"""Module docstring explaining the lesson focus."""

from __future__ import annotations

# Standard library imports
from typing import List, Dict, Optional

# Third-party imports
import numpy as np
import pandas as pd


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

### Key Principles

1. **Educational clarity**: Code should be clear and educational, not just efficient
1. **Self-contained lessons**: Each lesson should stand alone while building on previous concepts
1. **Business relevance**: Examples should be business-relevant when possible
1. **Progressive complexity**: Complexity should build gradually across lessons
1. **Comments for context**: Explain "why," not just "what"

### ML Code Reproducibility

For machine learning lessons:

- Use fixed random seeds (`np.random.seed(42)`)
- Document hyperparameters clearly
- Provide deterministic train/test splits
- Include evaluation metrics in docstrings

## 🚀 CI/CD Workflows

### Python CI (`ci.yml`)

Runs on push/PR to main when Python files or dependencies change:

- Checks formatting with `make format`
- Runs pytest suite
- Enforces coverage requirements

### Documentation (`docs.yml`)

Runs on push to main when docs or READMEs change:

- Generates lesson pages with `tools/build_docs.py`
- Builds and deploys MkDocs site to GitHub Pages

## 💡 Tips for Contributors

1. **Minimal changes**: Only modify what's necessary
1. **Test thoroughly**: Run tests before submitting
1. **Update docs**: Keep documentation in sync with code changes
1. **Follow patterns**: Look at existing lessons for guidance
1. **Ask questions**: Open an issue if you need clarification

## 📬 Questions or Issues?

- Open an issue for bugs or feature requests
- Start a discussion for questions or ideas
- Check existing issues and PRs before creating new ones

Thank you for contributing to make Coding for MBA better! 🎉
