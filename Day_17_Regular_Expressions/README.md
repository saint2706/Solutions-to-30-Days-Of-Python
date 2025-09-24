# 🔍 Day 17: Regular Expressions

## Welcome to Day 17

Today, we're going to learn about a powerful tool for text processing: **regular expressions** (often shortened to "regex" or "regexp"). This is an essential skill for anyone working with text data.

## Why are Regular Expressions Important for Business Analytics?

As a business analyst, you'll often need to extract specific information from large amounts of text, such as:

- Finding all the email addresses or phone numbers in a document.
- Extracting product codes or order numbers from unstructured text.
- Cleaning up messy text data by removing unwanted characters or formatting.

Regular expressions provide a concise and powerful way to perform these tasks, saving you a lot of time and effort compared to writing complex string manipulation code.

## Regular Expressions in Python

Python's built-in `re` module provides a set of functions for working with regular expressions.

## Exploring `regex.py`

The `regex.py` script in this folder provides several examples of how to use regular expressions in Python to solve common text processing problems.

## 💻 Exercises: Day 17

1. **Find all numbers in a string**:
    - The `para` variable in `regex.py` contains a string with some numbers.
    - Write a Python script that uses `re.findall()` to extract all the numbers from this string and prints them as a list of integers.

2. **Validate a variable name**:
    - The `is_valid_variable` function in `regex.py` checks if a string is a valid Python variable name.
    - Test this function with the following inputs: `_name`, `first_name`, `1name`, `name-1`. Which ones are valid?

3. **Clean up a messy sentence**:
    - The `sentence` variable in `regex.py` contains a string with a lot of unwanted characters.
    - Use the `clean_text` function to clean up this sentence.
    - After cleaning the text, use the `most_common_words` function to find the 3 most common words in the cleaned sentence.

### Solutions

You can find the solutions to these exercises in the `solutions.py` file in this directory.

🎉 **Congratulations!** You've learned how to use regular expressions to process and extract information from text data. This is a valuable skill that you'll use time and time again in your analytics career.
