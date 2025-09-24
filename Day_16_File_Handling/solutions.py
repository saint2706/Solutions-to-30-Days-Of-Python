# Day 16: File Handling - Solutions

import json
import re

## Exercise 1: Word and Line Count

# First, create the file 'my_story.txt' with some content.
# For example:
#
# This is a story about a brave knight.
# The knight fought a dragon to save the princess.
# They all lived happily ever after.

def count_words_and_lines(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            print(f"The file '{filename}' has {num_lines} lines and {num_words} words.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# To run this solution, make sure you have a file named 'my_story.txt' in the same directory.
# count_words_and_lines('my_story.txt')


## Exercise 2: JSON Data Processing

def top_5_populated_countries(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            countries_data = json.load(f)

        # Sort the countries by population in descending order
        sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

        print("Top 5 most populated countries:")
        for i in range(5):
            country = sorted_countries[i]
            print(f"{i+1}. {country['name']}: {country['population']:,}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode the JSON file '{filename}'.")

# To run this solution, you need the 'countries_data.json' file in the 'data' directory.
# Assuming the 'data' directory is in the parent directory.
# top_5_populated_countries('../data/countries_data.json')


## Exercise 3: Email Extraction

def extract_unique_emails(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
            # A simple regex to find email addresses
            emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
            unique_emails = set(emails)
            print(f"Found {len(unique_emails)} unique email addresses:")
            for email in unique_emails:
                print(email)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# To run this solution, you need the 'email_exchanges.txt' file in the 'data' directory.
# extract_unique_emails('../data/email_exchanges.txt')
