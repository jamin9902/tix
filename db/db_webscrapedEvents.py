from db_master import *


# Create Web Scraped Event Table
createTable("webScrapedEventInfo", ["eventID", "sectionName", "count", "priceRange", "inventoryType", "accessibility", "offerCodes", "offerType"])


def insertWebScrapedEventInfo(eventID, sectionName, count, priceRange, inventoryType, accessibility, offerCodes, offerType):
  try:
    cur.execute("INSERT INTO webScrapedEventInfo VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (eventID, sectionName, count, priceRange, inventoryType, accessibility, offerCodes, offerType))
    con.commit()
  except:
    print("Error while inserting into webScrapedEventInfo table")


def printAllWebScrapedEventInfo():
  try:
    data = cur.execute("SELECT * FROM webScrapedEventInfo")
    return data.fetchall()
  except:
    print("Error while selecting from webScrapedEventInfo table")


def searchWebScrapedEventInfo(eventID):
    try:
        data = cur.execute("SELECT * FROM webScrapedEventInfo WHERE eventID=?", (eventID,))
        return data.fetchall()
    except:
        print("Error while selecting from webScrapedEventInfo table")


closeDB();
