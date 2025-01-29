import argparse
import os
import pyodbc

# initialize connection and cursor
serverName = "localhost\SQLEXPRESS"
dbName = "Practice"

cnxnStr = f'Driver={{ODBC Driver 17 for SQL Server}};Server={serverName};Database={dbName};Trusted_Connection=Yes;'

cnxn = pyodbc.connect(cnxnStr)

cursor = cnxn.cursor()

# prompt user for option
done = False
while not done:
    optionInput = '0'
    while optionInput != '1' and optionInput != '2':
        print("Main Menu")
        print("1 - Login with Existing Account")
        print("2 - Create New Account")
        optionInput = input("Enter Option Number: ")
        
        if optionInput != '1' and optionInput != '2':
            print("Invalid input. Please try again.")

    if optionInput == '1':
        while not done:
            # prompt user for input
            usernameInput = input("Enter username: ")

            passwordInput = input("Enter password: ")

            # attempt to find a login set that corresponds to both username and password provided
            cursor.execute(f"SELECT * FROM Login WHERE Username='{usernameInput}' AND Password='{passwordInput}'")

            loginRow = cursor.fetchone()

            # check if login as successful
            if loginRow != None:
                print(f"Login successful as user {loginRow[0]}")
                done = True
            else:
                print("Login failed. Please check that you entered the right credentials.")

    elif optionInput == '2':
        done = False
        while not done:
            # prompt user for input
            usernameInput = input("Enter new username: ")

            passwordInput = input("Enter new password: ")

            passwordInput2 = input("Enter new password again: ")

            if passwordInput == passwordInput2:
                # attempt to find a login set that corresponds to username provided
                cursor.execute(f"SELECT * FROM Login WHERE Username='{usernameInput}'")

                loginRow = cursor.fetchone()

                # check if login already exists
                if loginRow == None:
                    cursor.execute(f"INSERT INTO Login (Username, Password) VALUES ('{usernameInput}','{passwordInput}')")
                    done = True
                else:
                    print(f"Username already in use by user {loginRow[0]}. Please choose a different username and try again.")
            else:
                print(f"Passwords do not match. Please try again.")
        
        # allow returning to the login screen after creating an account
        done = False
