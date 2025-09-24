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


from typing import Dict, Union, List

# Import PersonAccount from CaO.py
from CaO import PersonAccount

## Exercise 3: Extend the `PersonAccount` class

# Create an enhanced PersonAccount instance with additional methods
# The PersonAccount class is imported from CaO.py

# Example usage:
person = PersonAccount(
    "John", "Doe", {"Salary": 5000, "Bonus": 1000}, {"Rent": 1500, "Food": 500}
)


# Additional methods that could be added to PersonAccount class:
def get_income_sources(account: PersonAccount) -> List[str]:
    """Get all income source names for a PersonAccount."""
    return list(account.incomes.keys())


def get_expense_sources(account: PersonAccount) -> List[str]:
    """Get all expense source names for a PersonAccount."""
    return list(account.expenses.keys())


print(f"Income sources: {get_income_sources(person)}")
print(f"Expense sources: {get_expense_sources(person)}")
print(f"Total income: {person.total_income()}")
print(f"Total expenses: {person.total_expense()}")
print(f"Account balance: {person.account_balance()}")
