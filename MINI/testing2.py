import tkinter as tk
from tkinter import messagebox, font
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import ImageTk, Image

# Dictionary of GST rates for different expense categories in India
gst_rates = {
    'shirt': 5,
    'groceries': 0,
    'electronics': 18,
    'furniture': 12
}

expenses = []

def removeExpense():
    """Function to remove an expense from the list."""
    while True:
        listExpenses()
        try:
            expenseToRemove = int(input("Enter the index of the expense to remove: "))
            del expenses[expenseToRemove]
            update_expense_list()
            generateQRCode()  # Generate QR code upon removing an expense
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid index.")

def addExpense(amount, category):
    """Function to add a new expense to the list."""
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)
    update_expense_list()
    generateQRCode()  # Generate QR code upon adding new expense

def generateQRCode():
    """Function to generate and display QR code."""
    total_expenses = sum(float(expense['amount']) for expense in expenses)
    qr_data = f"Total Expenses: {total_expenses}\n\n"
    qr_data += "Expenses:\n"
    for expense in expenses:
        qr_data += f"- {expense['category']}: {expense['amount']}\n"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img = qr_img.resize((200, 200))  # Resize QR code image
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

def update_expense_list():
    """Function to update the displayed list of expenses."""
    list_box.delete(0, tk.END)
    for idx, expense in enumerate(expenses):
        list_box.insert(tk.END, f"{idx + 1}. {expense['category']}: ₹{expense['amount']}")

def calculateGST(amount, category):
    """Function to calculate GST amount based on expense category."""
    gst_percentage = gst_rates.get(category.lower(), 0)
    gst_amount = (gst_percentage / 100) * float(amount)
    return gst_amount

def handle_add_expense():
    """Handler for adding a new expense."""
    amount = amount_entry.get()
    category = category_entry.get()
    addExpense(amount, category)

# Creating the main application window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x400")
root.configure(bg="black")

# Customizing font style
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Widgets for adding expenses
amount_label = tk.Label(root, text="Amount (₹):", bg="black", fg="white", font=custom_font)
amount_label.pack(pady=10)

amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

category_label = tk.Label(root, text="Category:", bg="black", fg="white", font=custom_font)
category_label.pack(pady=10)

category_entry = tk.Entry(root)
category_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Expense", bg="#2337C6", fg="white", font=custom_font, command=handle_add_expense)
add_button.pack(pady=10)

# List box to display expenses
list_box = tk.Listbox(root, width=50, height=10, font=("Helvetica", 10))
list_box.pack(pady=20)

# Label for QR code display
qr_label = tk.Label(root, bg="white", width=200, height=200)
qr_label.pack(pady=20)

# Initialize list with existing expenses
update_expense_list()

root.mainloop()
