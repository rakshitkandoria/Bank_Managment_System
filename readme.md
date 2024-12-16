# Bank Management System
## Overview
The
**Bank Management System** 
is a simple, user-friendly application that allows users to perform basic banking operations such as creating a new account, logging into an existing account, depositing money, and withdrawing money. The application is built using **Python**, **Tkinter** for the GUI, and **MySQL** for the database.

## Features:
- Create a new user account.
- Log in to an existing user account using a PIN.
- Deposit money into the account.
- Withdraw money from the account.
- Display the current balance after transactions.
- Colorful and engaging user interface with vibrant colors.
## Requirements
Before running the application, you will need the following:

### 1. Python 3.x:
You can download and install Python from here.
### 2. Tkinter: 
Tkinter is a standard GUI library for '''Python''', which comes pre-installed with Python. However, if it's not installed, you can install it via the following command:
bash
Copy code
pip install tk
### 3. MySQL Server: 
This application uses MySQL to store user data (name, age, PIN, balance, etc.). You need to have MySQL installed and a database created for this project.
### 4. MySQL Connector:
You need the pymysql module to connect Python with MySQL. Install it using:
bash
Copy code
pip install pymysql
## Installation and Setup
### 1. Install MySQL: 
If you don't have MySQL installed, you can get it from the MySQL official website.

### 2. Create the Database:

- Open the MySQL shell or use any MySQL GUI (like phpMyAdmin or MySQL Workbench).
- Create a new database named user:
sql
Copy code
CREATE DATABASE user;
- Then, create a table table1 within this database to store the user data:
sql
Copy code
CREATE TABLE table1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    pin INT,
    state VARCHAR(100),
    gender VARCHAR(20),
    balance INT DEFAULT 0,
    account_no BIGINT
);
### 3. Update MySQL Credentials: 
Open the Python script and replace the MySQL connection details with your own.

python
Copy code
connection = pymysql.connect(
    host="localhost",
    user='root',
    password="your_password",  # Replace with your MySQL password
    cursorclass=pymysql.cursors.DictCursor,
    database="user"
)
### 4. Run the Application:

- After ensuring the database is properly set up, and all dependencies are installed, you can run the application.
- Simply execute the Python script from the terminal or your preferred IDE:
bash
Copy code
python bank_management_system.py
## Usage
### 1. Create a New User:
- Select the "New User" button from the main menu.
- Fill in the required details like Name, Age, PIN, State, and Gender.
- Click "Create User". A new account will be created with a unique account number, and the details will be stored in the database.
### 2. Log in as an Existing User:
- Select the "Login User" button from the main menu.
- Enter the Name and PIN of the user you wish to log in as.
- If the credentials are valid, you will be logged in and shown the transaction menu.
### 3. Transaction Menu:
- Once logged in, you will have options to either Deposit or Withdraw money.
- For each transaction, enter the amount and confirm the action.
- Your current balance will be displayed after each transaction.
### 4. Exit the Application:
- Click the "Exit" button in the main menu to close the application.
## Code Description
### Files:
- bank_management_system.py: Main Python script that contains the entire logic for creating users, logging in, depositing, and withdrawing money.
### Key Components:
- GUI: The graphical user interface (GUI) is built using the Tkinter library, with various frames for different sections like the main menu, new user creation, login, transactions, etc.
- MySQL Database: The application interacts with a MySQL database where user data is stored, such as user name, age, PIN, account number, and balance.
- Functions:
**create_new_user()**: Adds a new user to the database.
**login_user()**: Authenticates a user based on their name and PIN.
**deposit_money()**: Allows a logged-in user to deposit money into their account.
**withdraw_money()**: Allows a logged-in user to withdraw money from their account.
### Colors & Design:
- The application features a colorful and attractive interface with vibrant button colors and background themes.
- The design uses a light blue background and contrasting text and button colors to make it visually appealing.
## Screenshots
Below are screenshots of different screens in the Bank Management System application:

### 1. Main Menu Screen:

The main screen where the user can choose to create a new user, log in, or exit.

### 2. New User Creation:

The screen where a new user enters their details like Name, Age, PIN, etc., to create a new account.

### 3. Login Screen:

The screen where an existing user enters their Name and PIN to log in.

### 4. Transaction Menu:

The menu where the user can choose to deposit or withdraw money after logging in.

### 5. Deposit Screen:

The screen for depositing money into the account.

### 6. Withdraw Screen:

The screen for withdrawing money from the account.

#### Note: To use your own screenshots, save them in a folder named screenshots/ inside your project directory and replace the image file paths above accordingly.

## Troubleshooting
### 1. MySQL Connection Issues:
- Ensure that your MySQL server is running and accessible.
- Double-check your MySQL username and password in the script.
- Verify that the database and table have been created properly.
### 2. Dependencies Not Installed:
- Ensure all required dependencies (Tkinter and PyMySQL) are installed.
- Use the following commands to install them:
bash
Copy code
pip install tk
pip install pymysql
### 3. Error Messages:
- If you encounter any errors, read the error message carefully. Common issues include incorrect MySQL credentials, missing database or table, and missing dependencies.

