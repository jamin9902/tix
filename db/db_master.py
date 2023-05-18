# File for SQLite3 database connection
# Documentation: https://docs.python.org/3/library/sqlite3.html

import sqlite3
import datetime

# Database file location
db_location = "db/trial.db"
con = None
cur = None


# Create database file (or connection if file exists)
def createDB():
  global con, cur
  try:
    con = sqlite3.connect(db_location)
    cur = con.cursor()
    print("Database created successfully")
  except sqlite3.Error as error:
    print("Error while creating or connecting to sqlite3 table", error)

  
# Close database connection
def closeDB():
  global con
  try:
    con.commit() # Save (commit) any changes made
    con.close() # Close connection
    print("Database connection closed successfully")
  except sqlite3.Error as error:
    print("Error while closing sqlite3 table", error)


# Delete database file if it exists
def deleteDB():
  import os
  if os.path.exists(db_location):
    os.remove(db_location)
    print("Database deleted successfully")
  else:
    print("Database does not exist")


# Create table
def createTable(tableName, *tableColumns):
  global cur
  
  # Create table columns string with commas separating each column
  cols = ""
  for col in tableColumns:
    cols += str(col) + ", "
  cols = cols[:-2] # Remove last comma and space

  try:
    cur.execute('''CREATE TABLE IF NOT EXISTS ''' + tableName + '''(''' + cols + ''')''')
    print("Table created successfully")
  except sqlite3.Error as error:
    print("Error while creating a sqlite3 table", error)


# Delete table
def deleteTable(tableName):
  global cur
  try:
    cur.execute('''DROP TABLE IF EXISTS ''' + tableName)
    print("Table deleted successfully")
  except sqlite3.Error as error:
    print("Error while deleting a sqlite3 table", error)


# Create Database
createDB();
