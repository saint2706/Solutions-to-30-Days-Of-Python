"""
Day 30: Web Scraping Presidents Data

This script scrapes data about the presidents of the United States from Wikipedia,
processes it using pandas, and saves it as a JSON file.
"""

import requests
import pandas as pd
import csv
import json
import os

def scrape_presidents_data(url: str) -> pd.DataFrame:
    """
    Scrapes the list of US presidents from a Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        pd.DataFrame: A DataFrame containing the presidents' data.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        # The pd.read_html function returns a list of all tables on the page
        tables = pd.read_html(response.content)
        # The first table is the one we want
        presidents_df = tables[0].copy()
        # Drop the last row which is a footnote
        presidents_df = presidents_df.iloc[:-1].copy()
        # Replace empty strings with NaN
        presidents_df.replace("", float("NaN"), inplace=True)
        # Drop columns that are all NaN
        presidents_df.dropna(how='all', axis=1, inplace=True)
        return presidents_df
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the page: {e}")
        return None
    except (IndexError, KeyError) as e:
        print(f"Error parsing the table: {e}")
        return None

def convert_csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    """
    Converts a CSV file to a JSON file.

    The JSON file will have the first column of the CSV as keys.

    Args:
        csv_file_path (str): The path to the input CSV file.
        json_file_path (str): The path to the output JSON file.
    """
    data = {}
    try:
        with open(csv_file_path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Get the name of the first column to use as a key
            key_column = csv_reader.fieldnames[0]
            for row in csv_reader:
                key = row[key_column]
                data[key] = row

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def main():
    """
    Main function to scrape, process, and save the presidents' data.
    """
    # URL of the Wikipedia page with the list of US presidents
    presidents_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

    # Define file paths relative to the script's location
    # This makes the script more portable
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'presidents.csv')
    json_path = os.path.join(base_dir, 'presidents.json')

    # Scrape the data
    presidents_df = scrape_presidents_data(presidents_url)

    if presidents_df is not None:
        # Save the DataFrame to a temporary CSV file, without the index
        presidents_df.to_csv(csv_path, index=False)

        # Convert the CSV to JSON
        convert_csv_to_json(csv_path, json_path)

        # Remove the temporary CSV file
        try:
            os.remove(csv_path)
            print(f"Successfully created '{json_path}' and removed temporary CSV.")
        except OSError as e:
            print(f"Error removing temporary file {csv_path}: {e}")

if __name__ == '__main__':
    main()
