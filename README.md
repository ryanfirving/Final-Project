# Shared Expense Settlement Program

## Description

This program helps a group of users split shared expenses and determine who owes whom by creating the most efficient possible repayment plan. Users first enter the members of a group, then input expenses by specifying who paid, how much was paid, and who participated in each expense. The program calculates each person’s balance and generates a repayment plan to settle debts efficiently.

The program also supports saving expenses to a CSV file and optionally loading them in future sessions, which allows users to continue tracking expenses across multiple runs of the program instead of losing data when the program ends. It also allows users to maintain an observable sheet of expenses over time while using the program.

---

## How to Run

1. Make sure all project files are in the same directory:
   - first.py
   - user_input.py
   - storage.py
   - calculations.py
   - repayment.py

2. Run the program using Python:

   python3 first.py

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

The program is organized into multiple code files to improve readability:

- user_input.py: handles all user interaction
- storage.py: handles saving and loading data from CSV files
- calculations.py: performs balance calculations
- repayment.py: generates the repayment plan

---

## Use of AI Tools

I used ChatGPT as a coding assistant during this project. ChatGPT helped me brainstorm ideas, debug issues, and write or revise portions of the code.

Specifically, I used ChatGPT to help with:
- designing and building the repayment algorithm that determines who should pay whom
- adding input validation for names, yes/no responses, amounts, and participants
- implementing CSV saving and loading
- reorganizing the program into multiple files
- fixing bugs, such as invalid yes/no inputs being accepted
- refining and formatting this README

I reviewed, tested, and modified all code to ensure both full understanding and that it works correctly.
