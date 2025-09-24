import statistics as stat
from typing import Sequence, List, Dict, Union, Tuple


class Statistics:
    """
    A class to perform basic statistical calculations on a list of numbers.

    This class provides methods to calculate common statistical measures such as
    mean, median, mode, variance, and standard deviation.

    Attributes:
        data (Sequence[Union[int, float]]): A sequence of numbers to perform calculations on.

    Example:
        ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
        stats = Statistics(ages)
        print(stats.describe())
    """

    def __init__(self, data: Sequence[Union[int, float]]):
        """
        Initializes the Statistics class with a list of numbers.

        Args:
            data (Sequence[Union[int, float]]): A sequence of numbers.
        """
        self.data = data

    def get_data(self) -> Sequence[Union[int, float]]:
        """
        Returns the original data.

        Returns:
            Sequence[Union[int, float]]: The sequence of numbers.
        """
        return self.data

    def count(self) -> int:
        """
        Calculates the number of elements in the data.

        Returns:
            int: The count of numbers.
        """
        return len(self.data)

    def sum(self) -> Union[int, float]:
        """
        Calculates the sum of the numbers in the data.

        Returns:
            Union[int, float]: The sum of the numbers.
        """
        return sum(self.data)

    def min(self) -> Union[int, float]:
        """
        Finds the minimum value in the data.

        Returns:
            Union[int, float]: The minimum value.
        """
        return min(self.data)

    def max(self) -> Union[int, float]:
        """
        Finds the maximum value in the data.

        Returns:
            Union[int, float]: The maximum value.
        """
        return max(self.data)

    def range(self) -> Union[int, float]:
        """
        Calculates the range of the data.

        Returns:
            Union[int, float]: The range of the data.
        """
        return self.max() - self.min()

    def mean(self) -> float:
        """
        Calculates the mean of the data.

        Returns:
            float: The mean of the data.
        """
        return stat.mean(self.data)

    def median(self) -> Union[int, float]:
        """
        Calculates the median of the data.

        Returns:
            Union[int, float]: The median of the data.
        """
        return stat.median(self.data)

    def mode(self) -> Dict[str, Union[int, float]]:
        """
        Calculates the mode of the data.

        Returns:
            Dict[str, Union[int, float]]: A dictionary containing the mode and its count.
        """
        mode_value = stat.mode(self.data)
        return {"mode": mode_value, "count": self.data.count(mode_value)}

    def std(self) -> float:
        """
        Calculates the standard deviation of the data.

        Returns:
            float: The standard deviation of the data.
        """
        return stat.stdev(self.data)

    def var(self) -> float:
        """
        Calculates the variance of the data.

        Returns:
            float: The variance of the data.
        """
        return stat.variance(self.data)

    def freq_dist(self) -> List[Tuple[float, Union[int, float]]]:
        """
        Calculates the frequency distribution of the data.

        The frequency is expressed as a percentage.

        Returns:
            List[Tuple[float, Union[int, float]]]: A list of tuples, where each tuple
            contains the frequency (in percent) and the corresponding data value, sorted by frequency.
        """
        if not self.data:
            return []
        total = len(self.data)
        return sorted(
            [(self.data.count(i) * 100 / total, i) for i in set(self.data)],
            reverse=True,
        )

    def describe(self) -> str:
        """
        Provides a descriptive summary of the data.

        Returns:
            str: A string containing the summary of the data.
        """
        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean()}\n"
            f"Median: {self.median()}\n"
            f"Mode: {self.mode()}\n"
            f"Standard Deviation: {self.std():.2f}\n"
            f"Variance: {self.var():.2f}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )


# Example usage:
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
data = Statistics(ages)
print(data.describe())


class PersonAccount:
    """
    A class to manage a person's income and expenses.

    This class provides methods to calculate total income, total expenses,
    and the account balance. It also allows adding new income and expenses.

    Attributes:
        firstname (str): The person's first name.
        lastname (str): The person's last name.
        incomes (Dict[str, Union[int, float]]): A dictionary of income sources and amounts.
        expenses (Dict[str, Union[int, float]]): A dictionary of expense sources and amounts.

    Example:
        person = PersonAccount('John', 'Doe', {'Salary': 5000, 'Bonus': 1000}, {'Rent': 1500, 'Food': 500})
        print(person.account_info())
        person.add_income({'Freelance': 500})
        person.add_expense({'Utilities': 200})
        print(f"Account Balance: {person.account_balance()}")
    """

    def __init__(
        self,
        firstname: str,
        lastname: str,
        incomes: Dict[str, Union[int, float]],
        expenses: Dict[str, Union[int, float]],
    ):
        """
        Initializes the PersonAccount class.

        Args:
            firstname (str): The person's first name.
            lastname (str): The person's last name.
            incomes (Dict[str, Union[int, float]]): A dictionary of incomes.
            expenses (Dict[str, Union[int, float]]): A dictionary of expenses.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self) -> Union[int, float]:
        """
        Calculates the total income.

        Returns:
            Union[int, float]: The total income.
        """
        return sum(self.incomes.values())

    def total_expense(self) -> Union[int, float]:
        """
        Calculates the total expense.

        Returns:
            Union[int, float]: The total expense.
        """
        return sum(self.expenses.values())

    def account_info(self) -> str:
        """
        Provides information about the person's account.

        Returns:
            str: A string containing the person's name, total income, and total expense.
        """
        return f"{self.firstname} {self.lastname}'s account. Total income: {self.total_income()}, Total expense: {self.total_expense()}."

    def add_income(self, data: Dict[str, Union[int, float]]) -> None:
        """
        Adds new income sources.

        Args:
            data (Dict[str, Union[int, float]]): A dictionary of new income sources and amounts.
        """
        self.incomes.update(data)

    def add_expense(self, data: Dict[str, Union[int, float]]) -> None:
        """
        Adds new expense sources.

        Args:
            data (Dict[str, Union[int, float]]): A dictionary of new expense sources and amounts.
        """
        self.expenses.update(data)

    def account_balance(self) -> Union[int, float]:
        """
        Calculates the account balance.

        Returns:
            Union[int, float]: The account balance (total income - total expense).
        """
        return self.total_income() - self.total_expense()


# Example usage:
me = PersonAccount(
    "Rishabh",
    "Agrawal",
    {"Salary": 150000, "Bonus": 5500},
    {"Rent": 20000, "General": 4500},
)
print(me.total_income())
print(me.total_expense())
print(me.account_info())
me.add_income({"Diwali": 2500, "Birthday": 5000})
print(f"Incomes after adding: {me.incomes}")
me.add_expense({"Tax": 2500, "Fuel": 5000})
print(f"Expenses after adding: {me.expenses}")
print(f"Final Account Balance: {me.account_balance()}")
