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

Day 16: File Handling for Business Analytics (Refactored)

This module demonstrates various file handling operations commonly used in business.

```python

import csv
import os
import re
import string
from collections import Counter
from typing import Dict, List, Optional, Tuple

# Import stop words from the local file
from .stop_words import stop_words as sw


def count_words_and_lines(fname: str) -> Tuple[int, int]:
    """Count words and lines in a text file."""
    num_words, num_lines = 0, 0
    try:
        with open(fname, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                wordslist = line.split()
                num_lines += 1
                num_words += len(wordslist)
        return num_words, num_lines
    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return 0, 0
    except IOError as e:
        print(f"❌ Error reading file '{fname}': {e}")
        return 0, 0


def find_most_common_words(fname: str, top_n: int) -> List[Tuple[str, int]]:
    """Find the most frequently used words in a text file, ignoring stop words."""
    try:
        with open(fname, "r", encoding="utf-8") as f:
            text = f.read().lower()

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()

        # Filter out stop words
        filtered_words = [word for word in words if word not in sw]

        # Count and return the most common
        counts = Counter(filtered_words)
        return counts.most_common(top_n)

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return []
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return []


def extract_emails_from_file(fname: str) -> List[str]:
    """Extract all unique email addresses from a text file."""
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    try:
        with open(fname, "r", encoding="utf-8") as f:
            text = f.read()

        emails = re.findall(email_pattern, text)
        return sorted(list(set(emails)))  # Return unique emails, sorted

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return []
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return []


def analyze_sales_csv(fname: str) -> Optional[Dict[str, float]]:
    """
    Reads a sales CSV and calculates total revenue and average transaction value.
    Assumes CSV format: Product,Price,Quantity
    """
    total_revenue = 0.0
    transaction_count = 0

    try:
        with open(fname, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            _ = next(csv_reader)  # Skip header row

            for row in csv_reader:
                try:
                    price = float(row[1])
                    quantity = int(row[2])
                    total_revenue += price * quantity
                    transaction_count += 1
                except (ValueError, IndexError):
                    # Skip rows with malformed data
                    continue

        if transaction_count == 0:
            return None

        average_transaction = total_revenue / transaction_count
        return {
            "total_revenue": total_revenue,
            "average_transaction": average_transaction,
        }

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None


def main():
    """Main function to demonstrate file handling capabilities."""
    print("🗂️  Day 16: File Handling for Business Analytics")
    print("=" * 60)

    # Create dummy files for demonstration
    # In a real scenario, these files would already exist.
    demo_text_content = "This is a sample business report. The report details sales and profits. Contact support@example.com for details."
    demo_csv_content = "Product,Price,Quantity\nLaptop,1200.00,5\nMouse,25.50,10"

    demo_text_file = "demo_report.txt"
    demo_csv_file = "demo_sales.csv"

    with open(demo_text_file, "w") as f:
        f.write(demo_text_content)
    with open(demo_csv_file, "w") as f:
        f.write(demo_csv_content)

    # 1. Analyze document word counts
    print("\n📄 Document Analysis Example:")
    words, lines = count_words_and_lines(demo_text_file)
    print(f"✅ Document '{demo_text_file}' has {words} words and {lines} lines.")

    # 2. Find most common words
    print("\n📊 Most Common Words Example:")
    common_words = find_most_common_words(demo_text_file, 3)
    print(f"✅ Top 3 most common words: {common_words}")

    # 3. Extract emails
    print("\n📧 Email Extraction Example:")
    emails = extract_emails_from_file(demo_text_file)
    print(f"✅ Found emails: {emails}")

    # 4. Analyze CSV data
    print("\n📈 CSV Sales Analysis Example:")
    sales_analysis = analyze_sales_csv(demo_csv_file)
    if sales_analysis:
        print(f"✅ Total Revenue: ${sales_analysis['total_revenue']:.2f}")
        print(f"✅ Average Transaction: ${sales_analysis['average_transaction']:.2f}")

    # Clean up dummy files
    os.remove(demo_text_file)
    os.remove(demo_csv_file)

    print("\n✨ Demonstration complete!")


if __name__ == "__main__":
    main()

```
