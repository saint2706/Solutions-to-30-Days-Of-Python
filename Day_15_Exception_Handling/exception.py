"""
Day 15: Exception Handling

This script demonstrates the use of extended iterable unpacking and a try-except block.
"""

# A list of country names
country_names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

try:
    # This is an example of extended iterable unpacking.
    # The '*' operator is used to assign multiple items to a single variable.
    # In this case, 'nordic_countries' will be a list of the first n-2 items,
    # 'estonia' will be the second to last item, and 'russia' will be the last item.
    *nordic_countries, estonia, russia = country_names

    print("Nordic Countries:", nordic_countries)
    print("Estonia:", estonia)
    print("Russia:", russia)

except Exception as e:
    # This block will be executed if any exception occurs in the 'try' block.
    # It's a good practice to catch specific exceptions instead of the general 'Exception',
    # but for this educational example, we are catching any possible exception.
    print(f"An error occurred: {e}")
