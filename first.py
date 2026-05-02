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
        name = input("Enter the name of a group member: ").strip()

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
        payer = input("Enter payer name (or type 'Show balances' to finish): ").strip()

        if payer == "Show balances":
            break

        if payer not in people:
            print("Invalid payer. Please choose from:", people)
            continue

        amount = float(input("Enter amount paid: "))

        participants_input = input("Enter participants (comma-separated): ")
        participants = [p.strip() for p in participants_input.split(",")]

        valid = True
        for person in participants:
            if person not in people:
                print(f"{person} is not in the group.")
                valid = False

        if not valid:
            print("Please re-enter the expense using valid group members.\n")
            continue

        note = input("Enter note (optional): ")

        expense = {
            "payer": payer,
            "amount": amount,
            "participants": participants,
            "note": note
        }

        expenses.append(expense)
        print("Expense recorded.\n")

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
    expenses = get_expenses(people)

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
