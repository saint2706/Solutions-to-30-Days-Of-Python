import requests
import pandas as pd

def investigate_wiki_tables(url: str):
    """
    Investigates the tables on a Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        tables = pd.read_html(response.content)

        print(f"Found {len(tables)} tables on the page.")

        for i, table in enumerate(tables):
            print(f"--- Table {i} ---")
            print(table.head())
            print("\n")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
    investigate_wiki_tables(wiki_url)
