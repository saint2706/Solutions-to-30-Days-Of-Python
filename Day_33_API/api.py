"""
Day 33: Accessing Live Data with APIs

This script demonstrates how to make GET requests to a public
REST API to retrieve data and load it into Pandas.
"""

import requests
import pandas as pd

# --- 1. Making a Basic GET Request ---
print("--- 1. Fetching a list of users ---")
# The endpoint for a list of users
users_url = "https://jsonplaceholder.typicode.com/users"

try:
    # Make the request
    response = requests.get(users_url)
    # This line will raise an HTTPError if the HTTP request returned an unsuccessful status code
    response.raise_for_status()

    # Parse the JSON response into a Python list of dictionaries
    users_data = response.json()

    # Load the data into a Pandas DataFrame
    users_df = pd.DataFrame(users_data)

    print("Successfully fetched user data. First 5 rows:")
    print(users_df.head())

except requests.exceptions.RequestException as e:
    print(f"Failed to fetch data: {e}")
print("-" * 20)


# --- 2. Making a Request for a Specific Resource ---
print("--- 2. Fetching a single post (ID = 1) ---")
# The endpoint for a single post
post_url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(post_url)
    response.raise_for_status()

    # The response for a single item is usually a single dictionary
    post_data = response.json()

    print("Successfully fetched post data:")
    print(f"  User ID: {post_data['userId']}")
    print(f"  Title: {post_data['title']}")

except requests.exceptions.RequestException as e:
    print(f"Failed to fetch data: {e}")
print("-" * 20)


# --- 3. Making a Request with Parameters ---
print("--- 3. Fetching all posts by a specific user (userId = 2) ---")
# The base endpoint for posts
all_posts_url = "https://jsonplaceholder.typicode.com/posts"

# A dictionary of query parameters to filter the results
# This will be converted to ?userId=2 in the URL
params = {"userId": 2}

try:
    response = requests.get(all_posts_url, params=params)
    response.raise_for_status()

    user_2_posts_data = response.json()
    user_2_posts_df = pd.DataFrame(user_2_posts_data)

    print(f"Found {len(user_2_posts_df)} posts for userId=2. First 5 rows:")
    print(user_2_posts_df.head())

except requests.exceptions.RequestException as e:
    print(f"Failed to fetch data: {e}")
print("-" * 20)
