import tkinter as tk
from tkinter import messagebox
import qrcode
import os

# Function to calculate GST based on expense category
def calculate_gst(category, amount):
    # Implement GST calculation logic based on categories
    gst_rate = 0.18 if category == "Groceries" else 0.12
    gst_amount = amount * gst_rate
    return gst_amount

# Function to generate QR code for expenses
def generate_qr_code(expenses):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(str(expenses))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("expenses_qr_code.png")

# Function to handle expense submission
def submit_expense():
    category = category_entry.get()
    amount = float(amount_entry.get())
    gst = calculate_gst(category, amount)
    total_amount = amount + gst
    expenses.append({'category': category, 'amount': amount, 'gst': gst, 'total_amount': total_amount})
    messagebox.showinfo("Expense Tracker", "Expense added successfully!")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Function to download expenses as PDF using QR code
def download_expenses():
    generate_qr_code(expenses)
    os.system("convert expenses_qr_code.png expenses.pdf")
    os.remove("expenses_qr_code.png")
    messagebox.showinfo("Expense Tracker", "Expenses downloaded as PDF!")

# Initialize Tkinter window
root = tk.Tk()
root.title("Expense Tracker")

# Create GUI elements
tk.Label(root, text="Category:").grid(row=0, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=0, column=1)

tk.Label(root, text="Amount:").grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

submit_button = tk.Button(root, text="Submit Expense", command=submit_expense)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

download_button = tk.Button(root, text="Download Expenses (PDF)", command=download_expenses)
download_button.grid(row=3, column=0, columnspan=2, pady=10)

# Expense data storage
expenses = []

root.mainloop()
