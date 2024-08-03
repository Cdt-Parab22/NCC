import tkinter as tk
from tkinter import messagebox

expenses = []
expense1 = {'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '21.55', 'category': 'groceries'}
expenses.append(expense2)

def removeExpense():
    """Function to remove an expense from the list."""
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except:
            print("Invalid input. Please try again.")

def addExpense(amount, category):
    """Function to add a new expense to the list."""
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    """Function to print the menu options."""
    print("Please choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")

def listExpenses():
    """Function to list all expenses."""
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    counter = 0
    for expense in expenses:
        print("#", counter, " - ", expense['amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")

def handle_add_expense():
    """Handler for adding a new expense."""
    amount = amount_entry.get()
    category = category_entry.get()
    addExpense(amount, category)
    update_expense_list()

def handle_remove_expense():
    """Handler for removing an expense."""
    try:
        expenseToRemove = int(remove_entry.get())
        del expenses[expenseToRemove]
        update_expense_list()
    except:
        messagebox.showerror("Error", "Invalid input. Please enter a valid index.")

def update_expense_list():
    """Function to update the displayed list of expenses."""
    list_box.delete(0, tk.END)
    for idx, expense in enumerate(expenses):
        list_box.insert(tk.END, f"#{idx} - {expense['amount']} - {expense['category']}")

# Creating the main application window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

# Widgets for adding expenses
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=10)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

category_label = tk.Label(root, text="Category:")
category_label.pack(pady=10)
category_entry = tk.Entry(root)
category_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Expense", command=handle_add_expense)
add_button.pack(pady=10)

# Widget for removing expenses
remove_label = tk.Label(root, text="Enter index to remove:")
remove_label.pack(pady=10)
remove_entry = tk.Entry(root)
remove_entry.pack(pady=5)

remove_button = tk.Button(root, text="Remove Expense", command=handle_remove_expense)
remove_button.pack(pady=10)

# List box to display expenses
list_box = tk.Listbox(root, width=50, height=10)
list_box.pack(pady=20)

update_expense_list()  # Initialize list with existing expenses

root.mainloop()
