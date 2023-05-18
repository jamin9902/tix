from db_master import *


# Create Static Event Table
createTable("staticEventInfo", ["eventID", "eventName", "venue", "city", "stateCode", "country", "eventDate", "eventTime", "eventURL", "userTrackingList"])


def insertStaticEventInfo(eventID, eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList):
  try:
    cur.execute("INSERT INTO staticEventInfo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (eventID, eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList))
    con.commit()
  except:
    print("Error while inserting into staticEventInfo table")


def printAllStaticEventInfo():
  try:
    data = cur.execute("SELECT * FROM staticEventInfo")
    return data.fetchall()
  except:
    print("Error while selecting from staticEventInfo table")

def printStaticEventInfo(eventID):
  try:
    data = cur.execute("SELECT * FROM staticEventInfo WHERE eventID=?", (eventID,))
    return data.fetchall()
  except:
    print("Error while selecting from staticEventInfo table")


def updateStaticEventInfo(eventID, eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList):
  try:
    cur.execute("UPDATE staticEventInfo SET eventName=?, venue=?, city=?, stateCode=?, country=?, eventDate=?, eventTime=?, eventURL=?, userTrackingList=? WHERE eventID=?", (eventName, venue, city, stateCode, country, eventDate, eventTime, eventURL, userTrackingList, eventID))
    con.commit()
  except:
    print("Error while updating staticEventInfo table")
  

def deleteStaticEventInfo(eventID):
  try:
    cur.execute("DELETE FROM staticEventInfo WHERE eventID=?", (eventID,))
    con.commit()
  except:
    print("Error while deleting from staticEventInfo table")


def searchStaticEventInfo(searchString):
  try:
    data = cur.execute("SELECT * FROM staticEventInfo WHERE eventName LIKE ?", ('%' + searchString + '%',))
    return data.fetchall()
  except:
    print("Error while selecting from staticEventInfo table")

def sortStaticEventInfoByDate():
    try:
        data = cur.execute("SELECT * FROM staticEventInfo ORDER BY eventDate ASC")
        return data.fetchall()
    except:
        print("Error while selecting from staticEventInfo table")


closeDB();
