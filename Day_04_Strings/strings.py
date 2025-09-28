"""
Day 4: Manipulating Business Text Data with Strings (Refactored)

This script demonstrates common string manipulations and methods
applied to business-related text data. This version is refactored
into functions for better organization and testability.
"""

def generate_report_header(title, year):
    """Creates a formatted report header."""
    return f"*** {title.upper()} - FY{year} ***"

def clean_and_format_name(raw_name):
    """Cleans and capitalizes a raw name string."""
    return raw_name.strip().title()

def format_date_string(date_str, old_separator="-", new_separator="/"):
    """Replaces separators in a date string."""
    return date_str.replace(old_separator, new_separator)

def parse_sku(sku):
    """Parses a SKU string into its component parts."""
    parts = sku.split("-")
    if len(parts) == 3:
        return {"type": parts[0], "name": parts[1], "id": parts[2]}
    return None

def is_transaction_type(transaction_id, prefix):
    """Checks if a transaction ID starts with a given prefix."""
    return transaction_id.startswith(prefix)

def has_file_extension(filename, extension):
    """Checks if a filename ends with a given extension."""
    return filename.endswith(extension)

def feedback_contains_keyword(feedback, keyword):
    """Checks if a feedback string contains a specific keyword."""
    return feedback.find(keyword) != -1

if __name__ == "__main__":
    # --- Formatting Strings for Reports ---
    print("--- Generating Report Headers ---")
    header_text = generate_report_header("Quarterly Sales Report", 2024)
    print(header_text)
    print("-" * 20)

    # --- Cleaning Customer and Product Data ---
    print("--- Data Cleaning Examples ---")
    customer_name = "  john doe  "
    formatted_customer_name = clean_and_format_name(customer_name)
    print(f"Raw name: '{customer_name}', Final formatted name: '{formatted_customer_name}'")

    date_string = "2023-Jan-15"
    formatted_date_str = format_date_string(date_string)
    print(f"Original date: {date_string}, Formatted date: {formatted_date_str}")
    print("-" * 20)

    # --- Parsing and Extracting Information from Strings ---
    print("--- Parsing Product and Transaction IDs ---")
    product_sku = "PROD-GADGET-001"
    parsed_sku = parse_sku(product_sku)
    if parsed_sku:
        print(f"SKU: {product_sku}")
        print(f"  Product Type: {parsed_sku['type']}")
        print(f"  Product Name: {parsed_sku['name']}")
        print(f"  Product ID: {parsed_sku['id']}")
    print()

    trans_id = "INV-2024-03-15-998"
    is_inv = is_transaction_type(trans_id, "INV")
    print(f"Transaction '{trans_id}' is an invoice: {is_inv}")

    report_filename = "q1_sales_report.pdf"
    is_a_pdf = has_file_extension(report_filename, ".pdf")
    print(f"Report file '{report_filename}' is a PDF: {is_a_pdf}")
    print("-" * 20)

    # --- Searching for keywords ---
    customer_feedback_text = "The new CRM is great, but the reporting feature is slow."
    if feedback_contains_keyword(customer_feedback_text, "slow"):
        print("Feedback contains the word 'slow'. Action may be required.")
    else:
        print("Feedback does not contain the word 'slow'.")