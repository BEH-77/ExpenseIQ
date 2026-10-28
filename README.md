# ExpenseIQ

**ExpenseIQ** is a lightweight expense tracking application built with Python. It helps users record, categorize, and analyze their expenses, providing a simple way to understand and manage personal spending.

This project was developed as part of **Assignment 2 – GitHub Collaboration & Automation**, focusing on collaborative software development, version control, unit testing, and continuous integration.

## Features

### 1. Expense Management
- Add new expenses with an amount, category, date, and description.
- View recorded expenses.
- Edit existing expenses.
- Delete existing expenses.
- Validate expense information.
- Store and retrieve expenses from a local JSON file.

### 2. Expense Analytics (Planned)
- Calculate total expenses.
- Calculate spending by category.
- Identify the category with the highest spending.
- Generate spending summaries.

## Team Members

| Member | GitHub Username | Responsibilities |
|---|---|---|
| Badr | `@BEH-77` | Core Expense Management: add, view, edit, and delete expenses; validate expense information; implement expense storage and retrieval. |
| Reda Nadir | `@xivzk` | Expense Analytics: calculate total spending and expenses by category; identify the highest-spending category; generate spending summaries and statistics. |

## Technologies

- **Python** – Application logic
- **pytest** – Unit testing
- **Git & GitHub** – Version control and collaboration
- **GitHub Actions** – Planned automated testing
- **GitHub Pages** – Planned project documentation website

## Project Structure

```text
ExpenseIQ/
├── expenseiq/
│   ├── __init__.py
│   ├── expenses.py
│   ├── storage.py
│   └── cli.py
├── tests/
│   ├── test_expenses.py
│   └── test_storage.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ExpenseIQ.git
cd ExpenseIQ
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Using Expense Management

Run the command-line interface with `python -m expenseiq.cli`. Expenses are saved to `expenses.json` in the current directory by default. Use `--file PATH` before a command to choose another JSON file.

```bash
python -m expenseiq.cli add --amount 12.50 --category Food --date 2026-10-28 --description "Lunch"
python -m expenseiq.cli list
python -m expenseiq.cli update 1 --amount 13.00
python -m expenseiq.cli delete 1
```

Dates use `YYYY-MM-DD`. Amounts must be greater than zero. Expense analytics are planned separately.

## Running Tests

Run all unit tests using:

```bash
python -m pytest
```

The project aims to include at least six meaningful unit tests covering normal behavior, edge cases, and invalid inputs.

## GitHub Collaboration

Development follows a feature-branch workflow:

1. Each member creates a dedicated feature branch.
2. Changes are committed with meaningful commit messages.
3. Pull Requests are opened for code review.
4. At least one team member reviews and approves changes.
5. Automated tests must pass before merging into `main`.

The `main` branch is protected through GitHub repository rules.

## Continuous Integration

GitHub Actions testing is planned for a later stage of the assignment.

## GitHub Pages

The project website is planned for a later stage of the assignment.

## Project Status

Project status: Development in progress.

## License

Created for educational purposes as part of Assignment 2 – GitHub Collaboration & Automation.
