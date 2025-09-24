# 📘 Day 29: Building a Simple API with Flask

Consuming data from APIs is a core skill. But what if you need to provide data from your analysis to another person or application? Instead of sending a CSV file, you can build your own API. This allows other services (like a web dashboard or another analyst's script) to access your data programmatically.

Today, we'll learn how to build a simple web API using **Flask**, a popular "micro-framework" for Python. It's called a micro-framework because it's very lightweight and simple to start with, but can be extended to build complex applications.

## What is a Web Framework?

A web framework like Flask handles all the low-level, complicated parts of web communication (like handling HTTP requests and responses), so you can focus on writing your application's logic.

## Your First Flask API

A Flask application can be incredibly simple. Here is a basic "Hello, World" example:

```python
from flask import Flask

# 1. Create an instance of the Flask class
app = Flask(__name__)

# 2. Define a "route"
# This tells Flask: "When someone visits the main URL ('/'), run this function."
@app.route('/')
def home():
    return "Welcome to our API!"

# 3. Run the app
# The __name__ == '__main__' block ensures this code only runs when you execute the script directly.
if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for auto-reloading on code changes
```

## Returning JSON Data

An API for data analysis isn't very useful if it just returns text. We need to return structured data, and the standard format for that is JSON. Flask provides a handy function called `jsonify` that converts a Python dictionary into a proper JSON response.

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (in a real app, this might come from a database or a Pandas DataFrame)
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1200},
    {'id': 2, 'name': 'Mouse', 'price': 25}
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)
```

Now, if you run this app and navigate to `http://127.0.0.1:5000/api/products` in your browser or an API tool, you'll get the list of products in JSON format.

## Dynamic Routes

You can create routes that accept parameters. For example, to get a single product by its ID.

```python
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Find the product with the matching ID
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        # Return a 404 Not Found error if the product doesn't exist
        return jsonify({"error": "Product not found"}), 404
```

Now you can go to `/api/products/1` to get the laptop, or `/api/products/2` to get the mouse.

## 💻 Exercises: Day 29

1. **Create a Basic API Server:**
    * Create a file named `my_api.py`.
    * Set up a basic Flask application.
    * Create a root endpoint `/` that returns a simple welcome message like "Welcome to the Company Data API".

2. **Serve Employee Data:**
    * Inside your `my_api.py` script, create a list of employee dictionaries. Each employee should have an `id`, `name`, and `department`.
    * Create a new endpoint at `/api/employees`.
    * When a `GET` request is made to this endpoint, it should return the full list of employees as a JSON response.

3. **Serve a Single Employee's Data:**
    * Create a dynamic route `/api/employees/<int:employee_id>`.
    * This endpoint should find the employee with the matching ID from your list.
    * If the employee is found, return their data as a JSON object.
    * If no employee with that ID is found, return a JSON error message with a 404 status code.

🎉 **Incredible!** You've just learned how to build a web API. This is a massive step. It bridges the gap between performing analysis for yourself and providing data and services to others, forming the backbone of modern data applications and microservices.
