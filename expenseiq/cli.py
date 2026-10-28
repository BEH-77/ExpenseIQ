"""Small command-line interface for managing expenses."""

import argparse
from .expenses import ExpenseManager


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage local expenses")
    parser.add_argument("--file", default="expenses.json", help="JSON storage file")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Add an expense")
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--date", required=True)
    add.add_argument("--description", required=True)

    commands.add_parser("list", help="View expenses")

    update = commands.add_parser("update", help="Edit an expense")
    update.add_argument("id", type=int)
    update.add_argument("--amount", type=float)
    update.add_argument("--category")
    update.add_argument("--date")
    update.add_argument("--description")

    delete = commands.add_parser("delete", help="Delete an expense")
    delete.add_argument("id", type=int)

    args = parser.parse_args()
    try:
        manager = ExpenseManager(args.file)
        if args.command == "add":
            expense = manager.add_expense(args.amount, args.category, args.date, args.description)
            print(f"Added expense {expense.id}")
        elif args.command == "list":
            expenses = manager.list_expenses()
            if not expenses:
                print("No expenses recorded.")
            for expense in expenses:
                print(f"{expense.id}: {expense.date} | {expense.category} | "
                      f"{expense.amount:.2f} | {expense.description}")
        elif args.command == "update":
            changes = {name: getattr(args, name) for name in
                       ("amount", "category", "date", "description")
                       if getattr(args, name) is not None}
            manager.update_expense(args.id, **changes)
            print(f"Updated expense {args.id}")
        elif args.command == "delete":
            manager.delete_expense(args.id)
            print(f"Deleted expense {args.id}")
    except (ValueError, KeyError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
