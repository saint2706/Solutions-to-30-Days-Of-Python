# 🌐 Day 35: Flask Web Framework

## Welcome to Day 35!

Today, we're going to learn about **Flask**, a lightweight and popular web framework for Python. A web framework provides a set of tools and libraries to help you build web applications more easily.

## Why is Flask Important for Business Analytics?

While you might not be building full-fledged web applications as a business analyst, understanding the basics of web frameworks like Flask can be very useful for:
- **Creating interactive dashboards**: You can use Flask to build simple web-based dashboards to display your analysis and visualizations.
- **Building APIs**: You can create APIs (Application Programming Interfaces) to serve your data and models to other applications.
- **Prototyping ideas**: Flask is great for quickly building prototypes of data-driven products and services.

## Key Concepts in Flask

- **Routes**: A route is a URL that your application will respond to. You define routes using the `@app.route()` decorator.
- **View functions**: A view function is a Python function that is executed when a user visits a specific route. It returns the content that will be displayed in the user's browser.
- **Templates**: Templates are HTML files that can be used to render dynamic content. Flask uses the Jinja2 templating engine.

## Exploring `app.py`

The `app.py` script in this folder contains a simple Flask application that demonstrates the basic concepts of Flask.

### How to Run the Application

1.  **Install Flask**: If you haven't already, install Flask using pip:
    ```bash
    pip install Flask
    ```

2.  **Run the application**: Open your terminal, navigate to this directory, and run the following command:
    ```bash
    python app.py
    ```

3.  **Open your browser**: Open your web browser and go to `http://127.0.0.1:5000/`. You should see the home page of the application.

## 💻 Exercises: Day 35

1.  **Create a new route**:
    *   Add a new route to the `app.py` script at the URL `/about`.
    *   Create a view function that returns a simple string, like "This is the about page."

2.  **Create a new template**:
    *   Create a new HTML file named `contact.html` in the `templates` directory.
    *   Add a new route to the `app.py` script at the URL `/contact` that renders the `contact.html` template.

3.  **Pass data to a template**:
    *   Modify the `/about` route to pass your name to a new `about.html` template.
    *   In the `about.html` template, display the name that was passed from the view function.

### Solutions

You can find the solutions to these exercises in the `solutions.py` file in this directory.

🎉 **Congratulations!** You've learned the basics of Flask, a powerful tool for building web applications and dashboards with Python.
