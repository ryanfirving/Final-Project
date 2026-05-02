import csv

def welcome_user():
    print("Welcome to the Shared Expense Settlement Program!")
    print()
    print("This program will help your group figure out who owes whom after shared expenses.")
    print("First, you will enter the names of the group members.")
    print("Then, you will enter each expense, including:")
    print("- who paid")
    print("- how much they paid")
    print("- who the expense was for")
    print("- an optional note describing the expense")
    print()
    print("When you are done entering expenses, type 'Show balances'.")
    print("The program will then calculate balances and create a repayment plan.")
    print()

def get_group_members():
    people = []

    while True:
        name = input("Enter the name of a group member: ").strip().title()

        if name == "":
            print("Name cannot be blank.")
            continue

        if name in people:
            print("That person is already in the group.")
            continue

        people.append(name)

        while True:
            another = input("Is there another group member? (yes/no): ").strip().lower()

            if another == "yes":
                break
            elif another == "no":
                if len(people) < 2:
                    print("You need at least two people to split expenses.")
                    break
                return people
            else:
                print("Please enter 'yes' or 'no'.")


def get_expenses(people):
    expenses = []

    while True:
        payer = input("Enter payer name (or type 'Show balances' to finish): ").strip().title()

        if payer.lower() == "show balances":
            break

        if payer not in people:
            print("Invalid payer. Please choose from:", people)
            continue

        while True:
            amount_input = input("Enter amount paid: ").strip()

            try:
                amount = float(amount_input)

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number, such as 12.50.")

        participants_input = input("Enter participants (comma-separated): ").strip()

        if participants_input == "":
            print("Participants cannot be blank.")
            continue

        participants = [p.strip().title() for p in participants_input.split(",")]

        valid = True

        for person in participants:
            if person not in people:
                print(f"{person} is not in the group.")
                valid = False

        if not valid:
            print("Please re-enter the expense using valid group members.\n")
            continue

        note = input("Enter note (optional): ").strip()

        expense = {
            "payer": payer,
            "amount": amount,
            "participants": participants,
            "note": note
        }

        expenses.append(expense)
        print("Expense recorded.\n")

    return expenses

def save_expenses_to_csv(expenses, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["payer", "amount", "participants", "note"])

        for expense in expenses:
            participants_string = ",".join(expense["participants"])

            writer.writerow([
                expense["payer"],
                expense["amount"],
                participants_string,
                expense["note"]
            ])

def load_expenses_from_csv(filename):
    expenses = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = {
                    "payer": row["payer"],
                    "amount": float(row["amount"]),
                    "participants": row["participants"].split(","),
                    "note": row["note"]
                }

                expenses.append(expense)

    except FileNotFoundError:
        print("No saved expense file found yet.")

    return expenses

def get_people(expenses):
    people = set()

    for expense in expenses:
        people.add(expense["payer"])
        for person in expense["participants"]:
            people.add(person)

    return list(people)


def calculate_paid(expenses, people):
    paid = {person: 0 for person in people}

    for expense in expenses:
        payer = expense["payer"]
        paid[payer] += expense["amount"]

    return paid


def calculate_owed(expenses, people):
    owed = {person: 0 for person in people}

    for expense in expenses:
        amount = expense["amount"]
        participants = expense["participants"]

        share = amount / len(participants)

        for person in participants:
            owed[person] += share

    return owed


def calculate_balances(paid, owed):
    balances = {}

    for person in paid:
        balances[person] = paid[person] - owed[person]

    return balances

def create_repayment_plan(balances):
    debtors = []
    creditors = []

    for person in balances:
        balance = round(balances[person], 2)

        if balance < 0:
            debtors.append([person, -balance])
        elif balance > 0:
            creditors.append([person, balance])

    payments = []

    debtor_index = 0
    creditor_index = 0

    while debtor_index < len(debtors) and creditor_index < len(creditors):
        debtor = debtors[debtor_index]
        creditor = creditors[creditor_index]

        amount = min(debtor[1], creditor[1])
        amount = round(amount, 2)

        payments.append({
            "from": debtor[0],
            "to": creditor[0],
            "amount": amount
        })

        debtor[1] -= amount
        creditor[1] -= amount

        debtor[1] = round(debtor[1], 2)
        creditor[1] = round(creditor[1], 2)

        if debtor[1] == 0:
            debtor_index += 1

        if creditor[1] == 0:
            creditor_index += 1

    return payments


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
