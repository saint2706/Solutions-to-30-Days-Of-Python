"""
Day 30: Web Scraping in Practice

This script demonstrates the fundamentals of web scraping by
extracting book titles and prices from a practice website.

This educational example shows how to:
- Make HTTP requests with proper headers
- Parse HTML content with BeautifulSoup
- Handle errors gracefully
- Extract and clean data
- Structure data in pandas DataFrame

Author: 30 Days of Python Course
Purpose: Educational example for MBA students
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import bs4
from typing import List, Optional, Dict, Any
import time

# The URL of the website we want to scrape
# This site is specifically designed for scraping practice.
URL = "http://books.toscrape.com/"


def scrape_books(url: str) -> Optional[pd.DataFrame]:
    """
    Scrape book data from the given URL.

    Args:
        url (str): The URL to scrape

    Returns:
        Optional[pd.DataFrame]: DataFrame with book data or None if scraping fails
    """
    # --- 1. Download the HTML Content ---
    # Use requests.get() to download the page.
    # It's good practice to include a 'User-Agent' header to identify your script.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        print(f"🌐 Connecting to {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        # Raise an exception if the request was unsuccessful (e.g., 404 Not Found)
        response.raise_for_status()
        print(f"✅ Successfully downloaded the content from {url}")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server might be slow or unresponsive.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading the page: {e}")
        return None

    # If we get here, the request was successful
    return process_book_data(response)


def process_book_data(response: requests.Response) -> Optional[pd.DataFrame]:
    """
    Process the HTML response and extract book data.

    Args:
        response: The HTTP response object

    Returns:
        Optional[pd.DataFrame]: Processed book data or None if processing fails
    """
    try:
        # --- 2. Create a BeautifulSoup Object ---
        # This object parses the HTML content and makes it searchable.
        soup = BeautifulSoup(response.content, "html.parser")

        # --- 3. Find and Extract Data ---
        # We inspected the page and found that book information is within <article> tags with the class 'product_pod'
        books = soup.find_all("article", class_="product_pod")

        if not books:
            print(
                "❌ No books found on the page. The website structure may have changed."
            )
            return None

        titles = []
        prices = []

        # Loop through each book found on the page
        for book in books:
            # Type check to ensure book is a Tag
            if not isinstance(book, bs4.element.Tag):
                continue

            try:
                # The title is in an 'a' tag within an 'h3' tag.
                # We access the 'title' attribute of the 'a' tag.
                h3_tag = book.find("h3")
                if isinstance(h3_tag, bs4.element.Tag):
                    a_tag = h3_tag.find("a")
                    if isinstance(a_tag, bs4.element.Tag):
                        title = a_tag.get("title")
                        if title:
                            titles.append(str(title))
                        else:
                            titles.append("N/A")
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

            except Exception as e:
                print(f"⚠️  Error processing book: {e}")
                titles.append("Error")
                prices.append("Error")
                continue

        # --- 4. Structure the Data in a DataFrame ---
        if titles and prices and len(titles) == len(prices):
            book_data = pd.DataFrame({"Title": titles, "Price": prices})

            print(f"\n📊 Successfully scraped {len(book_data)} books")
            print("\n--- Scraped Book Data ---")
            print(book_data.head(10))

            # --- 5. Data Cleaning (Bonus) ---
            # The price is scraped as a string with '£'. Let's clean it.
            try:
                # Filter out error entries before processing
                clean_data = book_data[book_data["Price"] != "Error"].copy()

                if not clean_data.empty:
                    clean_data["Price_Float"] = (
                        clean_data["Price"]
                        .str.replace("£", "", regex=False)
                        .astype(float)
                    )

                    print("\n--- DataFrame After Cleaning Price ---")
                    print(clean_data.head(10))

                    # --- 6. Basic Analysis ---
                    print("\n📈 Basic Price Analysis:")
                    print(f"   Average price: £{clean_data['Price_Float'].mean():.2f}")
                    print(f"   Minimum price: £{clean_data['Price_Float'].min():.2f}")
                    print(f"   Maximum price: £{clean_data['Price_Float'].max():.2f}")
                    print(f"   Number of books: {len(clean_data)}")

                    # Find most expensive and cheapest books
                    most_expensive = clean_data.loc[clean_data["Price_Float"].idxmax()]
                    cheapest = clean_data.loc[clean_data["Price_Float"].idxmin()]

                    print(
                        f"\n💰 Most expensive: '{most_expensive['Title']}' - {most_expensive['Price']}"
                    )
                    print(f"💸 Cheapest: '{cheapest['Title']}' - {cheapest['Price']}")

                    return clean_data
                else:
                    print("⚠️  No valid price data found for analysis")
                    return book_data

            except Exception as e:
                print(f"❌ Error during data cleaning: {e}")
                print("Raw data will be displayed without price analysis")
                return book_data

        elif not titles or not prices:
            print(
                "❌ Could not find book titles or prices. The website structure may have changed."
            )
            return None
        else:
            print(f"❌ Data mismatch: {len(titles)} titles vs {len(prices)} prices")
            return None

    except Exception as e:
        print(f"❌ Error processing book data: {e}")
        return None


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
    book_df = scrape_books(URL)

    if book_df is not None:
        print("\n🎉 Web scraping completed successfully!")
        print(f"📊 Total books scraped: {len(book_df)}")
        print("\n💡 Next steps you could take:")
        print("   • Save data to CSV: book_df.to_csv('books.csv')")
        print("   • Filter books by price range")
        print("   • Scrape additional pages for more data")
        print("   • Add more data fields (ratings, availability, etc.)")
    else:
        print("\n❌ Web scraping failed. Please check the error messages above.")
        print("💡 This could be due to:")
        print("   • Network connectivity issues")
        print("   • Website being temporarily unavailable")
        print("   • Blocked by website's anti-bot protection")
        print("   • URL has changed or is incorrect")


if __name__ == "__main__":
    main()
