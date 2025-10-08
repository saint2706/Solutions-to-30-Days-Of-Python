import os
import sys

import pytest

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_18_Classes_and_Objects.CaO import PersonAccount, Statistics


@pytest.fixture
def sample_data():
    return [10, 20, 30, 20]


@pytest.fixture
def multimodal_data():
    return [1, 2, 3, 4, 5]  # No unique mode


def test_statistics_init(sample_data):
    """Tests the initialization of the Statistics class."""
    stats = Statistics(sample_data)
    assert stats.data == sample_data


def test_statistics_calculations(sample_data):
    """Tests basic statistical calculations."""
    stats = Statistics(sample_data)
    assert stats.count() == 4
    assert stats.sum() == 80
    assert stats.min() == 10
    assert stats.max() == 30
    assert stats.range() == 20
    assert stats.mean() == 20
    assert stats.median() == 20
    assert stats.std() == pytest.approx(8.16, rel=1e-2)
    assert stats.var() == pytest.approx(66.67, rel=1e-2)


def test_statistics_mode(sample_data):
    """Tests the mode calculation."""
    stats = Statistics(sample_data)
    mode_result = stats.mode()
    assert mode_result["mode"] == 20
    assert mode_result["count"] == 2


def test_statistics_no_unique_mode(multimodal_data):
    """Tests the mode calculation when there is no unique mode."""
    stats = Statistics(multimodal_data)
    mode_result = stats.mode()
    assert mode_result["mode"] == "No unique mode"
    assert mode_result["count"] == 0


def test_statistics_empty_data():
    """Tests that the Statistics class handles empty data gracefully."""
    stats = Statistics([])
    assert stats.count() == 0
    assert stats.sum() == 0
    assert stats.min() is None
    assert stats.max() is None
    assert stats.range() == 0
    assert stats.mean() == 0.0
    assert stats.median() == 0.0
    assert stats.std() == 0.0
    assert stats.var() == 0.0


def test_person_account_init():
    """Tests the initialization of the PersonAccount class."""
    person = PersonAccount("John", "Doe")
    assert person.firstname == "John"
    assert person.lastname == "Doe"
    assert person.incomes == {}
    assert person.expenses == {}


def test_person_account_transactions():
    """Tests adding income/expenses and calculating totals."""
    person = PersonAccount("Jane", "Smith")
    person.add_income("Salary", 5000)
    person.add_income("Bonus", 1000)
    person.add_expense("Rent", 1500)
    person.add_expense("Food", 500)

    assert person.total_income() == 6000
    assert person.total_expense() == 2000
    assert person.account_balance() == 4000

    # Test adding to existing category
    person.add_expense("Food", 100)
    assert person.total_expense() == 2100
    assert person.account_balance() == 3900
