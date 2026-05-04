# Shared Expense Settlement Program

## Description

This program helps a group of users split shared expenses and determine who owes whom. Users first enter the members of a group, then input expenses by specifying who paid, how much was paid, and who participated in each expense. The program calculates each person’s balance and generates a repayment plan to settle debts efficiently.

The program also supports saving expenses to a CSV file and optionally loading them in future sessions. This allows users to continue tracking expenses across multiple runs of the program instead of losing data when the program ends.

---

## How to Run

1. Make sure all project files are in the same directory:
   - first.py (main file)
   - user_input.py
   - storage.py
   - calculations.py
   - repayment.py

2. Run the program using Python:

   python first.py

3. Follow the prompts:
   - Enter group members
   - Choose whether to load previous expenses
   - Enter expenses
   - Type "Show balances" when finished

4. The program will:
   - Display balances for each person
   - Output a repayment plan
   - Save all expenses to `expenses.csv`

---

## Features

- Input validation (prevents invalid names, amounts, and participants)
- Case-insensitive input handling
- Persistent storage using CSV files
- Modular design across multiple files
- Automated repayment plan generation

---

## Design Notes

The program is organized into multiple modules to improve readability and maintainability:

- user_input.py: handles all user interaction
- storage.py: handles saving and loading data from CSV files
- calculations.py: performs balance calculations
- repayment.py: generates the repayment plan

This modular structure separates different responsibilities and makes the program easier to understand and extend.

---

## Known Limitations

- The program assumes that previously saved expenses belong to the current group of users
- If a different group uses the program, loaded expenses may not match the current participants

---

## Use of AI Tools

I used ChatGPT as a coding assistant during this project. ChatGPT helped me brainstorm ideas, debug issues, and write or revise portions of the code.

Specifically, I used ChatGPT to help with:
- designing and building the repayment algorithm that determines who should pay whom
- adding input validation for names, yes/no responses, amounts, and participants
- writing the try/except structure for handling invalid numeric input
- implementing CSV saving and loading to allow expenses to persist across sessions
- reorganizing the program into multiple files to improve readability and structure
- identifying and fixing bugs, such as invalid yes/no inputs being accepted
- refining and formatting this README

I reviewed, tested, and modified all code in my own development environment to ensure it works correctly and meets the project requirements.

---

## External Sources

- Python CSV documentation:
  https://docs.python.org/3/library/csv.html
