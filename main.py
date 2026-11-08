from datetime import date


class Transaction:
    def __init__(self, transaction_type, description, category, amount, transaction_date):
        self.transaction_type = transaction_type
        self.description = description
        self.category = category
        self.amount = amount
        self.transaction_date = transaction_date

    def display(self):
        print(
            f"{self.transaction_date} | {self.transaction_type:<7} | "
            f"{self.category:<12} | {self.description} | KSh {self.amount:,.2f}"
        )


transactions = []
CATEGORIES = ["Food", "Transport", "Rent", "Education", "Shopping", "Other"]


def add_transaction(transaction_type):
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    print("Categories:", ", ".join(CATEGORIES))
    category = input("Category: ").strip().title()
    if category not in CATEGORIES:
        print("Invalid category. Please choose one from the list.")
        return

    try:
        amount = float(input("Amount (KSh): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    transaction_date = input(
        f"Date (YYYY-MM-DD, press Enter for {date.today()}): "
    ).strip()

    if not transaction_date:
        transaction_date = str(date.today())
    else:
        try:
            date.fromisoformat(transaction_date)
        except ValueError:
            print("Date must use YYYY-MM-DD format.")
            return

    transactions.append(
        Transaction(transaction_type, description, category, amount, transaction_date)
    )
    print(f"{transaction_type} recorded successfully!")


def show_transactions():
    if not transactions:
        print("No transactions recorded.")
        return
    print("\nDATE       | TYPE    | CATEGORY     | DESCRIPTION | AMOUNT")
    print("-" * 75)
    for transaction in transactions:
        transaction.display()


def financial_summary():
    income = sum(t.amount for t in transactions if t.transaction_type == "Income")
    expenses = sum(t.amount for t in transactions if t.transaction_type == "Expense")
    print("\n========== FINANCIAL SUMMARY ==========")
    print(f"Total income: KSh {income:,.2f}")
    print(f"Total expenses: KSh {expenses:,.2f}")
    print(f"Remaining balance: KSh {income - expenses:,.2f}")
    if expenses > income:
        print("WARNING: Your total expenses exceed your total income.")
    print("=======================================")


def expenses_by_category():
    totals = {}
    for transaction in transactions:
        if transaction.transaction_type == "Expense":
            totals[transaction.category] = (
                totals.get(transaction.category, 0) + transaction.amount
            )

    if not totals:
        print("No expenses have been recorded.")
        return

    print("\n========== EXPENSES BY CATEGORY ==========")
    for category, amount in totals.items():
        print(f"{category}: KSh {amount:,.2f}")
    highest_category = max(totals, key=totals.get)
    print(f"Highest spending category: {highest_category}")
    print("==========================================")


def search_transactions():
    search_term = input("Search by description or category: ").strip().lower()
    if not search_term:
        print("Search term cannot be empty.")
        return

    matches = [
        t for t in transactions
        if search_term in t.description.lower()
        or search_term in t.category.lower()
    ]

    if not matches:
        print("No matching transactions found.")
    else:
        for transaction in matches:
            transaction.display()


def main_menu():
    while True:
        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Record income")
        print("2. Record expense")
        print("3. Display all transactions")
        print("4. Financial summary")
        print("5. View expenses by category")
        print("6. Search transactions")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction("Income")
        elif choice == "2":
            add_transaction("Expense")
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            financial_summary()
        elif choice == "5":
            expenses_by_category()
        elif choice == "6":
            search_transactions()
        elif choice == "7":
            print("Thank you for using the Personal Expense Tracker!")
            break
        else:
            print("Invalid option. Choose 1-7.")


if __name__ == "__main__":
    main_menu()
