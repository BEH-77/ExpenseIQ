"""Expense analytics: totals, category breakdowns, and summaries."""

from .expenses import Expense


def total_expenses(expenses: list[Expense]) -> float:
    """Return the sum of all expense amounts. Returns 0.0 for an empty list."""
    return sum(expense.amount for expense in expenses)


def spending_by_category(expenses: list[Expense]) -> dict[str, float]:
    """Return a mapping of category name -> total amount spent, sorted by category."""
    totals: dict[str, float] = {}
    for expense in expenses:
        totals[expense.category] = totals.get(expense.category, 0.0) + expense.amount
    return dict(sorted(totals.items()))


def top_category(expenses: list[Expense]) -> str | None:
    """Return the category with the highest total spending, or None if empty.

    Ties are broken alphabetically for deterministic output.
    """
    totals = spending_by_category(expenses)
    if not totals:
        return None
    # Sort by (-total, category) so highest spending wins, ties go alphabetical
    return min(totals.items(), key=lambda item: (-item[1], item[0]))[0]


def spending_summary(expenses: list[Expense]) -> dict[str, object]:
    """Return a structured summary of the expense list."""
    return {
        "total": total_expenses(expenses),
        "by_category": spending_by_category(expenses),
        "top_category": top_category(expenses),
        "count": len(expenses),
    }