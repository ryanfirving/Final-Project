def get_expenses():
    expenses = []

    while True:
        payer = input("Enter payer name (or type 'Show balances' to finish): ")

        if payer == "Show balances":
            break

        amount = float(input("Enter amount paid: "))

        participants_input = input("Enter participants (comma-separated): ")
        participants = participants_input.split(",")

        # Clean up spaces
        participants = [p.strip() for p in participants]

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


def main():
    expenses = get_expenses()

    people = get_people(expenses)
    paid = calculate_paid(expenses, people)
    owed = calculate_owed(expenses, people)
    balances = calculate_balances(paid, owed)

    print("\n--- BALANCES ---")
    for person in balances:
        print(f"{person}: {balances[person]:.2f}")


main()
