"""
Day 4: Manipulating Business Text Data with Strings

This script demonstrates common string manipulations and methods
applied to business-related text data.
"""

# --- Formatting Strings for Reports ---
print("--- Generating Report Headers ---")
report_title = "Quarterly Sales Report"
fiscal_year = 2024

# Using an f-string and the .upper() method to create a clean, formatted header.
header = f"*** {report_title.upper()} - FY{fiscal_year} ***"
print(header)
print("-" * 20)


# --- Cleaning Customer and Product Data ---
print("--- Data Cleaning Examples ---")

# .strip() is essential for cleaning user input or messy data.
raw_customer_name = "  john doe  "
cleaned_name = raw_customer_name.strip()
print(f"Raw name: '{raw_customer_name}', Cleaned name: '{cleaned_name}'")

# .title() is a handy method for capitalizing names correctly.
formatted_name = cleaned_name.title()
print(f"Final formatted name: '{formatted_name}'")
print()

# .replace() is great for standardizing data.
raw_date = "2023-Jan-15"
formatted_date = raw_date.replace("-", "/")
print(f"Original date: {raw_date}, Formatted date: {formatted_date}")
print("-" * 20)


# --- Parsing and Extracting Information from Strings ---
print("--- Parsing Product and Transaction IDs ---")

# .split() is used to break a string into a list of smaller strings.
sku = "PROD-GADGET-001"
parts = sku.split("-")
print(f"SKU: {sku}")
print(f"  Product Type: {parts[0]}")
print(f"  Product Name: {parts[1]}")
print(f"  Product ID: {parts[2]}")
print()

# .startswith() helps in identifying or validating data.
transaction_id = "INV-2024-03-15-998"
is_invoice = transaction_id.startswith("INV")
print(f"Transaction '{transaction_id}' is an invoice: {is_invoice}")

# .endswith() is great for checking file types.
report_file = "q1_sales_report.pdf"
is_pdf = report_file.endswith(".pdf")
print(f"Report file '{report_file}' is a PDF: {is_pdf}")
print("-" * 20)

# .find() can be used to locate substrings
customer_feedback = "The new CRM is great, but the reporting feature is slow."
# find returns the starting index of the word, or -1 if not found
if customer_feedback.find("slow") != -1:
    print("Feedback contains the word 'slow'. Action may be required.")
else:
    print("Feedback does not contain the word 'slow'.")
