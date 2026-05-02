import csv


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
