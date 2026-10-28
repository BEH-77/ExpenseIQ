"""Expense validation and management, independent of analytics."""

from dataclasses import asdict, dataclass
from datetime import date as calendar_date
from math import isfinite
from pathlib import Path

from .storage import load_data, save_data


@dataclass(frozen=True)
class Expense:
    id: int
    amount: float
    category: str
    date: str
    description: str

    def __post_init__(self) -> None:
        if type(self.id) is not int or self.id < 1:
            raise ValueError("Expense ID must be a positive integer")
        if isinstance(self.amount, bool) or not isinstance(self.amount, (int, float)):
            raise ValueError("Amount must be a positive number")
        if not isfinite(self.amount) or self.amount <= 0:
            raise ValueError("Amount must be a positive, finite number")
        for name in ("category", "description"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name.capitalize()} is required")
        if not isinstance(self.date, str):
            raise ValueError("Date must use YYYY-MM-DD")
        try:
            parsed_date = calendar_date.fromisoformat(self.date)
        except ValueError as exc:
            raise ValueError("Date must be a valid date in YYYY-MM-DD format") from exc
        if parsed_date.isoformat() != self.date:
            raise ValueError("Date must use YYYY-MM-DD")


class ExpenseManager:
    """Manage expenses in one JSON file, saving each change immediately."""

    def __init__(self, path: str | Path = "expenses.json") -> None:
        self.path = Path(path)
        data = load_data(self.path)
        try:
            self._expenses = [Expense(**record) for record in data["expenses"]]
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Invalid expense record in {self.path}") from exc
        self._next_id = data["next_id"]
        ids = [expense.id for expense in self._expenses]
        if len(ids) != len(set(ids)) or any(id_ >= self._next_id for id_ in ids):
            raise ValueError(f"Invalid expense IDs in {self.path}")

    def _save(self) -> None:
        save_data(self.path, {
            "next_id": self._next_id,
            "expenses": [asdict(expense) for expense in self._expenses],
        })

    def add_expense(
        self, amount: float, category: str, date: str, description: str
    ) -> Expense:
        expense = Expense(self._next_id, amount, category, date, description)
        self._expenses.append(expense)
        self._next_id += 1
        self._save()
        return expense

    def list_expenses(self) -> list[Expense]:
        return list(self._expenses)

    def get_expense(self, expense_id: int) -> Expense:
        if type(expense_id) is not int or expense_id < 1:
            raise ValueError("Expense ID must be a positive integer")
        for expense in self._expenses:
            if expense.id == expense_id:
                return expense
        raise KeyError(f"Expense ID {expense_id} does not exist")

    def update_expense(self, expense_id: int, **changes: object) -> Expense:
        existing = self.get_expense(expense_id)
        allowed = {"amount", "category", "date", "description"}
        if not changes or set(changes) - allowed:
            raise ValueError("Provide one or more valid expense fields to update")
        updated = Expense(**(asdict(existing) | changes))
        index = self._expenses.index(existing)
        self._expenses[index] = updated
        self._save()
        return updated

    def delete_expense(self, expense_id: int) -> None:
        existing = self.get_expense(expense_id)
        self._expenses.remove(existing)
        self._save()
