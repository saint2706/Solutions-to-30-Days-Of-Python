# Day 20: Python Package Manager (pip) - Solutions

import requests
import json

## Exercise 1: Install a package

# To install pandas, open your terminal or command prompt and run:
# pip install pandas

# To verify the installation, run:
# pip show pandas


## Exercise 2: Explore a package

# The documentation for the requests library can be found at:
# https://requests.readthedocs.io/en/latest/
#
# The get() function is used to send a GET request to a specified URL.
# It returns a Response object, which contains the server's response to the request.


## Exercise 3: Analyze country data

def top_5_largest_countries_by_area():
    try:
        url = 'https://restcountries.com/v2/all'
        response = requests.get(url)
        response.raise_for_status()
        countries = response.json()

        # Filter out countries that don't have an 'area' key
        countries_with_area = [c for c in countries if 'area' in c and c['area'] is not None]

        # Sort the countries by area in descending order
        sorted_countries = sorted(countries_with_area, key=lambda x: x['area'], reverse=True)

        print("Top 5 largest countries by area:")
        for i in range(5):
            country = sorted_countries[i]
            print(f"{i+1}. {country['name']}: {country['area']:,} sq. km")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error: Could not decode the JSON response.")

top_5_largest_countries_by_area()
