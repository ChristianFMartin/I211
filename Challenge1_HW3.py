#Challenge 1 Group Homework 3
#Team 15


import sqlite3

def createPersonTable(cursor):
    SQL = """CREATE TABLE Person
            (PersonID varchar (10) UNIQUE,
            FirstName varchar (25) NOT NULL,
            LastName varchar (25) NOT NULL,
            Birth date NOT NULL,
            Age int DEFAULT 18);"""
    cursor.execute(SQL)
def createOtherTable(cursor):
    SQL = """CREATE TABLE Other
            (OtherID varchar (10) UNIQUE,
            Name varchar (25) NOT NULL,
            City varchar (25) NOT NULL,
            Birth date NOT NULL,
            Age int DEFAULT 18);"""
    cursor.execute(SQL)

def insertPerson(cursor, id_num, fname, lname, bdate, age=18):
    SQL = "INSERT INTO Person (PersonID, FirstName, LastName, Birth, Age)"
    SQL += "VALUES ('" + str(id_num) + "', '" + fname + "', '" + lname + "', '"
    SQL += bdate + "', " + str(age) + ");"
    cursor.execute(SQL)

db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()
#createPersonTable(cursor)
#createOtherTable(cursor)
#insertPerson(cursor, 1, 'Jack', 'Sparrow', '1745-04-01', 46)
db_con.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
results = cursor.fetchall()
for row in results:
    for item in row:
        print(item, "\t", end="")
    print()






