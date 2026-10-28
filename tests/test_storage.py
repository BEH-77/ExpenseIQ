import json

import pytest

from expenseiq import ExpenseManager


def test_save_and_load_expenses(tmp_path):
    path = tmp_path / "expenses.json"
    manager = ExpenseManager(path)
    first = manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")
    second = manager.add_expense(5, "Travel", "2026-10-29", "Bus")

    reloaded = ExpenseManager(path)

    assert reloaded.list_expenses() == [first, second]
    assert reloaded.get_expense(1) == first
    saved = json.loads(path.read_text(encoding="utf-8"))
    assert saved["expenses"][0]["category"] == "Food"
    assert saved["next_id"] == 3


def test_update_and_delete_are_saved(tmp_path):
    path = tmp_path / "expenses.json"
    manager = ExpenseManager(path)
    first = manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")
    second = manager.add_expense(5, "Travel", "2026-10-29", "Bus")

    updated = manager.update_expense(second.id, amount=6.5)
    assert ExpenseManager(path).list_expenses() == [first, updated]

    manager.delete_expense(first.id)
    assert ExpenseManager(path).list_expenses() == [updated]


def test_empty_collection_and_id_after_delete(tmp_path):
    path = tmp_path / "expenses.json"
    manager = ExpenseManager(path)
    assert manager.list_expenses() == []

    manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")
    manager.delete_expense(1)
    reloaded = ExpenseManager(path)

    assert reloaded.list_expenses() == []
    assert reloaded.add_expense(5, "Travel", "2026-10-29", "Bus").id == 2


def test_invalid_json_is_reported(tmp_path):
    path = tmp_path / "expenses.json"
    path.write_text("{broken", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid JSON"):
        ExpenseManager(path)
