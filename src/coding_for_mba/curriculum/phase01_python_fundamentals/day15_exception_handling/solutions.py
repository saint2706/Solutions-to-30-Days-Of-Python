# Day 15: Exception Handling - Solutions

## Exercise 1: Handling a `ValueError`


try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a numeric value for your age.")


## Exercise 2: Handling a `ZeroDivisionError`


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of the division is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter numeric values.")


## Exercise 3: Refactor `exception.py`


country_names = ["Finland"]

try:
    *nordic_countries, estonia, russia = country_names

    print("Nordic Countries:", nordic_countries)
    print("Estonia:", estonia)
    print("Russia:", russia)

except ValueError as e:
    if "not enough values to unpack" in str(e):
        print(
            f"Error: The list of countries must have at least two elements. Details: {e}"
        )
    else:
        print(f"A ValueError occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
