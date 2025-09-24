# 📁 Day 16: File Handling

## Welcome to Day 16!

Today, we'll dive into **file handling**, which is the process of working with files on your computer. This is a fundamental skill for any data analyst or developer, as it allows you to read, write, and update data from various sources.

## Why is File Handling Important for Business Analytics?

In business analytics, you'll constantly be working with data stored in files. Whether it's reading sales data from a CSV file, parsing customer feedback from a text file, or saving your analysis to a new file, understanding file handling is essential. It enables you to:
- **Automate data processing**: Write scripts that can process thousands of files without manual intervention.
- **Integrate with other systems**: Read data from and write data to other systems that use files for data exchange.
- **Create persistent reports**: Save the results of your analysis to a file that can be shared with stakeholders.

## Basic File Operations in Python

Python provides a built-in `open()` function to work with files. It's a good practice to use the `with` statement, which ensures that the file is automatically closed.

```python
with open("filename.txt", "r") as f:
    content = f.read()
    print(content)
```

## Exploring `fh.py`

The `fh.py` script in this folder contains a variety of functions that demonstrate different aspects of file handling and text processing. It's a great example of how file handling can be combined with other programming concepts to build powerful data processing tools.

## 💻 Exercises: Day 16

1.  **Word and Line Count**:
    *   Create a text file named `my_story.txt` and write a short story in it.
    *   Write a Python script that reads the file and prints the number of words and lines in the story. You can adapt the `counter` function from `fh.py`.

2.  **JSON Data Processing**:
    *   The `data` directory contains a file named `countries_data.json`.
    *   Write a Python script that reads this file and finds the top 5 most populated countries. You can adapt the `most_populated_countries` function from `fh.py`.

3.  **Email Extraction**:
    *   The `data` directory contains a file named `email_exchanges.txt`.
    *   Write a Python script that reads this file and extracts all the unique email addresses from it. You can use the `extract_emails` function from `fh.py` as a starting point.

### Solutions

You can find the solutions to these exercises in the `solutions.py` file in this directory.

🎉 **Congratulations!** You've learned the basics of file handling in Python. You're now equipped to work with a wide variety of data sources.
