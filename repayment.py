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
