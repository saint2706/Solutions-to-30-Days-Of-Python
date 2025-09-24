"""Day 20: Python Package Manager - Working with Third-Party Libraries

This script demonstrates how to use popular Python packages for data analysis
and API interaction. It showcases the power of pip and the Python ecosystem
for business analytics.

Required packages:
- requests: For HT    try:
        from bs4 import BeautifulSoup  # Import here to avoid issues if not available

        print("\\n🕷️  Web Scraping Demonstration")
        print("   Note: This is for educational purposes only.")

        # Example: Scraping a simple, scraping-friendly site
        url = 'https://httpbin.org/html'
        print(f"   Fetching content from: {url}")

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1')

        if title:
            print(f"   Page title: {title.get_text()}")
        else:
            print("   No title found")I calls
- numpy: For numerical computations
- beautifulsoup4: For web scraping (optional)

Install with: pip install requests numpy beautifulsoup4
"""

import requests
import numpy as np
from collections import Counter
from typing import List, Dict, Tuple, Any, Optional
from pprint import pprint

# Optional import for web scraping
try:
    from bs4 import BeautifulSoup

    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False
    print("BeautifulSoup4 not available. Web scraping features disabled.")


def analyze_text_frequency(text: str, top_n: int = 10) -> List[Tuple[str, int]]:
    """Analyze text and return the most common words.

    Args:
        text (str): Text to analyze
        top_n (int): Number of top words to return

    Returns:
        List[Tuple[str, int]]: List of (word, frequency) tuples
    """
    words = text.lower().split()
    # Filter out common punctuation and short words
    filtered_words = [word.strip('.,!?;:"()[]') for word in words if len(word) > 3]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(top_n)


def fetch_gutenberg_text(
    url: str = "https://www.gutenberg.org/files/1112/1112.txt",
) -> Optional[str]:
    """Fetch text from Project Gutenberg for analysis.

    Args:
        url (str): URL to fetch text from

    Returns:
        Optional[str]: Text content if successful, None otherwise
    """
    try:
        print(f"📚 Fetching text from Project Gutenberg...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("✅ Text downloaded successfully!")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching text: {e}")
        return None


def analyze_cat_breed_data() -> None:
    """Analyze cat breed data from TheCatAPI for business insights.

    This demonstrates how businesses might analyze product or demographic data
    using APIs and statistical analysis.
    """
    try:
        print("\n🐱 Fetching cat breed data from TheCatAPI...")
        response = requests.get("https://api.thecatapi.com/v1/breeds", timeout=10)
        response.raise_for_status()

        breeds_data = response.json()
        print(f"✅ Retrieved data for {len(breeds_data)} cat breeds")

        # Analyze weight data
        print("\n📊 WEIGHT ANALYSIS")
        analyze_weight_metrics(breeds_data)

        # Analyze lifespan data
        print("\n📊 LIFESPAN ANALYSIS")
        analyze_lifespan_metrics(breeds_data)

        # Analyze origin distribution
        print("\n🌍 ORIGIN DISTRIBUTION")
        analyze_breed_origins(breeds_data)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching cat breed data: {e}")
    except Exception as e:
        print(f"❌ Error analyzing data: {e}")


def parse_weight_range(weight_str: str) -> float:
    """Parse weight range string and return average weight.

    Args:
        weight_str (str): Weight range like '3 - 7' or '5'

    Returns:
        float: Average weight
    """
    try:
        parts = weight_str.split(" - ")
        if len(parts) == 2:
            return (float(parts[0]) + float(parts[1])) / 2
        else:
            return float(parts[0])
    except (ValueError, IndexError):
        return 0.0


def parse_lifespan_range(lifespan_str: str) -> float:
    """Parse lifespan range string and return average lifespan.

    Args:
        lifespan_str (str): Lifespan range like '12 - 15' or '14'

    Returns:
        float: Average lifespan in years
    """
    try:
        parts = lifespan_str.split(" - ")
        if len(parts) == 2:
            return (float(parts[0]) + float(parts[1])) / 2
        else:
            return float(parts[0])
    except (ValueError, IndexError):
        return 0.0


def analyze_weight_metrics(breeds_data: List[Dict[str, Any]]) -> None:
    """Analyze weight statistics across cat breeds.

    Args:
        breeds_data (List[Dict]): List of breed dictionaries
    """
    weights = []

    for breed in breeds_data:
        if "weight" in breed and "metric" in breed["weight"]:
            avg_weight = parse_weight_range(breed["weight"]["metric"])
            if avg_weight > 0:
                weights.append(avg_weight)

    if weights:
        print(f"   Sample Size: {len(weights)} breeds")
        print(f"   Mean Weight: {np.mean(weights):.2f} kg")
        print(f"   Median Weight: {np.median(weights):.2f} kg")
        print(f"   Std Deviation: {np.std(weights):.2f} kg")
        print(f"   Min Weight: {min(weights):.2f} kg")
        print(f"   Max Weight: {max(weights):.2f} kg")
    else:
        print("   No weight data available")


def analyze_lifespan_metrics(breeds_data: List[Dict[str, Any]]) -> None:
    """Analyze lifespan statistics across cat breeds.

    Args:
        breeds_data (List[Dict]): List of breed dictionaries
    """
    lifespans = []

    for breed in breeds_data:
        if "life_span" in breed:
            avg_lifespan = parse_lifespan_range(breed["life_span"])
            if avg_lifespan > 0:
                lifespans.append(avg_lifespan)

    if lifespans:
        print(f"   Sample Size: {len(lifespans)} breeds")
        print(f"   Mean Lifespan: {np.mean(lifespans):.2f} years")
        print(f"   Median Lifespan: {np.median(lifespans):.2f} years")
        print(f"   Std Deviation: {np.std(lifespans):.2f} years")
        print(f"   Min Lifespan: {min(lifespans):.2f} years")
        print(f"   Max Lifespan: {max(lifespans):.2f} years")
    else:
        print("   No lifespan data available")


def analyze_breed_origins(breeds_data: List[Dict[str, Any]]) -> None:
    """Analyze the geographic distribution of cat breed origins.

    Args:
        breeds_data (List[Dict]): List of breed dictionaries
    """
    origins = []

    for breed in breeds_data:
        if "origin" in breed and breed["origin"]:
            origins.append(breed["origin"])

    if origins:
        origin_counts = Counter(origins)
        sorted_origins = dict(
            sorted(origin_counts.items(), key=lambda x: x[1], reverse=True)
        )

        print(f"   Total Origins: {len(sorted_origins)}")
        print("   Top 10 Countries by Number of Breeds:")
        for i, (country, count) in enumerate(list(sorted_origins.items())[:10], 1):
            print(f"   {i:2d}. {country}: {count} breeds")
    else:
        print("   No origin data available")


def analyze_country_data() -> None:
    """Analyze world country data for business market analysis.

    This demonstrates how businesses might analyze geographic markets,
    population data, and economic indicators for expansion planning.
    """
    try:
        print("\n🌍 Fetching world countries data...")
        # Using REST Countries API for comprehensive country data
        response = requests.get("https://restcountries.com/v3.1/all", timeout=15)
        response.raise_for_status()

        countries_data = response.json()
        print(f"✅ Retrieved data for {len(countries_data)} countries")

        # Find top 5 largest countries by area
        print("\n📊 TOP 5 LARGEST COUNTRIES BY AREA")
        analyze_largest_countries_by_area(countries_data)

        # Analyze population data
        print("\n📊 POPULATION ANALYSIS")
        analyze_population_metrics(countries_data)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching country data: {e}")
    except Exception as e:
        print(f"❌ Error analyzing country data: {e}")


def analyze_largest_countries_by_area(countries_data: List[Dict[str, Any]]) -> None:
    """Find and display the largest countries by area.

    Args:
        countries_data (List[Dict]): List of country dictionaries
    """
    countries_with_area = []

    for country in countries_data:
        if "area" in country and country["area"] is not None:
            name = country.get("name", {}).get("common", "Unknown")
            area = country["area"]
            countries_with_area.append((name, area))

    # Sort by area (descending)
    countries_with_area.sort(key=lambda x: x[1], reverse=True)

    print("   Rank | Country        | Area (km²)")
    print("   -----|----------------|------------------")
    for i, (name, area) in enumerate(countries_with_area[:5], 1):
        print(f"   {i:2d}   | {name:14s} | {area:,.0f}")


def analyze_population_metrics(countries_data: List[Dict[str, Any]]) -> None:
    """Analyze global population statistics.

    Args:
        countries_data (List[Dict]): List of country dictionaries
    """
    populations = []

    for country in countries_data:
        if "population" in country and country["population"] is not None:
            populations.append(country["population"])

    if populations:
        total_population = sum(populations)
        print(f"   Total World Population: {total_population:,}")
        print(f"   Mean Population: {np.mean(populations):,.0f}")
        print(f"   Median Population: {np.median(populations):,.0f}")
        print(f"   Largest Population: {max(populations):,}")
        print(f"   Smallest Population: {min(populations):,}")
    else:
        print("   No population data available")


def demonstrate_web_scraping() -> None:
    """Demonstrate basic web scraping capabilities.

    Note: This is for educational purposes only. Always respect robots.txt
    and website terms of service when scraping.
    """
    if not BS4_AVAILABLE:
        print(
            "\n⚠️  BeautifulSoup4 not available. Install with: pip install beautifulsoup4"
        )
        return

    try:
        print("\n🕷️  Web Scraping Demonstration")
        print("   Note: This is for educational purposes only.")

        # Example: Scraping a simple, scraping-friendly site
        url = "https://httpbin.org/html"
        print(f"   Fetching content from: {url}")

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup( # type: ignore
            response.content, "html.parser"
        )
        title = soup.find("h1")

        if title:
            print(f"   Page title: {title.get_text()}")
        else:
            print("   No title found")

    except Exception as e:
        print(f"   ❌ Web scraping demo failed: {e}")


def main() -> None:
    """Main function to demonstrate package manager capabilities."""
    print("🚀 Day 20: Python Package Manager Demo")
    print("📦 Showcasing third-party libraries for business analytics\n")

    # Text analysis example
    gutenberg_text = fetch_gutenberg_text()
    if gutenberg_text:
        print("\n📝 TEXT ANALYSIS - Most Common Words:")
        common_words = analyze_text_frequency(gutenberg_text, 10)
        for i, (word, count) in enumerate(common_words, 1):
            print(f"   {i:2d}. {word}: {count} occurrences")

    # API analysis examples
    analyze_cat_breed_data()
    analyze_country_data()

    # Web scraping demonstration
    demonstrate_web_scraping()

    print("\n✅ Demo complete! You've seen how pip enables powerful data analysis.")
    print("💡 Tip: Explore more packages at pypi.org for your business needs!")


if __name__ == "__main__":
    main()
