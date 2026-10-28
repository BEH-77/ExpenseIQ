"""Unit tests for expense analytics."""

import pytest

from expenseiq.analytics import (
    spending_by_category,
    spending_summary,
    top_category,
    total_expenses,
)
from expenseiq.expenses import Expense


def make_expense(id_: int, amount: float, category: str) -> Expense:
    return Expense(id_, amount, category, "2026-10-28", "test")


# --- total_expenses ---

def test_total_expenses_empty_list_returns_zero():
    assert total_expenses([]) == 0.0


def test_total_expenses_sums_single_expense():
    assert total_expenses([make_expense(1, 12.50, "Food")]) == 12.50


def test_total_expenses_sums_multiple_expenses():
    expenses = [
        make_expense(1, 10.00, "Food"),
        make_expense(2, 25.50, "Transport"),
        make_expense(3, 4.50, "Food"),
    ]
    assert total_expenses(expenses) == pytest.approx(40.00)


# --- spending_by_category ---

def test_spending_by_category_empty_list_returns_empty_dict():
    assert spending_by_category([]) == {}


def test_spending_by_category_groups_repeated_categories():
    expenses = [
        make_expense(1, 10.00, "Food"),
        make_expense(2, 5.00, "Transport"),
        make_expense(3, 4.50, "Food"),
    ]
    result = spending_by_category(expenses)
    assert result == {"Food": pytest.approx(14.50), "Transport": pytest.approx(5.00)}


# --- top_category ---

def test_top_category_empty_list_returns_none():
    assert top_category([]) is None


def test_top_category_returns_highest_spending_category():
    expenses = [
        make_expense(1, 10.00, "Food"),
        make_expense(2, 50.00, "Transport"),
        make_expense(3, 5.00, "Food"),
    ]
    assert top_category(expenses) == "Transport"


def test_top_category_breaks_ties_alphabetically():
    expenses = [
        make_expense(1, 10.00, "Food"),
        make_expense(2, 10.00, "Books"),
    ]
    assert top_category(expenses) == "Books"


# --- spending_summary ---

def test_spending_summary_combines_all_metrics():
    expenses = [
        make_expense(1, 10.00, "Food"),
        make_expense(2, 20.00, "Transport"),
    ]
    summary = spending_summary(expenses)
    assert summary["total"] == pytest.approx(30.00)
    assert summary["count"] == 2
    assert summary["top_category"] == "Transport"
    assert summary["by_category"]["Food"] == pytest.approx(10.00)
    assert summary["by_category"]["Transport"] == pytest.approx(20.00)


def test_spending_summary_empty_list():
    summary = spending_summary([])
    assert summary == {
        "total": 0.0,
        "by_category": {},
        "top_category": None,
        "count": 0,
    }