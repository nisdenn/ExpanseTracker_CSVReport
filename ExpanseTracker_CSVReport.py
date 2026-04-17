import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amount", "Description"])
    except FileExistsError:
        pass

def add_transaction():
    t_type = input("Type (income/expense): ").lower()
    amount = float(input("Amount: "))
    desc = input("Description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, amount, desc])

    print("Transaction added!\n")

def view_transactions():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No data found.\n")

def show_balance():
    income = 0
    expense = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Type"] == "income":
                    income += float(row["Amount"])
                elif row["Type"] == "expense":
                    expense += float(row["Amount"])
    except FileNotFoundError:
        print("No data found.\n")
        return

    print(f"\nTotal Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Balance: {income - expense}\n")

def main():
    init_file()

    while True:
        print("=== EXPENSE TRACKER ===")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()