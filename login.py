import argparse
import os
import pyodbc

# initialize connection and cursor
serverName = "localhost\SQLEXPRESS"
dbName = "Practice"

cnxnStr = f'Driver={{ODBC Driver 17 for SQL Server}};Server={serverName};Database={dbName};Trusted_Connection=Yes;'

cnxn = pyodbc.connect(cnxnStr)

cursor = cnxn.cursor()

# prompt user for input
usernameInput = input("Enter username: ")

passwordInput = input("Enter password: ")

# attempt to find a login set that corresponds to both username and password provided
cursor.execute(f"SELECT * FROM Login WHERE Username='{usernameInput}' AND Password='{passwordInput}'")

loginRow = cursor.fetchone()

# check if login as successful
if loginRow != None:
    print(f"Login successful as user {loginRow[0]}")
else:
    print("Login failed. Please check that you entered the right credentials.")