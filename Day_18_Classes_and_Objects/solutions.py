# Day 18: Classes and Objects - Solutions

from datetime import datetime
from typing import Dict, Union, List

## Exercise 1 & 2: Create a `Car` class with a `get_age` method

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> None:
        print(f"Car Information: {self.year} {self.make} {self.model}")

    def get_age(self) -> int:
        current_year = datetime.now().year
        return current_year - self.year

# Example usage:
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
print(f"The car is {my_car.get_age()} years old.")


## Exercise 3: Extend the `PersonAccount` class

# We need to import the PersonAccount class from the CaO.py file
# For this to work, make sure the files are in the same directory.
try:
    from CaO import PersonAccount
except ImportError:
    # If the import fails, we define a simplified version of the class here
    # so the solution can be run independently.
    class PersonAccount:
        def __init__(self, firstname: str, lastname: str, incomes: Dict[str, Union[int, float]], expenses: Dict[str, Union[int, float]]):
            self.firstname = firstname
            self.lastname = lastname
            self.incomes = incomes
            self.expenses = expenses

        def get_income_sources(self) -> List[str]:
            return list(self.incomes.keys())

        def get_expense_sources(self) -> List[str]:
            return list(self.expenses.keys())

# Example usage:
person = PersonAccount('John', 'Doe', {'Salary': 5000, 'Bonus': 1000}, {'Rent': 1500, 'Food': 500})
print(f"Income sources: {person.get_income_sources()}")
print(f"Expense sources: {person.get_expense_sources()}")
