
import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add a new expense
def add_expense():
    print("\n===== ADD EXPENSE =====")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/etc.): ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    print("\n===== ALL EXPENSES =====")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            found = True
            print(
                "Date:", row["Date"],
                "| Category:", row["Category"],
                "| Description:", row["Description"],
                "| Amount: Rs.", row["Amount"]
            )

        if not found:
            print("No expenses recorded yet.")


# Filter expenses by category
def filter_expenses():
    category = input("\nEnter category to search: ").strip().lower()

    print("\n===== FILTERED EXPENSES =====")

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].lower() == category:
                found = True
                print(
                    row["Date"],
                    row["Category"],
                    row["Description"],
                    "Rs.", row["Amount"]
                )

    if not found:
        print("No expenses found in this category.")


# Category-wise summary
def category_summary():
    print("\n===== CATEGORY SUMMARY =====")

    totals = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    if not totals:
        print("No expenses available.")
        return

    for category, total in totals.items():
        print(category, ": Rs.", round(total, 2))

    print("-------------------------")
    print("Total Expenses: Rs.", round(sum(totals.values()), 2))


# Main program
create_file()

while True:
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses by Category")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
