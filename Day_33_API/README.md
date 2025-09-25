# 📘 Day 33: APIs - Accessing Live Data from the Web

So far, we've worked with data from static files (CSVs) and databases. But what if you need live, up-to-the-minute data? Or what if you need to programmatically interact with another software service, like a CRM or a social media platform? For this, we use **APIs (Application Programming Interfaces)**.

## What is an API?

An API is a set of rules and protocols that allows one software application to talk to another. It's like a contract that says, "If you send me a request in this specific format, I will send you back data in this specific format."

For a business analyst, APIs are a gateway to a vast world of live data:

* Financial APIs provide real-time stock prices.
* Weather APIs provide current forecasts.
* Social media APIs provide data on trends and user posts.
* Your company's own internal services (like a CRM or ERP) likely have APIs that allow you to access customer and product data programmatically.

## REST APIs and JSON

The most common type of web API is a **REST API**. The key concept is that you make a request to a specific URL, called an **endpoint**, and the API sends back data.

The most common data format for API responses is **JSON (JavaScript Object Notation)**. JSON is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.

The great news is that JSON's structure maps almost perfectly to Python dictionaries and lists!

## Making API Requests with the `requests` Library

The `requests` library is the standard way to make HTTP requests in Python. The most common type of request is a `GET` request, which is used to retrieve data.

```python
import requests
import pandas as pd

# The URL of the API endpoint we want to get data from
# JSONPlaceholder is a free fake API for testing and prototyping.
url = 'https://jsonplaceholder.typicode.com/users'

try:
    # Make the GET request
    response = requests.get(url)
    response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)

    # The .json() method parses the JSON response into a Python list of dictionaries
    users_data = response.json()

    # Now we can load this directly into a Pandas DataFrame!
    users_df = pd.DataFrame(users_data)

    print(users_df.head())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
```

## Working with API Parameters

Sometimes, you need to provide parameters to the API to specify what data you want. For example, you might want to get data for a specific user or product. These are usually passed as **query parameters** in the URL.

The `requests` library lets you provide these as a dictionary.

```python
# Get data for a specific user (userId = 1)
base_url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}

response = requests.get(base_url, params=params)
posts_user1 = response.json()
```

This is equivalent to requesting the URL `https://jsonplaceholder.typicode.com/posts?userId=1`.

## 💻 Exercises: Day 33

For these exercises, we will use the free and public [**{JSON} Placeholder API**](https://jsonplaceholder.typicode.com/).

1. **Fetch All Posts:**
    * The endpoint to get all posts is `https://jsonplaceholder.typicode.com/posts`.
    * Write a script that makes a `GET` request to this endpoint.
    * Load the JSON response into a Pandas DataFrame.
    * Print the first 5 rows of the DataFrame.

2. **Fetch a Specific User's Data:**
    * The endpoint to get data for a single user is `https://jsonplaceholder.typicode.com/users/USER_ID`, where `USER_ID` is a number from 1 to 10.
    * Write a script that fetches the data for user with ID `5`.
    * The response will be a single dictionary. Print the user's `name` and `company` name.

3. **Fetch Comments for a Specific Post:**
    * The API allows you to fetch comments for a specific post. The endpoint is `https://jsonplaceholder.typicode.com/comments`.
    * Use the `params` argument in your `requests.get()` call to filter for comments where the `postId` is `3`.
    * Load the resulting list of comment dictionaries into a Pandas DataFrame.
    * Print the head of the DataFrame.

🎉 **Excellent!** Being able to work with APIs is a crucial skill. It unlocks the ability to enrich your analyses with live, external data and allows you to integrate your Python scripts with other critical business systems.
