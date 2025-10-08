# Coding for MBA

> **A 67-day applied Python, analytics, and machine learning curriculum designed for business professionals.**

Transform your business acumen into technical capability with this comprehensive, hands-on curriculum. Each lesson is self-contained and builds toward end-to-end data fluency—from programming fundamentals to modern ML operations.

[![Python CI](https://github.com/saint2706/Coding-For-MBA/actions/workflows/ci.yml/badge.svg)](https://github.com/saint2706/Coding-For-MBA/actions/workflows/ci.yml)
[![Documentation](https://github.com/saint2706/Coding-For-MBA/actions/workflows/docs.yml/badge.svg)](https://saint2706.github.io/Coding-For-MBA/)

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/saint2706/Coding-For-MBA.git
cd Coding-For-MBA
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Optional database dependencies:**

```bash
pip install mysql-connector-python psycopg2-binary pymongo
```

## 📖 Documentation

**[View the full documentation site →](https://saint2706.github.io/Coding-For-MBA/)**

The documentation includes interactive examples, detailed explanations, and downloadable materials for each lesson.

## 🗺️ Curriculum Overview

The curriculum is organized into four progressive phases over 67 days:

| Phase | Days | Focus |
|-------|------|-------|
| **Phase 1** | 01-20 | Python foundations, data structures, file handling |
| **Phase 2** | 21-39 | Data workflows, databases, APIs, statistics, visualization |
| **Phase 3** | 40-54 | ML fundamentals, neural networks, NLP |
| **Phase 4** | 55-67 | Advanced ML, MLOps, transformers, deployment |

📘 **[See full curriculum roadmap →](docs/ml_curriculum.md)**

## 💻 Working with Lessons

Each `Day_XX_*` folder contains:

- **README.md** - Lesson content and explanations
- **Python scripts (.py)** - Executable code examples
- **Jupyter notebooks (.ipynb)** - Interactive versions
- **Solutions (where applicable)** - Reference implementations

**Launch Jupyter for interactive learning:**

```bash
jupyter notebook
# Navigate to any Day_XX folder and open the .ipynb file
```

## 📚 All Lessons

Quick access to all 67 lessons:

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

## ⭐ Featured Lessons

Explore some of the standout lessons that demonstrate production-ready patterns:

- **[Day 50 – MLOps](docs/featured-lessons.md#day-50--mlops)** - Model training, saving, and deployment patterns
- **[Day 58 – Transformers](docs/featured-lessons.md#day-58--transformers-and-attention)** - Attention mechanisms and Hugging Face integration
- **[Day 60 – Graph Learning](docs/featured-lessons.md#day-60--graph-and-geometric-learning)** - GraphSAGE and attention message passing
- **[Day 36 – Case Study](docs/featured-lessons.md#day-36--capstone-case-study)** - End-to-end analytics workflow

📘 **[View all featured lessons →](docs/featured-lessons.md)**

## 🧪 Testing & Development

### Running Tests

```bash
pip install -r requirements-dev.txt
pytest
```

Tests cover 233+ scenarios across all lesson phases with 40%+ coverage requirements.

### Code Formatting

```bash
make format  # Auto-format Python, notebooks, and Markdown
make lint    # Check formatting without changes
```

📘 **[Full development guide →](docs/contributing.md)**

## 📁 Repository Structure

```
├── Day_01_Introduction → Day_67_Model_Monitoring_and_Reliability/
│   └── Self-contained lessons with READMEs, scripts, and notebooks
├── docs/          # Documentation, curriculum roadmaps, guides
├── tools/         # Build scripts for docs and notebooks
├── tests/         # 233+ automated tests
└── data/          # Sample datasets
```

## 🙌 Contributing

We welcome contributions that keep the curriculum practical and accessible!

- 🐛 **Report bugs** via GitHub Issues
- 💡 **Suggest improvements** through Pull Requests
- 📖 **Improve documentation** - every contribution helps

📘 **[Read the contributing guide →](docs/contributing.md)**

## 📄 License

This project is open source and available under the [LICENSE](LICENSE) file in this repository.

______________________________________________________________________

**Built with ❤️ for business professionals learning data science and ML**
