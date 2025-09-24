"""
Day 30: Web Scraping Presidents Data

This script scrapes data about the presidents of the United States from Wikipedia,
processes it using pandas, and saves it as a JSON file.
"""

from typing import Optional
import requests
import pandas as pd
import csv
import json
import os


def scrape_presidents_data(url: str) -> Optional[pd.DataFrame]:
    """
    Scrapes the list of US presidents from a Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        pd.DataFrame: A DataFrame containing the presidents' data.
    """
    try:
        print(f"🌐 Connecting to {url}...")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        print("📊 Parsing HTML tables...")
        # Use response.text instead of response.content for pd.read_html
        tables = pd.read_html(response.text)

        if not tables:
            print("❌ No tables found on the page")
            return None

        print(f"✅ Found {len(tables)} tables on the page")

        # The first table is typically the one we want
        presidents_df = tables[0].copy()

        print(f"📋 Original data shape: {presidents_df.shape}")

        # Clean up the data
        # Drop the last row if it appears to be a footnote (common in Wikipedia tables)
        if len(presidents_df) > 1:
            presidents_df = presidents_df.iloc[:-1].copy()

        # Replace empty strings with NaN
        presidents_df.replace("", float("NaN"), inplace=True)
        presidents_df.replace(
            "—", float("NaN"), inplace=True
        )  # Common dash used in Wikipedia

        # Drop columns that are all NaN
        presidents_df.dropna(how="all", axis=1, inplace=True)

        print(f"📋 Cleaned data shape: {presidents_df.shape}")
        print(f"📋 Columns: {list(presidents_df.columns)}")

        return presidents_df
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server might be slow.")
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
    except (IndexError, KeyError) as e:
        print(f"❌ Error parsing the table: {e}")
        print("💡 The website structure may have changed.")
        return None
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")
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
        print(f"📄 Converting {csv_file_path} to {json_file_path}...")
        with open(csv_file_path, encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Check if fieldnames exist and get the first column
            if not csv_reader.fieldnames:
                print("❌ No column headers found in CSV file")
                return

            key_column = csv_reader.fieldnames[0]
            print(f"📊 Using '{key_column}' as the key column")

            row_count = 0
            for row in csv_reader:
                key = row[key_column]
                if key:  # Only add rows with non-empty keys
                    data[key] = row
                    row_count += 1

            print(f"✅ Processed {row_count} records")

        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"✅ Successfully converted to JSON: {json_file_path}")
    except FileNotFoundError:
        print(f"❌ Error: The file {csv_file_path} was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing files.")
    except Exception as e:
        print(f"❌ An error occurred during conversion: {e}")


def main():
    """
    Main function to scrape, process, and save the presidents' data.
    """
    print("🕸️  Day 30: Web Scraping Presidents Data")
    print("🏛️  Scraping US Presidents data from Wikipedia")
    print("=" * 50)

    # URL of the Wikipedia page with the list of US presidents
    presidents_url = (
        "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    )

    # Define file paths relative to the script's location
    # This makes the script more portable
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "presidents.csv")
    json_path = os.path.join(base_dir, "presidents.json")

    print(f"📁 Output files will be saved to: {base_dir}")

    # Scrape the data
    presidents_df = scrape_presidents_data(presidents_url)

    if presidents_df is not None:
        try:
            # Save the DataFrame to a temporary CSV file, without the index
            print("💾 Saving data to CSV...")
            presidents_df.to_csv(csv_path, index=False, encoding="utf-8")
            print(f"✅ CSV file created: {csv_path}")

            # Convert the CSV to JSON
            convert_csv_to_json(csv_path, json_path)

            # Remove the temporary CSV file
            try:
                os.remove(csv_path)
                print(f"🧹 Removed temporary CSV file")
            except OSError as e:
                print(f"⚠️  Warning: Could not remove temporary file {csv_path}: {e}")

            # Verify the JSON file was created and show some info
            if os.path.exists(json_path):
                file_size = os.path.getsize(json_path)
                print(f"\n🎉 Success! Created '{json_path}' ({file_size:,} bytes)")

                # Show a preview of the data
                try:
                    with open(json_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        print(f"📊 Total presidents in dataset: {len(data)}")
                        if data:
                            first_key = next(iter(data))
                            print(
                                f"📋 Sample entry keys: {list(data[first_key].keys())[:5]}..."
                            )
                except Exception as e:
                    print(f"⚠️  Could not preview JSON data: {e}")
            else:
                print(f"❌ JSON file was not created successfully")

        except Exception as e:
            print(f"❌ Error in main processing: {e}")
    else:
        print("❌ Failed to scrape presidents data.")
        print("💡 This could be due to:")
        print("   • Network connectivity issues")
        print("   • Wikipedia page structure changes")
        print("   • Server blocking the request")
        print("   • Temporary website unavailability")


if __name__ == "__main__":
    main()
