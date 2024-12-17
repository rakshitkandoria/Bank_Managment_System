import tkinter as tk
from tkinter import messagebox
import random
import pymysql.cursors

# Database connection
connection = pymysql.connect(
    host="localhost",
    user='root',
    password="passward",  # Replace with your MySQL password
    cursorclass=pymysql.cursors.DictCursor,
    database="user"
)
mycursor = connection.cursor()

# Functions for navigating the UI
def show_main_menu():
    new_user_frame.pack_forget()
    login_user_frame.pack_forget()
    transaction_frame.pack_forget()
    deposit_frame.pack_forget()
    withdraw_frame.pack_forget()
    main_menu_frame.pack()

def show_new_user():
    main_menu_frame.pack_forget()
    new_user_frame.pack()

def show_login_user():
    main_menu_frame.pack_forget()
    login_user_frame.pack()

def show_transaction():
    login_user_frame.pack_forget()
    transaction_frame.pack()

def show_deposit():
    transaction_frame.pack_forget()
    deposit_frame.pack()

def show_withdraw():
    transaction_frame.pack_forget()
    withdraw_frame.pack()

# Function to create a new user
def create_new_user():
    name = name_entry.get()
    age = age_entry.get()
    pin = pin_entry.get()
    state = state_entry.get()
    gender = gender_entry.get()
    account_no = random.randint(10000000000, 99999999999)

    if not (name and age and pin and state and gender):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        mycursor.execute(
            "INSERT INTO table1 (name, age, pin, state, gender, balance, account_no) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, int(age), int(pin), state, gender, 0, account_no)
        )
        connection.commit()
        messagebox.showinfo("Success", "New user created successfully!\nAccount No: " + str(account_no))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to log in as an existing user
def login_user():
    global logged_in_user
    name = login_name_entry.get()
    pin = login_pin_entry.get()

    if not (name and pin):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        mycursor.execute("SELECT * FROM table1 WHERE name = %s AND pin = %s", (name, int(pin)))
        user = mycursor.fetchone()

        if user:
            logged_in_user = user
            balance_label.config(text=f"Current Balance: ₹{logged_in_user['balance']}")
            show_transaction()
        else:
            messagebox.showerror("Error", "Invalid credentials.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to deposit money
def deposit_money():
    amount = deposit_entry.get()

    if not amount or not amount.isdigit() or int(amount) <= 0:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    new_balance = logged_in_user['balance'] + int(amount)
    try:
        mycursor.execute("UPDATE table1 SET balance = %s WHERE account_no = %s", (new_balance, logged_in_user['account_no']))
        connection.commit()
        logged_in_user['balance'] = new_balance
        balance_label.config(text=f"Current Balance: ₹{new_balance}")
        messagebox.showinfo("Success", f"Deposited ₹{amount} successfully!")
        show_main_menu()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to withdraw money
def withdraw_money():
    amount = withdraw_entry.get()

    if not amount or not amount.isdigit() or int(amount) <= 0:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    if int(amount) > logged_in_user['balance']:
        messagebox.showerror("Error", "Insufficient balance.")
        return

    new_balance = logged_in_user['balance'] - int(amount)
    try:
        mycursor.execute("UPDATE table1 SET balance = %s WHERE account_no = %s", (new_balance, logged_in_user['account_no']))
        connection.commit()
        logged_in_user['balance'] = new_balance
        balance_label.config(text=f"Current Balance: ₹{new_balance}")
        messagebox.showinfo("Success", f"Withdrawn ₹{amount} successfully!")
        show_main_menu()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter setup
root = tk.Tk()
root.title("Bank Management System")
root.geometry("500x600")
root.config(bg="#f5f5f5")

logged_in_user = None

# Colorful Theme
bg_color = "#f5f5f5"  # Light Gray
button_color = "#4caf50"  # Green
button_hover_color = "#45a049"  # Darker Green for hover
label_color = "#2c3e50"  # Dark Grayish Blue
frame_border_color = "#3498db"  # Soft Blue boundary for frames

# Function to create a frame with border
def create_frame_with_border(parent, bg_color, border_color, border_width=1):
    frame = tk.Frame(parent, bg=bg_color, bd=border_width, relief="solid", highlightbackground=border_color, highlightthickness=border_width)
    return frame

# Main Menu Frame
main_menu_frame = create_frame_with_border(root, bg_color, frame_border_color)
main_menu_frame.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(main_menu_frame, text="Bank Management System", font=("Arial", 18, "bold"), bg=bg_color, fg=label_color).pack(pady=40)

tk.Button(main_menu_frame, text="New User", font=("Arial", 14), command=show_new_user, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)
tk.Button(main_menu_frame, text="Login User", font=("Arial", 14), command=show_login_user, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)
tk.Button(main_menu_frame, text="Exit", font=("Arial", 14), command=root.destroy, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)

# New User Frame
new_user_frame = create_frame_with_border(root, bg_color, frame_border_color)

tk.Label(new_user_frame, text="Create New User", font=("Arial", 16, "bold"), bg=bg_color, fg=label_color).pack(pady=20)

name_label = tk.Label(new_user_frame, text="Name:", bg=bg_color, fg=label_color)
name_label.pack(pady=5)
name_entry = tk.Entry(new_user_frame, font=("Arial", 12))
name_entry.pack(pady=5)

age_label = tk.Label(new_user_frame, text="Age:", bg=bg_color, fg=label_color)
age_label.pack(pady=5)
age_entry = tk.Entry(new_user_frame, font=("Arial", 12))
age_entry.pack(pady=5)

pin_label = tk.Label(new_user_frame, text="PIN:", bg=bg_color, fg=label_color)
pin_label.pack(pady=5)
pin_entry = tk.Entry(new_user_frame, show="*", font=("Arial", 12))
pin_entry.pack(pady=5)

state_label = tk.Label(new_user_frame, text="State:", bg=bg_color, fg=label_color)
state_label.pack(pady=5)
state_entry = tk.Entry(new_user_frame, font=("Arial", 12))
state_entry.pack(pady=5)

gender_label = tk.Label(new_user_frame, text="Gender:", bg=bg_color, fg=label_color)
gender_label.pack(pady=5)
gender_entry = tk.Entry(new_user_frame, font=("Arial", 12))
gender_entry.pack(pady=5)

tk.Button(new_user_frame, text="Create User", font=("Arial", 12), command=create_new_user, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=15)
tk.Button(new_user_frame, text="Back to Main Menu", font=("Arial", 12), command=show_main_menu, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)

# Login User Frame
login_user_frame = create_frame_with_border(root, bg_color, frame_border_color)

tk.Label(login_user_frame, text="Login", font=("Arial", 16, "bold"), bg=bg_color, fg=label_color).pack(pady=20)

login_name_label = tk.Label(login_user_frame, text="Name:", bg=bg_color, fg=label_color)
login_name_label.pack(pady=5)
login_name_entry = tk.Entry(login_user_frame, font=("Arial", 12))
login_name_entry.pack(pady=5)

login_pin_label = tk.Label(login_user_frame, text="PIN:", bg=bg_color, fg=label_color)
login_pin_label.pack(pady=5)
login_pin_entry = tk.Entry(login_user_frame, show="*", font=("Arial", 12))
login_pin_entry.pack(pady=5)

tk.Button(login_user_frame, text="Login", font=("Arial", 12), command=login_user, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=15)
tk.Button(login_user_frame, text="Back to Main Menu", font=("Arial", 12), command=show_main_menu, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)

# Transaction Frame
transaction_frame = create_frame_with_border(root, bg_color, frame_border_color)

tk.Label(transaction_frame, text="Transaction Menu", font=("Arial", 16, "bold"), bg=bg_color, fg=label_color).pack(pady=20)

balance_label = tk.Label(transaction_frame, text="", font=("Arial", 12), bg=bg_color, fg=label_color)
balance_label.pack(pady=10)

tk.Button(transaction_frame, text="Deposit", command=show_deposit, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)
tk.Button(transaction_frame, text="Withdraw", command=show_withdraw, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)
tk.Button(transaction_frame, text="Back to Main Menu", command=show_main_menu, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)

# Deposit Frame
deposit_frame = create_frame_with_border(root, bg_color, frame_border_color)

tk.Label(deposit_frame, text="Deposit Amount:", bg=bg_color, fg=label_color).pack(pady=10)
deposit_entry = tk.Entry(deposit_frame, font=("Arial", 12))
deposit_entry.pack(pady=5)
tk.Button(deposit_frame, text="Confirm Deposit", command=deposit_money, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)
tk.Button(deposit_frame, text="Back to Transaction Menu", command=show_transaction, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)

# Withdraw Frame
withdraw_frame = create_frame_with_border(root, bg_color, frame_border_color)

tk.Label(withdraw_frame, text="Withdraw Amount:", bg=bg_color, fg=label_color).pack(pady=10)
withdraw_entry = tk.Entry(withdraw_frame, font=("Arial", 12))
withdraw_entry.pack(pady=5)
tk.Button(withdraw_frame, text="Confirm Withdraw", command=withdraw_money, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)
tk.Button(withdraw_frame, text="Back to Transaction Menu", command=show_transaction, bg=button_color, activebackground=button_hover_color, relief="raised", width=20).pack(pady=10)

# Start the application
root.mainloop()
