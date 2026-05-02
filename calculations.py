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
