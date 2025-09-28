"""
Day 5: Managing and Analyzing Business Data with Lists (Refactored)

This script demonstrates how to create, access, modify, and analyze
lists containing business-related data. This version is refactored
into functions for better organization and testability.
"""

def get_list_element(data_list, index):
    """Safely gets an element from a list by its index."""
    if -len(data_list) <= index < len(data_list):
        return data_list[index]
    return None

def get_first_half_sales(sales_list):
    """Returns the first half of a list of sales."""
    midpoint = len(sales_list) // 2
    return sales_list[:midpoint]

def add_product(product_list, new_product):
    """Adds a new product to a list of products."""
    new_list = product_list.copy()
    new_list.append(new_product)
    return new_list

def remove_product(product_list, product_to_remove):
    """Removes a product from a list if it exists."""
    new_list = product_list.copy()
    if product_to_remove in new_list:
        new_list.remove(product_to_remove)
    return new_list

def analyze_team_sales(sales_figures):
    """Sorts sales, finds top performers, and returns an analysis."""
    if not sales_figures:
        return None

    sorted_sales = sorted(sales_figures, reverse=True)
    top_3_sales = sorted_sales[:3]
    total_top_sales = sum(top_3_sales)

    return {
        "sorted_sales": sorted_sales,
        "top_3_sales": top_3_sales,
        "total_top_sales": total_top_sales,
    }

if __name__ == "__main__":
    # --- Initializing Lists with Business Data ---
    print("--- Initializing Business Lists ---")
    departments_list = ["Sales", "Marketing", "Human Resources", "Engineering"]
    quarterly_sales_figures = [120000.50, 135000.75, 110000.00, 145000.25]
    print(f"Company Departments: {departments_list}")
    print(f"Quarterly Sales: {quarterly_sales_figures}")
    print("-" * 20)

    # --- Accessing and Slicing List Data ---
    print("--- Accessing Specific Data ---")
    marketing_department = get_list_element(departments_list, 1)
    print(f"The second department is: {marketing_department}")

    last_sales = get_list_element(quarterly_sales_figures, -1)
    print(f"Sales for the last quarter: ${last_sales}")

    first_half_figures = get_first_half_sales(quarterly_sales_figures)
    print(f"First half sales: {first_half_figures}")
    print("-" * 20)

    # --- Modifying Lists ---
    print("--- Modifying a Product List ---")
    initial_products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
    print(f"Original product list: {initial_products}")

    products_after_add = add_product(initial_products, "Webcam")
    print(f"After adding 'Webcam': {products_after_add}")

    products_after_remove = remove_product(products_after_add, "Mouse")
    print(f"After removing 'Mouse': {products_after_remove}")
    print("-" * 20)

    # --- Analyzing List Data ---
    print("--- Analyzing Sales Performance ---")
    team_sales_figures = [5000, 8000, 4500, 12000, 6000, 11000]
    print(f"Sales figures for the team: {team_sales_figures}")

    sales_analysis = analyze_team_sales(team_sales_figures)
    if sales_analysis:
        print(f"Sales sorted from highest to lowest: {sales_analysis['sorted_sales']}")
        print(f"Top 3 sales figures: {sales_analysis['top_3_sales']}")
        print(f"Total sales from top 3 performers: ${sales_analysis['total_top_sales']}")
    print("-" * 20)