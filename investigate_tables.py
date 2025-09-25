"""
Web Data Investigation Tool for Business Analytics

This script demonstrates how to programmatically extract and analyze
tabular data from web pages, a crucial skill for business analysts
who need to gather competitive intelligence, market data, or industry statistics.

Purpose: Educational tool for MBA students learning data acquisition
"""

import requests
import pandas as pd
from typing import List, Optional


def investigate_wiki_tables(url: str) -> Optional[List[pd.DataFrame]]:
    """
    Investigates and extracts tables from a Wikipedia page.

    This function is particularly useful for business research when you need
    to quickly extract structured data from Wikipedia pages containing
    financial information, company lists, or industry statistics.

    Args:
        url (str): The URL of the Wikipedia page to analyze

    Returns:
        Optional[List[pd.DataFrame]]: List of DataFrames containing the tables,
                                    or None if extraction fails

    Raises:
        requests.exceptions.RequestException: If the web request fails
        ValueError: If no tables are found on the page

    Example:
        >>> url = 'https://en.wikipedia.org/wiki/Fortune_500'
        >>> tables = investigate_wiki_tables(url)
        >>> if tables:
        ...     print(f"Found {len(tables)} tables with business data")
    """
    try:
        # Use a realistic user agent to avoid being blocked by websites
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        print(f"📊 Connecting to: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # Raises an exception for bad status codes

        # Extract all tables from the HTML content
        tables = pd.read_html(response.text)

        if not tables:
            raise ValueError("No tables found on the specified page")

        print(f"✅ Successfully found {len(tables)} table(s) on the page.")
        print("=" * 50)

        # Display preview of each table for analysis
        for i, table in enumerate(tables):
            print(f"📋 Table {i + 1} Preview:")
            print(f"   Shape: {table.shape[0]} rows × {table.shape[1]} columns")
            print(f"   Columns: {list(table.columns)}")
            print("   First 3 rows:")
            print(table.head(3))
            print("-" * 30)

        return tables

    except requests.exceptions.Timeout:
        print("⏰ Error: Request timed out. The website may be slow to respond.")
        return None
    except requests.exceptions.ConnectionError:
        print(
            "🌐 Error: Unable to connect to the website. Check your internet connection."
        )
        return None
    except requests.exceptions.RequestException as e:
        print(f"🔗 Error downloading the page: {e}")
        return None
    except ValueError as e:
        print(f"📋 Data extraction error: {e}")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None


def main() -> None:
    """
    Main function to demonstrate table investigation functionality.

    This example uses the List of US Presidents page, which contains
    structured data that's perfect for demonstrating web scraping
    techniques applicable to business data collection.
    """
    print("🚀 Wikipedia Table Investigation Tool")
    print("🎯 Perfect for business research and competitive analysis\n")

    # Example: Investigating presidential data (good structured table example)
    wiki_url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

    tables = investigate_wiki_tables(wiki_url)

    if tables:
        print(
            f"\n📈 Analysis complete! {len(tables)} table(s) ready for business analysis."
        )
        print(
            "💡 Tip: These DataFrames can now be used for further analysis with pandas."
        )
    else:
        print("\n❌ Investigation failed. Please check the URL and try again.")


if __name__ == "__main__":
    main()
