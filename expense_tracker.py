class Expense:
    def __init__(self, amount, category, note):
        self.amount = amount
        self.category = category
        self.note = note

    def display(self):
        print(f"Amount: ₹{self.amount} | Category: {self.category} | Note: {self.note}")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        try:
            amount = float(input("Enter amount: ₹"))
            category = input("Enter category (Food/Travel/etc): ")
            note = input("Enter note/description: ")

            expense = Expense(amount, category, note)
            self.expenses.append(expense)

            print("✅ Expense added successfully!\n")

        except ValueError:
            print("❌ Invalid amount!\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.\n")
            return

        print("\n--- Expense List ---")
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. ", end="")
            exp.display()
        print()

    def total_spending(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"\n💰 Total Spending: ₹{total}\n")

    def filter_category(self):
        category = input("Enter category to filter: ")
        found = False

        print(f"\n--- Expenses in {category} ---")
        for exp in self.expenses:
            if exp.category.lower() == category.lower():
                exp.display()
                found = True

        if not found:
            print("No matching expenses found.")
        print()


def main():
    tracker = ExpenseTracker()

    while True:
        print("====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_spending()

        elif choice == "4":
            tracker.filter_category()

        elif choice == "5":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice!\n")


if __name__ == "__main__":
    main()
