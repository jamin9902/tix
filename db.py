# File for SQLite3 database connection
# Documentation: https://docs.python.org/3/library/sqlite3.html

import sqlite3
import os

# Delete database file if it exists
if os.path.exists("db/trial.db"):
  os.remove("db/trial.db")

# Create database file
con = sqlite3.connect("db/trial.db")
cur = con.cursor()


############################################################################################################
# Create Static Event Table
cur.execute('''CREATE TABLE staticEventInfo(eventID, eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList)''')
# Insert a row of data
cur.execute("INSERT INTO staticEventInfo VALUES ('1', 'Bruce Springsteen and the E Street Band', 'Gillette Stadium', 'Foxborough', 'MA', 'US', '2023-08-24', '19:00:00', 'https://www.ticketmaster.com/bruce-springsteen-and-the-e-street-foxborough-massachusetts-08-24-2023/event/01005E4DD61A4439', '0')")
# Query the database and obtain data as Python objects
data = cur.execute("SELECT * FROM staticEventInfo")
print(data.fetchall())
############################################################################################################


############################################################################################################
# Create Web Scraped Event Table
cur.execute('''CREATE TABLE webScrapedEventInfo(eventID, sectionName, count, priceRange, inventoryType, accessibility, offerCodes, offerType)''')
# Insert a row of data
cur.execute("INSERT INTO webScrapedEventInfo VALUES ('1', 'Section 1', '100', '100-200', 'Standard', 'Standard', '12345', 'Standard')")
# Query the database and obtain data as Python objects
data = cur.execute("SELECT * FROM webScrapedEventInfo")
print(data.fetchall())
############################################################################################################


############################################################################################################
# Create User Table
cur.execute('''CREATE TABLE userInfo(userID, paymentLevel, favoritesList)''')
# Insert a row of data
cur.execute("INSERT INTO userInfo VALUES ('1', 'Standard', '0')")
# Query the database and obtain data as Python objects
data = cur.execute("SELECT * FROM userInfo")
print(data.fetchall())
############################################################################################################


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

