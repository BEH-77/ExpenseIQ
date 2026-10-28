import json

import pytest

from expenseiq import ExpenseManager


def test_save_and_load_expenses(tmp_path):
    path = tmp_path / "expenses.json"
    manager = ExpenseManager(path)
    first = manager.add_expense(12.5, "Food", "2026-10-28", "Lunch")
    manager.add_expense(5, "Travel", "2026-10-29", "Bus")

    reloaded = ExpenseManager(path)

    assert len(reloaded.list_expenses()) == 2
    assert reloaded.get_expense(1) == first
    assert json.loads(path.read_text(encoding="utf-8"))["expenses"][0]["category"] == "Food"


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
