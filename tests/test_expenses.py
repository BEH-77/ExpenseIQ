import pytest

from expenseiq import ExpenseManager


@pytest.fixture
def manager(tmp_path):
    return ExpenseManager(tmp_path / "expenses.json")


def test_add_and_view_expense(manager):
    expense = manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")

    assert expense.id == 1
    assert expense.amount == 12.5
    assert manager.get_expense(1) == expense
    assert manager.list_expenses() == [expense]


@pytest.mark.parametrize("amount", [0, -1, float("nan"), float("inf"), True])
def test_invalid_amounts_are_rejected(manager, amount):
    with pytest.raises(ValueError, match="Amount"):
        manager.add_expense(amount, "Food", "2026-10-28", "Lunch")

    assert manager.list_expenses() == []


@pytest.mark.parametrize("date", ["2026-02-30", "28/10/2026", "20261028", ""])
def test_invalid_dates_are_rejected(manager, date):
    with pytest.raises(ValueError, match="Date"):
        manager.add_expense(12.5, "Food", date, "Lunch")


@pytest.mark.parametrize("field", ["category", "description"])
def test_required_text_fields_are_rejected_when_blank(manager, field):
    values = {"amount": 12.5, "category": "Food", "date": "2026-10-28", "description": "Lunch"}
    values[field] = "  "

    with pytest.raises(ValueError, match=field.capitalize()):
        manager.add_expense(**values)


def test_update_existing_expense(manager):
    manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")

    updated = manager.update_expense(1, amount=13.0, description="Dinner")

    assert updated.amount == 13.0
    assert updated.description == "Dinner"
    assert updated.category == "Food"
    assert manager.get_expense(1) == updated


def test_invalid_update_leaves_saved_expense_unchanged(manager):
    original = manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")

    with pytest.raises(ValueError, match="Amount"):
        manager.update_expense(1, amount=0)

    assert ExpenseManager(manager.path).get_expense(1) == original


def test_delete_existing_expense(manager):
    manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")

    manager.delete_expense(1)

    assert manager.list_expenses() == []


@pytest.mark.parametrize("operation", ["get", "update", "delete"])
def test_nonexistent_id_is_rejected(manager, operation):
    with pytest.raises(KeyError, match="does not exist"):
        if operation == "get":
            manager.get_expense(99)
        elif operation == "update":
            manager.update_expense(99, amount=10)
        else:
            manager.delete_expense(99)


def test_boolean_id_is_rejected(manager):
    manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")

    with pytest.raises(ValueError, match="Expense ID"):
        manager.get_expense(True)
