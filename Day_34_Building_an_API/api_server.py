"""
Day 34: Building a Simple API with Flask

This script creates a simple web API that serves sample
business data in JSON format.
"""

from flask import Flask, jsonify

# 1. Create an instance of the Flask class
# '__name__' is a special Python variable that gets the name of the current module.
app = Flask(__name__)


# --- Sample Data ---
# In a real application, this data would come from a database.
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 25, "category": "Peripherals"},
    {"id": 3, "name": "Keyboard", "price": 75, "category": "Peripherals"},
]

EMPLOYEES = [
    {"id": 101, "name": "Alice", "department": "Sales"},
    {"id": 102, "name": "Bob", "department": "Engineering"},
]


# --- API Routes ---


# 2. Define a "route" for the home/root URL
# This is the function that runs when someone visits the main page.
@app.route("/")
def home():
    return "<h1>Welcome to the Company Data API</h1><p>Use endpoints like /api/products to get data.</p>"


# Route to get all products
@app.route("/api/v1/products", methods=["GET"])
def get_all_products():
    """Returns the full list of products as JSON."""
    return jsonify(PRODUCTS)


# Route to get a single product by its ID
# The <int:product_id> part is a dynamic variable in the URL.
@app.route("/api/v1/products/<int:product_id>", methods=["GET"])
def get_single_product(product_id):
    """Returns a single product matching the given ID."""
    # Use a generator expression to find the product. Returns None if not found.
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)

    if product:
        return jsonify(product)
    else:
        # Return a standard 404 Not Found error if the ID doesn't exist
        return jsonify({"error": "Product not found"}), 404


# Route to get all employees
@app.route("/api/v1/employees", methods=["GET"])
def get_all_employees():
    """Returns the full list of employees as JSON."""
    return jsonify(EMPLOYEES)


# 3. Run the app
# The __name__ == '__main__' block ensures this code only runs when
# you execute this script directly. It won't run if the script is imported
# as a module into another script.
if __name__ == "__main__":
    # debug=True will auto-reload the server when you make changes.
    # In a production environment, you would use a proper web server (like Gunicorn).
    # Host '0.0.0.0' makes it accessible from other devices on the network.
    app.run(host="0.0.0.0", port=5000, debug=True)
