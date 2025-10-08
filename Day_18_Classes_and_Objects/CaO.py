"""
Day 18: Classes and Objects for Structured Business Data (Refactored)

This module demonstrates how to use classes and objects to model
real-world business concepts like a statistics calculator and a personal account.
"""

import statistics as stat
from collections import Counter
from typing import Any, Dict, List, Sequence, Tuple, Union


class Statistics:
    """
    A class to perform basic statistical calculations on a list of numbers.
    """

    def __init__(self, data: Sequence[Union[int, float]]):
        """Initializes the Statistics class with a sequence of numbers."""
        if not data:
            # Handle empty data case gracefully
            self.data = []
        else:
            self.data = data

    def count(self) -> int:
        """Calculates the number of elements."""
        return len(self.data)

    def sum(self) -> Union[int, float]:
        """Calculates the sum of the numbers."""
        return sum(self.data) if self.data else 0

    def min(self) -> Union[int, float, None]:
        """Finds the minimum value."""
        return min(self.data) if self.data else None

    def max(self) -> Union[int, float, None]:
        """Finds the maximum value."""
        return max(self.data) if self.data else None

    def range(self) -> Union[int, float]:
        """Calculates the range of the data."""
        return self.max() - self.min() if self.data else 0

    def mean(self) -> float:
        """Calculates the mean."""
        return stat.mean(self.data) if self.data else 0.0

    def median(self) -> Union[int, float]:
        """Calculates the median."""
        return stat.median(self.data) if self.data else 0.0

    def mode(self) -> Dict[str, Any]:
        """Calculates the mode, handling cases with no unique mode."""
        if not self.data:
            return {"mode": "No data", "count": 0}

        counts = Counter(self.data)
        most_common = counts.most_common(2)  # Get up to two most common

        # If there's only one item or the most common is more frequent than the second most common
        if len(most_common) == 1 or most_common[0][1] > most_common[1][1]:
            mode_value = most_common[0][0]
            return {"mode": mode_value, "count": most_common[0][1]}
        else:
            return {"mode": "No unique mode", "count": 0}

    def std(self) -> float:
        """Calculates the standard deviation."""
        return stat.stdev(self.data) if self.count() > 1 else 0.0

    def var(self) -> float:
        """Calculates the variance."""
        return stat.variance(self.data) if self.count() > 1 else 0.0

    def freq_dist(self) -> List[Tuple[float, Union[int, float]]]:
        """Calculates the frequency distribution as percentages."""
        if not self.data:
            return []
        total = self.count()
        counts = Counter(self.data)
        return sorted(
            [(count / total * 100, item) for item, count in counts.items()],
            reverse=True,
        )

    def describe(self) -> str:
        """Provides a descriptive summary of the data."""
        if not self.data:
            return "No data to describe."

        desc = (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean():.2f}\n"
            f"Median: {self.median()}\n"
            f"Mode: {self.mode()['mode']} (Count: {self.mode()['count']})\n"
            f"Standard Deviation: {self.std():.2f}\n"
            f"Variance: {self.var():.2f}"
        )
        return desc


class PersonAccount:
    """A class to manage a person's income and expenses."""

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes: Dict[str, Union[int, float]] = {}
        self.expenses: Dict[str, Union[int, float]] = {}

    def add_income(self, source: str, amount: Union[int, float]):
        """Adds an income source and amount."""
        self.incomes[source] = self.incomes.get(source, 0) + amount

    def add_expense(self, category: str, amount: Union[int, float]):
        """Adds an expense category and amount."""
        self.expenses[category] = self.expenses.get(category, 0) + amount

    def total_income(self) -> Union[int, float]:
        """Calculates the total income."""
        return sum(self.incomes.values())

    def total_expense(self) -> Union[int, float]:
        """Calculates the total expense."""
        return sum(self.expenses.values())

    def account_balance(self) -> Union[int, float]:
        """Calculates the account balance."""
        return self.total_income() - self.total_expense()

    def account_info(self) -> str:
        """Provides information about the person's account."""
        return f"{self.firstname} {self.lastname}'s account:\n  Total Income: ${self.total_income():,.2f}\n  Total Expense: ${self.total_expense():,.2f}\n  Balance: ${self.account_balance():,.2f}"


def main():
    """Main function to demonstrate class usage."""
    print("--- Statistics Class Demonstration ---")
    ages = [
        31,
        26,
        34,
        37,
        27,
        26,
        32,
        32,
        26,
        27,
        27,
        24,
        32,
        33,
        27,
        25,
        26,
        38,
        37,
        31,
        34,
        24,
        33,
        29,
        26,
    ]
    stats_data = Statistics(ages)
    print(stats_data.describe())
    print("-" * 20)

    print("\n--- PersonAccount Class Demonstration ---")
    person_account = PersonAccount("Rishabh", "Agrawal")
    person_account.add_income("Salary", 150000)
    person_account.add_income("Bonus", 5500)
    person_account.add_expense("Rent", 20000)
    person_account.add_expense("General", 4500)

    print(person_account.account_info())

    person_account.add_income("Diwali", 2500)
    person_account.add_expense("Fuel", 5000)
    print("\nAfter adding more income and expenses:")
    print(person_account.account_info())
    print("-" * 20)


if __name__ == "__main__":
    main()
