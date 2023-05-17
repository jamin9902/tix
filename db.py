# File for SQLite3 database connection
# Documentation: https://docs.python.org/3/library/sqlite3.html

import sqlite3
import os

db_location = "db/trial.db"

# Delete database file if it exists
if os.path.exists(db_location):
  os.remove(db_location)

# Create database file
try:
  con = sqlite3.connect(db_location)
  cur = con.cursor()
  print("Database created successfully")
except sqlite3.Error as error:
  print("Error while creating a sqlite table", error)


############################################################################################################
try:
  # Create Static Event Table
  cur.execute('''CREATE TABLE IF NOT EXISTS staticEventInfo(eventID, eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList)''')
except:
  print("Error while creating a sqlite table")

def insertStaticEventInfo(eventID, eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList):
  try:
    # Insert a row of data
    cur.execute("INSERT INTO staticEventInfo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (eventID, eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList))
    con.commit()
  except:
    print("Error while inserting into staticEventInfo table")

def printAllStaticEventInfo():
  try:
    # Query the database and obtain data as Python objects
    data = cur.execute("SELECT * FROM staticEventInfo")
    return data.fetchall()
  except:
    print("Error while selecting from staticEventInfo table")
############################################################################################################


############################################################################################################
try:
  # Create Web Scraped Event Table
  cur.execute('''CREATE TABLE IF NOT EXISTS webScrapedEventInfo(eventID, sectionName, count, priceRange, inventoryType, accessibility, offerCodes, offerType)''')
except:
  print("Error while creating a sqlite table")

def insertWebScrapedEventInfo(eventID, sectionName, count, priceRange, inventoryType, accessibility, offerCodes, offerType):
  try:
    # Insert a row of data
    cur.execute("INSERT INTO webScrapedEventInfo VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (eventID, sectionName, count, priceRange, inventoryType, accessibility, offerCodes, offerType))
    con.commit()
  except:
    print("Error while inserting into webScrapedEventInfo table")

def printAllWebScrapedEventInfo():
  try:
    # Query the database and obtain data as Python objects
    data = cur.execute("SELECT * FROM webScrapedEventInfo")
    return data.fetchall()
  except:
    print("Error while selecting from webScrapedEventInfo table")
############################################################################################################


############################################################################################################
try:
  # Create User Table
  cur.execute('''CREATE TABLE IF NOT EXISTS userInfo(userID, paymentLevel, favoritesList)''')
except:
  print("Error while creating a sqlite table")

def insertUserInfo(userID, paymentLevel, favoritesList):
  try:
    # Insert a row of data
    cur.execute("INSERT INTO userInfo VALUES (?, ?, ?)", (userID, paymentLevel, favoritesList))
    con.commit()
  except:
    print("Error while inserting into userInfo table")

def printAllUserInfo():
  try:
    # Query the database and obtain data as Python objects
    data = cur.execute("SELECT * FROM userInfo")
    return data.fetchall()
  except:
    print("Error while selecting from userInfo table")
############################################################################################################


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

