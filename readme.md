# Bank Management System 🏦💻

Welcome to the **Bank Management System**! This is a Python-based application that simulates a basic banking system, allowing users to create accounts, log in, deposit, withdraw funds, and view their balance. The application is built using **Tkinter** for the GUI and **MySQL** as the database backend.

## Features 🚀

- **New User Registration** ✨: Create a new bank account with unique account numbers.
- **User Login** 🔒: Secure login with PIN authentication.
- **Transactions** 💰: Deposit and withdraw money easily.
- **Account Balance Display** 📊: Check your current account balance.
- **GUI Interface** 🖥️: Easy-to-use graphical interface.

## Requirements 📋

- Python 3.x
- Tkinter (comes pre-installed with Python)
- MySQL Server
- `pymysql` Python library

## Installation 🛠️

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required Python package:
   ```bash
   pip install pymysql
   ```

3. Set up the MySQL database:
   - Create a database named `user`.
   - Create a table `table1` with the following schema:
     ```sql
     CREATE TABLE table1 (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(255),
         age INT,
         pin INT,
         state VARCHAR(255),
         gender VARCHAR(50),
         balance FLOAT DEFAULT 0,
         account_no BIGINT UNIQUE
     );
     ```

4. Update the MySQL credentials in the code:
   ```python
   connection = pymysql.connect(
       host="localhost",
       user='root',
       password="your-password",  # Replace with your MySQL password
       cursorclass=pymysql.cursors.DictCursor,
       database="user"
   )
   ```

5. Run the application:
   ```bash
   python main.py
   ```

## Usage Instructions 📘

1. **Start the Application**:
   - Launch the program, and you will see the main menu.
2. **New User Registration**:
   - Click "New User" to create an account.
   - Fill in the required details, and you will receive a unique account number.
3. **Login**:
   - Click "Login User," enter your name and PIN to log in.
4. **Transactions**:
   - Deposit or withdraw money after logging in.
   - Check your account balance in the transaction menu.
5. **Exit**:
   - Click "Exit" to close the application.

## Screenshots 📸

### Main Menu
<img width="333" alt="image" src="https://github.com/user-attachments/assets/c72d1853-d630-4fa2-950b-fd7bbaa3b236" />

### New User Registration
<img width="227" alt="image" src="https://github.com/user-attachments/assets/e371ff97-41c0-4bc2-a8f4-59a7ea6046ca" />

<img width="187" alt="image" src="https://github.com/user-attachments/assets/7ad34713-cdc5-4339-8564-a935a33f0047" />


### Transactions
<img width="176" alt="image" src="https://github.com/user-attachments/assets/a8781158-5ba0-428b-8314-ffaaf38e1c1b" />

<img width="207" alt="image" src="https://github.com/user-attachments/assets/2fc9f6bd-04b7-4f53-8ed1-8dfe814db5bc" />

## Troubleshooting 🛠️

- Ensure the MySQL server is running.
- Verify that the database and table are created correctly.
- Check that the MySQL credentials in the script match your setup.
- Use Python 3.x to avoid compatibility issues.


