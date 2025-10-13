# 📘 Day 16: File Handling for Business Analytics

A huge part of data analysis involves reading data from files and writing results to them. Whether you're processing a sales report, a customer list, or log files, you need to interact with the file system. Python makes this easy.

## Key Concepts

- **Opening Files:** Use the `open()` function to open a file. It's best practice to use it with a `with` statement, which automatically closes the file for you, even if errors occur.
  ```python
  with open('my_report.txt', 'r') as file:
      content = file.read()
  ```
- **File Modes:**
  - `'r'`: Read (default). Throws an error if the file doesn't exist.
  - `'w'`: Write. Creates a new file or overwrites an existing one.
  - `'a'`: Append. Adds content to the end of an existing file.
- **Exception Handling:** When working with files, it's crucial to wrap your code in a `try...except FileNotFoundError` block to handle cases where a file might be missing.

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `fh.py`, has been refactored to provide several powerful, reusable functions for common business file-handling tasks.

1. **Review the Code:** Open `Day_16_File_Handling/fh.py`. Examine functions like `count_words_and_lines()`, `find_most_common_words()`, `extract_emails_from_file()`, and `analyze_sales_csv()`.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script. It will create a few temporary demo files, run the analysis functions on them, print the results, and then clean up the files.
   ```bash
   python Day_16_File_Handling/fh.py
   ```
1. **Run the Tests:** The tests for this lesson are more advanced. They create temporary files in memory to test the functions without needing actual files on your disk.
   ```bash
   pytest tests/test_day_16.py
   ```

## 💻 Exercises: Day 16

1. **Analyze a Text File:**

   - In a new script (`my_solutions_16.py`), create a simple text file named `my_memo.txt` and write a few sentences into it.
   - Import the `count_words_and_lines` and `find_most_common_words` functions from the lesson script.
   - Call these functions with your new file's path and print the results.

1. **Process a Simple CSV:**

   - Create a function `create_sales_data(filepath, sales_data)` that takes a list of lists and writes it to a CSV file.
   - Your `sales_data` could be `[['Product', 'Price', 'Quantity'], ['Widget A', '10.00', '50'], ['Widget B', '15.50', '30']]`.
   - Import and use the `analyze_sales_csv` function from the lesson to read your new CSV and print the total revenue and average transaction value.

🎉 **Excellent!** You can now programmatically read from and write to the most common file types. This is a fundamental skill for automating data intake, processing reports, and saving your analysis.

English Stop Words Collection for Text Analytics

This module provides a comprehensive list of common English stop words
used in business text analysis, sentiment analysis, and natural language
processing tasks. Stop words are frequently used words that are typically
filtered out during text preprocessing to focus on meaningful content.

Business Use Cases:
- Customer review sentiment analysis
- Social media monitoring and brand sentiment
- Content analysis of business documents
- Market research text mining
- Competitor analysis from web content

Usage:
    from data.stop_words import stop_words

    # Filter out stop words from business text
    business_text = "The company has great customer service"
    filtered_words = [word for word in business_text.lower().split()
                      if word not in stop_words]
    print(filtered_words)  # ['company', 'great', 'customer', 'service']

```python

from typing import List

# Comprehensive English stop words list for business text analysis
stop_words: List[str] = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "you're",
    "you've",
    "you'll",
    "you'd",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "she's",
    "her",
    "hers",
    "herself",
    "it",
    "it's",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "that'll",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "don't",
    "should",
    "should've",
    "now",
    "d",
    "ll",
    "m",
    "o",
    "re",
    "ve",
    "y",
    "ain",
    "aren",
    "aren't",
    "couldn",
    "couldn't",
    "didn",
    "didn't",
    "doesn",
    "doesn't",
    "hadn",
    "hadn't",
    "hasn",
    "hasn't",
    "haven",
    "haven't",
    "isn",
    "isn't",
    "ma",
    "mightn",
    "mightn't",
    "mustn",
    "mustn't",
    "needn",
    "needn't",
    "shan",
    "shan't",
    "shouldn",
    "shouldn't",
    "wasn",
    "wasn't",
    "weren",
    "weren't",
    "won",
    "won't",
    "wouldn",
    "wouldn't",
]

```
