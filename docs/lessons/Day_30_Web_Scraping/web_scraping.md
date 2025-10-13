# 📘 Day 30: Web Scraping - Extracting Data from the Web

Sometimes, the data you need isn't available in a clean CSV file or through an API. It's simply displayed on a website. **Web scraping** is the process of automatically downloading the HTML code of a web page and extracting useful information from it.

This is an incredibly powerful tool for a business analyst, allowing you to gather competitive intelligence, track news sentiment, collect product prices, and much more.

## 📦 Working Offline

If you do not have internet access, you can still explore the examples in this lesson. The folder includes a curated `presidents.csv` containing a snapshot of key columns—number, name, party, term dates, and vice presidents—for every U.S. president through Joe Biden. The exercise scripts will look for this local file first, so you can experiment with parsing and analysis even when the Wikipedia page is unavailable. When a connection is available you can still re-run the scraper to refresh the dataset, which will regenerate `presidents.json`. Git ignores these generated JSON files so your repository stays clean.

**A VERY IMPORTANT NOTE ON ETHICS AND LEGALITY:**

- **Check `robots.txt`:** Always check a website's `robots.txt` file (e.g., `https://example.com/robots.txt`) to see which parts of the site you are allowed to scrape. Respect the rules.
- **Be Gentle:** Don't send too many requests in a short period. You could overwhelm the website's server, which is inconsiderate and may get your IP address blocked. Introduce delays between your requests.
- **Identify Yourself:** Set a user-agent in your request headers that identifies your script or bot.
- **Public Data Only:** Only scrape data that is publicly visible. Do not attempt to scrape information that is behind a login or a paywall.

## The Web Scraping Toolkit

We will use two main libraries for web scraping:

1. **`requests`**: A simple and elegant library for making HTTP requests to download web pages.
1. **`BeautifulSoup`**: A library for parsing HTML and XML documents. It creates a parse tree from the page's source code that you can use to extract data.

## The Scraping Process

1. **Inspect the Page:** Use your web browser's "Inspect" or "View Source" tool to understand the HTML structure of the page you want to scrape. Find the HTML tags (e.g., `<h1>`, `<p>`, `<table>`, `<div>`) that contain the data you need. Look for unique `id` or `class` attributes on those tags.
1. **Download the HTML:** Use the `requests.get(url)` function to download the page's HTML content.
1. **Create a "Soup":** Pass the downloaded HTML to the `BeautifulSoup` constructor to create a parsable object.
1. **Find Your Data:** Use BeautifulSoup's methods, like `find()` and `find_all()`, to locate the specific HTML tags containing your data.
1. **Extract the Text:** Once you have the tags, use the `.get_text()` method to extract the clean text from them.
1. **Structure the Data:** Organize your extracted data into a list or, even better, a Pandas DataFrame.

```python
import requests
from bs4 import BeautifulSoup

url = 'http://example.com' # A simple example page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first <h1> tag
header = soup.find('h1').get_text()

# Find all <p> (paragraph) tags
paragraphs = soup.find_all('p')
first_paragraph_text = paragraphs[0].get_text()
```

## 🔬 Profiling the Scraper

Profiling helps you spot whether networking or HTML parsing is the bottleneck. Two helper commands wire into the shared profiler:

```bash
python Day_30_Web_Scraping/profile_web_scraping.py --mode cprofile
python Day_30_Web_Scraping/profile_web_scraping.py --mode timeit --local-html Day_30_Web_Scraping/books_sample.html --repeat 5 --number 3
```

The `cProfile` output shows that almost all time is spent inside `requests.Session.get`—network I/O dominates the runtime, so batching requests or caching responses offers the biggest win.【ad83b3†L1-L29】 For deterministic timing, use the saved `books_sample.html` page (refresh it with `curl http://books.toscrape.com/ -o Day_30_Web_Scraping/books_sample.html`). Parsing that local file takes ~0.03 seconds per iteration across five repeats, letting you focus on BeautifulSoup performance without hitting the network.【de293a†L1-L7】 Reusing a single `requests.Session` and avoiding repeated downloads can dramatically cut the cost when scraping multiple pages.

## 💻 Exercises: Day 30

For these exercises, we will scrape the website `http://books.toscrape.com/`, a site specifically designed for scraping practice.

1. **Scrape Book Titles:**

   - Visit `http://books.toscrape.com/`.
   - Write a script that downloads the page content.
   - Create a BeautifulSoup object from the content.
   - Find all the book titles on the first page. (Hint: Inspect the page to see what tag the titles are in. They are inside `<h3>` tags, within an `<a>` tag).
   - Create a list of all the book titles and print it.

1. **Scrape Book Prices:**

   - On the same page, find all the book prices. (Hint: They are in `p` tags with the class `price_color`).
   - Extract the text of the prices (e.g., "£51.77").
   - Create a list of all the prices and print it.

1. **Create a DataFrame:**

   - Combine your work from the previous two exercises.
   - Create a script that scrapes both the titles and the prices.
   - Store the results in a Pandas DataFrame with two columns: "Title" and "Price".
   - Print the first 5 rows of your new DataFrame using `.head()`.

🎉 **Great job!** Web scraping is a powerful skill that opens up a vast new source of data for your analyses. While it can be complex, mastering the basics of `requests` and `BeautifulSoup` is a huge step forward.

Day 30: Web Scraping in Practice

This script demonstrates the fundamentals of web scraping by
extracting book titles and prices from a practice website.

This educational example shows how to:
- Make HTTP requests with proper headers
- Parse HTML content with BeautifulSoup
- Handle errors gracefully
- Extract and clean data
- Structure data in pandas DataFrame

Author: 50 Days of Python Course
Purpose: Educational example for MBA students

```python

import time
from typing import Any, Dict, Optional, Tuple

import bs4
import pandas as pd
import requests
from bs4 import BeautifulSoup

# The URL of the website we want to scrape
# This site is specifically designed for scraping practice.
URL = "http://books.toscrape.com/"


class ScrapingError(Exception):
    """Custom exception for scraping errors."""


def scrape_books(
    url: str, session: Optional[requests.Session] = None
) -> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, Any]]:
    """
    Scrape book data from the given URL.

    Args:
        url (str): The URL to scrape

    Returns:
        Tuple containing the raw scraped DataFrame, the cleaned DataFrame, and
        a dictionary of summary statistics.
    """
    # --- 1. Download the HTML Content ---
    # Use requests.get() to download the page.
    # It's good practice to include a 'User-Agent' header to identify your script.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    session = session or requests.Session()

    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise
    except requests.exceptions.ConnectionError:
        raise
    except requests.exceptions.HTTPError:
        raise
    except requests.exceptions.RequestException as exc:
        raise ScrapingError("Error downloading the page") from exc

    # If we get here, the request was successful
    return process_book_data(response.content)


def process_book_data(
    html_content: bytes,
) -> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, Any]]:
    """
    Process the HTML response and extract book data.

    Args:
        response: The HTTP response object

    Returns:
        Tuple containing the raw scraped DataFrame, the cleaned DataFrame, and
        a dictionary of summary statistics.
    """
    # --- 2. Create a BeautifulSoup Object ---
    # This object parses the HTML content and makes it searchable.
    soup = BeautifulSoup(html_content, "html.parser")

    # --- 3. Find and Extract Data ---
    # We inspected the page and found that book information is within <article> tags with the class 'product_pod'
    books = soup.find_all("article", class_="product_pod")

    if not books:
        raise ValueError("No books found in the provided HTML content")

    titles = []
    prices = []

    # Loop through each book found on the page
    for book in books:
        # Type check to ensure book is a Tag
        if not isinstance(book, bs4.element.Tag):
            continue

        # The title is in an 'a' tag within an 'h3' tag.
        # We access the 'title' attribute of the 'a' tag.
        h3_tag = book.find("h3")
        if isinstance(h3_tag, bs4.element.Tag):
            a_tag = h3_tag.find("a")
            if isinstance(a_tag, bs4.element.Tag):
                title = a_tag.get("title")
                titles.append(str(title) if title else "N/A")
            else:
                titles.append("N/A")
        else:
            titles.append("N/A")

        # The price is in a 'p' tag with the class 'price_color'
        price_tag = book.find("p", attrs={"class": "price_color"})
        if isinstance(price_tag, bs4.element.Tag):
            price_text = price_tag.get_text(strip=True)
            prices.append(price_text)
        else:
            prices.append("N/A")

    # --- 4. Structure the Data in a DataFrame ---
    if not titles or not prices or len(titles) != len(prices):
        raise ValueError("Mismatch between titles and prices in the HTML content")

    book_data = pd.DataFrame({"Title": titles, "Price": prices})

    # --- 5. Data Cleaning (Bonus) ---
    clean_data = book_data.copy()
    clean_data["Price_Float"] = pd.to_numeric(
        clean_data["Price"].str.replace("£", "", regex=False), errors="coerce"
    )
    clean_data = clean_data.dropna(subset=["Price_Float"]).copy()

    if clean_data.empty:
        return book_data, clean_data, {}

    # --- 6. Basic Analysis ---
    price_series = clean_data["Price_Float"]
    analysis: Dict[str, Any] = {
        "average_price": float(price_series.mean()),
        "min_price": float(price_series.min()),
        "max_price": float(price_series.max()),
        "count": int(len(clean_data)),
    }

    most_expensive = clean_data.loc[price_series.idxmax()]
    cheapest = clean_data.loc[price_series.idxmin()]

    analysis["most_expensive_title"] = most_expensive["Title"]
    analysis["most_expensive_price"] = most_expensive["Price"]
    analysis["cheapest_title"] = cheapest["Title"]
    analysis["cheapest_price"] = cheapest["Price"]

    return book_data, clean_data, analysis


def main():
    """
    Main function to demonstrate web scraping workflow.
    """
    print("🕸️  Day 30: Web Scraping Demonstration")
    print("📚 Scraping book data from books.toscrape.com")
    print("=" * 50)

    # Add a small delay to be respectful to the server
    print("⏳ Starting scraping process...")
    time.sleep(1)

    # Execute the scraping
    try:
        print(f"🌐 Connecting to {URL}...")
        raw_df, clean_df, analysis = scrape_books(URL)
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server might be slow or unresponsive.")
        return
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
        return
    except requests.exceptions.HTTPError as exc:
        print(f"❌ HTTP error occurred: {exc}")
        return
    except ScrapingError as exc:
        print(f"❌ {exc}")
        print("💡 This could be due to:")
        print("   • Network connectivity issues")
        print("   • Website being temporarily unavailable")
        print("   • Blocked by website's anti-bot protection")
        print("   • URL has changed or is incorrect")
        return
    except ValueError as exc:
        print(f"❌ {exc}")
        print("💡 The website structure may have changed. Try updating the parser.")
        return

    print("✅ Successfully downloaded the content!")
    print(f"📊 Total books scraped: {len(raw_df)}")

    if clean_df.empty:
        print("⚠️  No valid price data found for analysis.")
        return

    print("\n--- Sample of Scraped Book Data ---")
    print(raw_df.head(10))

    print("\n--- Cleaned Price Data ---")
    print(clean_df.head(10))

    print("\n📈 Basic Price Analysis:")
    print(f"   Average price: £{analysis['average_price']:.2f}")
    print(f"   Minimum price: £{analysis['min_price']:.2f}")
    print(f"   Maximum price: £{analysis['max_price']:.2f}")
    print(f"   Number of books: {analysis['count']}")
    print(
        f"💰 Most expensive: '{analysis['most_expensive_title']}' - {analysis['most_expensive_price']}"
    )
    print(f"💸 Cheapest: '{analysis['cheapest_title']}' - {analysis['cheapest_price']}")

    print("\n💡 Next steps you could take:")
    print("   • Save data to CSV: clean_df.to_csv('books.csv', index=False)")
    print("   • Filter books by price range")
    print("   • Scrape additional pages for more data")
    print("   • Add more data fields (ratings, availability, etc.)")


if __name__ == "__main__":
    main()

```
