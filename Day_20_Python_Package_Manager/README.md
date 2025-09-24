# 📦 Day 20: Python Package Manager (pip)

## Welcome to Day 20

Today, we'll learn about the **Python Package Manager (pip)**, which is a tool for installing and managing third-party libraries (also known as packages) in Python.

## Why is Package Management Important for Business Analytics?

The real power of Python for business analytics comes from its vast ecosystem of third-party libraries. These libraries provide pre-written code for a wide range of tasks, such as:

- **`pandas`**: For data manipulation and analysis.
- **`numpy`**: For numerical computing.
- **`matplotlib` and `seaborn`**: For data visualization.
- **`scikit-learn`**: For machine learning.
- **`requests`**: For making HTTP requests to APIs and websites.

`pip` is the tool that allows you to easily install and manage these libraries.

## Using `pip`

`pip` is a command-line tool that comes with Python. You can use it to:

- **Install a package**: `pip install package_name`
- **Uninstall a package**: `pip uninstall package_name`
- **List installed packages**: `pip list`
- **See details about a package**: `pip show package_name`

## Exploring `url.py`

The `url.py` script in this folder provides an example of using the `requests` library, which is a popular third-party package for making HTTP requests. The script fetches data from a public API and performs some analysis on it.

To run this script, you first need to install the `requests` library:

```bash
pip install requests
```

## 💻 Exercises: Day 20

1. **Install a package**:
    - Open your terminal or command prompt and install the `pandas` library using `pip`.
    - Verify that the package is installed by running `pip show pandas`.

2. **Explore a package**:
    - The `url.py` script uses the `requests` library to fetch data from a cat API.
    - Read the documentation for the `requests` library to understand how the `get()` function works. You can find the documentation at [https://requests.readthedocs.io/](https://requests.readthedocs.io/).

3. **Analyze country data**:
    - The `url.py` script also contains a commented-out section that fetches data from a countries API.
    - Uncomment this section and run the script.
    - Modify the script to find the top 5 largest countries by area.

### Solutions

You can find the solutions to these exercises in the `solutions.py` file in this directory.

🎉 **Congratulations!** You've learned how to use `pip` to manage third-party libraries in Python. You now have access to a vast ecosystem of tools that will supercharge your business analytics skills.
