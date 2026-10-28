# ExpenseIQ

**ExpenseIQ** is a lightweight expense "causing a merge conflict" tracking application built with Python. It helps users record, categorize, and analyze their expenses, providing a simple way to understand and manage personal spending.


This project was developed as part of **Assignment 2 – GitHub Collaboration & Automation**, focusing on collaborative software development, version control, unit testing, and continuous integration.

## Features

### 1. Expense Management
- Add new expenses with an amount, category, date, and description.
- View recorded expenses.
- Edit existing expenses.
- Delete existing expenses.
- Validate expense information.
- Store and retrieve expenses from a local JSON file.

### 2. Expense Analytics 
- Calculate total expenses.
- Calculate spending by category.
- Identify the category with the highest spending.
- Generate spending summaries.

## Team Members

| Member | GitHub Username | Responsibilities |
|---|---|---|
| Badr | `@BEH-77` | Expense Management |
| Erraji Jihane | `@erraji-jihane` | Expense Analysis |

## Technologies

- **Python** – Application logic
- **pytest** – Unit testing
- **Git & GitHub** – Version control and collaboration
- **GitHub Actions** – Automated pytest checks on pushes and pull requests
- **GitHub Pages** – Project documentation website (published after setup)

## Project Structure

```text
ExpenseIQ/
├── expenseiq/
│   ├── __init__.py
│   ├── analytics.py       
│   ├── expenses.py
│   ├── storage.py
│   └── cli.py
├── tests/
│   ├── test_analytics.py  
│   ├── test_expenses.py
│   └── test_storage.py
├── docs/
│   ├── index.html         # GitHub Pages website
│   └── styles.css
└── .github/workflows/
    └── tests.yml          # Automated pytest workflow
```

## Installation

Clone the repository:

```bash
git clone https://github.com/BEH-77/ExpenseIQ.git
cd ExpenseIQ
```

Create a virtual environment and install the test dependency (Python 3.10 or newer):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate` instead of `source .venv/bin/activate`.

## Using Expense Management

Run the command-line interface with `python -m expenseiq.cli`. Expenses are saved to `expenses.json` in the current directory by default. Use `--file PATH` before a command to choose another JSON file.

```bash
python -m expenseiq.cli add --amount 12.50 --category Food --date 2026-10-28 --description "Lunch"
python -m expenseiq.cli list
python -m expenseiq.cli update 1 --amount 13.00
python -m expenseiq.cli delete 1
```

Dates use YYYY-MM-DD. Amounts must be greater than zero. Expense analytics are available as pure functions in expenseiq.analytics.

## Running Tests

Run all unit tests using:

```bash
python -m pytest -v
```

The suite covers expense management, validation, local storage, and analytics.

## GitHub Collaboration

Development follows a feature-branch workflow:

1. Each member creates a dedicated feature branch.
2. Changes are committed with meaningful commit messages.
3. Pull Requests are opened for code review.
4. At least one team member reviews and approves changes.
5. Automated tests must pass before merging into `main`.

The `main` branch is protected through GitHub repository rules.

## Continuous Integration

The workflow in `.github/workflows/tests.yml` installs dependencies and runs the full pytest suite on pushes and pull requests.

## GitHub Pages

The static project website lives in `docs/` and is prepared for deployment from the `main` branch and `/docs` folder. After the website branch is reviewed and merged, enable GitHub Pages in repository **Settings → Pages → Build and deployment**, select **Deploy from a branch**, then select `main` and `/docs`.

Expected website URL: [https://beh-77.github.io/ExpenseIQ/](https://beh-77.github.io/ExpenseIQ/). The link will work after GitHub Pages is enabled and the first deployment completes.

## Project Status

Project status: Development in progress.

## License

Created for educational purposes as part of Assignment 2 – GitHub Collaboration & Automation.
