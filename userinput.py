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
