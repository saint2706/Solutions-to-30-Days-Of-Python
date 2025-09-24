"""Business greeting module for Python applications.

This module demonstrates how to create reusable business functions
that can be imported and used across different Python scripts.
"""

def greet_person(firstname: str, lastname: str) -> str:
    """Generate a personalized business greeting message.
    
    This function combines first and last names to create a professional
    welcome message, commonly used in business applications for customer
    onboarding or employee management systems.
    
    Args:
        firstname (str): The person's first name
        lastname (str): The person's last name
        
    Returns:
        str: A formatted greeting message
        
    Example:
        >>> greet_person("John", "Smith")
        'John Smith, welcome to 30DaysOfPython Challenge!'
    """
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
