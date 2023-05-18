from db_master import *


# Create User Table
createTable("userInfo", ["userID", "paymentLevel", "favoritesList"])


def insertUserInfo(userID:int, paymentLevel, favoritesList):
  try:
    cur.execute("INSERT INTO userInfo VALUES (?, ?, ?)", (userID, paymentLevel, favoritesList))
    con.commit()
  except:
    print("Error while inserting into userInfo table")


def deleteUserInfo(userID:int):
  try:
    cur.execute("DELETE FROM userInfo WHERE userID=?", (userID,))
    con.commit()
  except:
    print("Error while deleting from userInfo table")


def printAllUserInfo():
  try:
    data = cur.execute("SELECT * FROM userInfo")
    print(data.fetchall())
  except:
    print("Error while selecting from userInfo table")


def printUserInfo(userID):
    try:
        data = cur.execute("SELECT * FROM userInfo WHERE userID=?", (userID,))
        return data.fetchall()
    except:
        print("Error while selecting from userInfo table")


insertUserInfo(2, "free", "test");
deleteUserInfo(1);
printAllUserInfo();

closeDB();
