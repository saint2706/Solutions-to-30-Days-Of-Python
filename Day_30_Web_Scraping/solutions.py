"""
Day 22: Solutions to Exercises
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://books.toscrape.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Successfully connected to books.toscrape.com")
except requests.exceptions.RequestException as e:
    print(f"Could not connect to the website: {e}")
    soup = None

if soup:
    # --- Exercise 1: Scrape Book Titles ---
    print("\n--- Solution to Exercise 1 ---")

    # Find all <h3> tags, then find the <a> tag inside, and get its 'title' attribute
    title_tags = soup.find_all('h3')
    titles = [tag.find('a')['title'] for tag in title_tags]

    print("Found the following titles:")
    # Print first 5 for brevity
    for title in titles[:5]:
        print(f"- {title}")
    print("-" * 20)


    # --- Exercise 2: Scrape Book Prices ---
    print("\n--- Solution to Exercise 2 ---")

    # Find all <p> tags that have the class 'price_color'
    price_tags = soup.find_all('p', class_='price_color')
    prices = [tag.get_text() for tag in price_tags]

    print("Found the following prices:")
    # Print first 5 for brevity
    for price in prices[:5]:
        print(f"- {price}")
    print("-" * 20)


    # --- Exercise 3: Create a DataFrame ---
    print("\n--- Solution to Exercise 3 ---")

    # Check if we have the same number of titles and prices
    if len(titles) == len(prices):
        book_df = pd.DataFrame({
            'Title': titles,
            'Price': prices
        })
        print("Created DataFrame from scraped data:")
        print(book_df.head())
    else:
        print("Mismatch between number of titles and prices found. Cannot create DataFrame.")
    print("-" * 20)

else:
    print("\nSkipping exercises as the website could not be scraped.")
