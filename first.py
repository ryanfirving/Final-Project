from storage import save_expenses_to_csv, load_expenses_from_csv
from calculations import calculate_paid, calculate_owed, calculate_balances
from repayment import create_repayment_plan
from userinput import welcome_user, get_group_members, get_expenses

def get_people(expenses):
    people = set()

    for expense in expenses:
        people.add(expense["payer"])
        for person in expense["participants"]:
            people.add(person)

    return list(people)

def main():
    welcome_user()

    people = get_group_members()

    saved_expenses = []

    choice = input("Do you want to load previous expenses? (yes/no): ").strip().lower()

    if choice == "yes":
        saved_expenses = load_expenses_from_csv("expenses.csv")

        if len(saved_expenses) > 0:
            print(f"{len(saved_expenses)} saved expenses were loaded.")
        else:
            print("No saved expenses found.")

    if len(saved_expenses) > 0:
        print(f"{len(saved_expenses)} saved expenses were loaded.")

    new_expenses = get_expenses(people)

    expenses = saved_expenses + new_expenses

    save_expenses_to_csv(expenses, "expenses.csv")
    print("Expenses saved to expenses.csv.")

    paid = calculate_paid(expenses, people)
    owed = calculate_owed(expenses, people)
    balances = calculate_balances(paid, owed)

    print("\n--- BALANCES ---")
    for person in balances:
        print(f"{person}: {balances[person]:.2f}")

    payments = create_repayment_plan(balances)

    print("\n--- REPAYMENT PLAN ---")
    if len(payments) == 0:
        print("No repayments needed.")
    else:
        for payment in payments:
            print(f"{payment['from']} pays {payment['to']}: ${payment['amount']:.2f}")

main()
