# ExpenseIQ

**ExpenseIQ** is a lightweight expense tracking application built with Python. It helps users record, categorize, and analyze their expenses, providing a simple way to understand and manage personal spending.

This project was developed as part of **Assignment 2 – GitHub Collaboration & Automation**, focusing on collaborative software development, version control, unit testing, and continuous integration.

## Features

### 1. Expense Management
- Add new expenses with an amount, category, date, and description.
- View recorded expenses.
- Delete existing expenses.
- Validate expense information.

### 2. Expense Analysis
- Calculate total expenses.
- Calculate spending by category.
- Identify the category with the highest spending.
- Generate spending summaries.

## Team Members

| Member | GitHub Username | Responsibilities |
|---|---|---|
| Badr | `@BEH-77` | Expense Management |
| Reda Nadir | `@xivzk` | Expense Analysis |

## Technologies

- **Python** – Application logic
- **pytest** – Unit testing
- **Git & GitHub** – Version control and collaboration
- **GitHub Actions** – Automated testing
- **GitHub Pages** – Project documentation website

## Project Structure

```text
ExpenseIQ/
├── expenseiq/
│   ├── __init__.py
│   ├── expenses.py
│   └── analysis.py
├── tests/
│   ├── test_expenses.py
│   └── test_analysis.py
├── docs/
│   └── index.html
├── .github/
│   └── workflows/
│       └── tests.yml
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

GitHub Actions automatically runs the Python test suite on pushes and Pull Requests to verify that the application works correctly.

## GitHub Pages

Project website: **[ExpenseIQ Project Page](https://YOUR_USERNAME.github.io/ExpenseIQ/)**

## Project Status

Project status: Development in progress.

## License

Created for educational purposes as part of Assignment 2 – GitHub Collaboration & Automation.
