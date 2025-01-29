import argparse
import os
import pyodbc

serverName = "localhost\SQLEXPRESS"
dbName = "Practice"

cnxnStr = f'Driver={{ODBC Driver 17 for SQL Server}};Server={serverName};Database={dbName};Trusted_Connection=Yes;'

print(f"cnxnStr: {cnxnStr}")

cnxn = pyodbc.connect(cnxnStr)

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Login')

for row in cursor:
    print('row = %r' % (row,))

print("Yep, that sure is some text")

inputVal = input("Enter something: ")

print(f"You entered: {inputVal}")