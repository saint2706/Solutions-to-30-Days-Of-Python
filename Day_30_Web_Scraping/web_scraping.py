"""
Day 22: Web Scraping in Practice

This script demonstrates the fundamentals of web scraping by
extracting book titles and prices from a practice website.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# The URL of the website we want to scrape
# This site is specifically designed for scraping practice.
URL = "http://books.toscrape.com/"

# --- 1. Download the HTML Content ---
# Use requests.get() to download the page.
# It's good practice to include a 'User-Agent' header to identify your script.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
try:
    response = requests.get(URL, headers=headers)
    # Raise an exception if the request was unsuccessful (e.g., 404 Not Found)
    response.raise_for_status()
    print(f"Successfully downloaded the content from {URL}")
except requests.exceptions.RequestException as e:
    print(f"Error downloading the page: {e}")
    response = None


if response:
    # --- 2. Create a BeautifulSoup Object ---
    # This object parses the HTML content and makes it searchable.
    soup = BeautifulSoup(response.content, 'html.parser')

    # --- 3. Find and Extract Data ---
    # We inspected the page and found that book information is within <article> tags with the class 'product_pod'
    books = soup.find_all('article', class_='product_pod')

    titles = []
    prices = []

    # Loop through each book found on the page
    for book in books:
        # The title is in an 'a' tag within an 'h3' tag.
        # We access the 'title' attribute of the 'a' tag.
        title = book.find('h3').find('a')['title']
        titles.append(title)

        # The price is in a 'p' tag with the class 'price_color'
        price = book.find('p', class_='price_color').get_text()
        prices.append(price)

    # --- 4. Structure the Data in a DataFrame ---
    if titles and prices:
        book_data = pd.DataFrame({
            'Title': titles,
            'Price': prices
        })

        print("\n--- Scraped Book Data ---")
        print(book_data.head())

        # --- 5. Data Cleaning (Bonus) ---
        # The price is scraped as a string with '£'. Let's clean it.
        book_data['Price_Float'] = book_data['Price'].str.replace('£', '').astype(float)

        print("\n--- DataFrame After Cleaning Price ---")
        print(book_data.head())

    else:
        print("Could not find book titles or prices. The website structure may have changed.")
else:
    print("Skipping scraping as the webpage could not be downloaded.")
