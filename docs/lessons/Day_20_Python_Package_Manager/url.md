# 📘 Day 20: Python Package Manager (pip) & Third-Party Libraries

The real power of Python for data analysis comes from its vast ecosystem of third-party libraries. These are pre-written modules, created by the community, that provide powerful tools for specific tasks.

- **`requests`**: For making HTTP requests to APIs and websites.
- **`numpy`**: For numerical computing and advanced math.
- **`pandas`**: For data manipulation and analysis (we'll dive deep into this soon).
- **`beautifulsoup4`**: For web scraping.

## `pip` and `requirements.txt`

- **`pip`** is the standard tool for installing these packages. You use it in your terminal (e.g., `pip install requests`).
- A **`requirements.txt`** file is the standard way to list all the third-party packages your project depends on. This allows anyone (including you, on a different computer) to install all the necessary libraries at once using a single command: `pip install -r requirements.txt`.

## Environment Setup

This project now has a `requirements.txt` file at its root. Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to create a virtual environment and run `pip install -r requirements.txt`.

## Exploring the Refactored Code

The script for this lesson, `url.py`, demonstrates how to use `requests` to fetch data from live APIs and `numpy` to perform calculations. The code has been refactored to separate the data fetching logic from the data analysis logic, which is a crucial best practice.

1. **Review the Code:** Open `Day_20_Python_Package_Manager/url.py`. Notice the `fetch_api_data()` function, which is responsible for the network request, and the `analyze_...` functions, which take data as input and perform calculations.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script. It will make live calls to external APIs and print the analysis.
   ```bash
   python Day_20_Python_Package_Manager/url.py
   ```
1. **Run the Tests:** The tests for this lesson demonstrate a key testing technique: **mocking**. We replace the live network call with a "mock" object that returns sample data. This makes our tests fast, reliable, and independent of the network.
   ```bash
   pytest tests/test_day_20.py
   ```

## 💻 Exercises: Day 20

1. **Explore the `requests` Response:**

   - In a new script (`my_solutions_20.py`), import the `requests` library.
   - Make a `get` request to `"https://api.thecatapi.com/v1/breeds"`.
   - The object returned by `requests.get()` is a `Response` object. Print its `status_code` attribute (e.g., `response.status_code`) and its `headers` attribute.

1. **Analyze Different Metrics:**

   - Import the `fetch_api_data` and `analyze_breed_metrics` functions from the lesson script.
   - Fetch the cat breed data.
   - The `analyze_breed_metrics` function can analyze both `'weight'` and `'life_span'`. Call it for `'life_span'` and print the result.

1. **Find the Top 3 Origins:**

   - Import and use the `analyze_breed_origins` function, but modify the call so it returns the top 3 most common origins instead of the default 5.

🎉 **Congratulations!** You now understand how to leverage the vast Python ecosystem using `pip`. This skill unlocks a world of powerful tools for data analysis, machine learning, web development, and more.

Day 20: Python Package Manager - Working with Third-Party Libraries (Refactored).

```python

import json
import re
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import requests

# Optional import for web scraping
try:
    from bs4 import BeautifulSoup

    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# --- Data Fetching Functions ---


def fetch_api_data(url: str) -> Optional[List[Dict[str, Any]]]:
    """Fetches and parses JSON data from a given API endpoint."""
    try:
        print(f"📚 Fetching data from {url}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        print("✅ Data downloaded successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Error: Failed to decode JSON response.")
        return None


# --- Data Analysis Functions ---


def analyze_text_frequency(text: str, top_n: int = 5) -> List[Tuple[str, int]]:
    """Analyzes text to find the most common words."""
    words = re.findall(r"\b[a-z]+\b", text.lower())
    return Counter(words).most_common(top_n)


def parse_metric_range(metric_str: str) -> float:
    """Parses a string like '3 - 7' and returns the average."""
    try:
        parts = [float(p.strip()) for p in metric_str.split("-")]
        return sum(parts) / len(parts)
    except (ValueError, IndexError):
        return 0.0


def analyze_breed_metrics(
    breeds_data: List[Dict[str, Any]], metric: str, unit: str
) -> Optional[Dict[str, float]]:
    """Analyzes a specific metric (e.g., 'weight', 'life_span') from breed data."""
    values = []
    for breed in breeds_data:
        if metric == "weight" and "weight" in breed and "metric" in breed["weight"]:
            avg_value = parse_metric_range(breed["weight"]["metric"])
        elif metric == "life_span" and "life_span" in breed:
            avg_value = parse_metric_range(breed["life_span"])
        else:
            continue

        if avg_value > 0:
            values.append(avg_value)

    if not values:
        return None

    return {
        "unit": unit,
        "mean": np.mean(values),
        "median": np.median(values),
        "std_dev": np.std(values),
    }


def analyze_breed_origins(
    breeds_data: List[Dict[str, Any]], top_n: int = 5
) -> List[Tuple[str, int]]:
    """Analyzes the geographic distribution of cat breed origins."""
    origins = [
        breed["origin"]
        for breed in breeds_data
        if "origin" in breed and breed["origin"]
    ]
    return Counter(origins).most_common(top_n)


def main():
    """Main function to demonstrate package manager capabilities."""
    print("🚀 Day 20: Python Package Manager Demo\n")

    # 1. Analyze Cat Breed Data from TheCatAPI
    print("--- Analyzing Cat Breed Data ---")
    cat_breeds = fetch_api_data("https://api.thecatapi.com/v1/breeds")
    if cat_breeds:
        weight_stats = analyze_breed_metrics(cat_breeds, "weight", "kg")
        if weight_stats:
            print(
                f"Average Cat Weight: {weight_stats['mean']:.2f} {weight_stats['unit']}"
            )

        lifespan_stats = analyze_breed_metrics(cat_breeds, "life_span", "years")
        if lifespan_stats:
            print(
                f"Average Cat Lifespan: {lifespan_stats['mean']:.2f} {lifespan_stats['unit']}"
            )

        top_origins = analyze_breed_origins(cat_breeds)
        print("Top 5 Breed Origins:", top_origins)

    print("-" * 20)

    # 2. Web Scraping Demonstration (Optional)
    if BS4_AVAILABLE:
        print("\n--- Web Scraping Demonstration ---")
        try:
            response = requests.get("https://httpbin.org/html", timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.find("h1")
            print(f"Scraped Page Title: {title.get_text() if title else 'Not Found'}")
        except Exception as e:
            print(f"❌ Web scraping demo failed: {e}")
    else:
        print("\n--- Web Scraping Demonstration ---")
        print("BeautifulSoup4 not installed. Skipping.")

    print("\n✅ Demo complete!")


if __name__ == "__main__":
    main()

```
