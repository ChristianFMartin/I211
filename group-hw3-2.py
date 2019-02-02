import sqlite3

def createFacultyTable(cursor):
    SQL = """CREATE TABLE Faculty
        (FacultyID int(11) UNIQUE,
        Name varchar(25) NOT NULL,
        Title varchar(100) NOT NULL,
        Email varchar(30),
        Areas varchar(200),
        PRIMARY KEY (FacultyID));"""
    cursor.execute(SQL)

def insertFacultyTable(cursor):
    SQL = """INSERT INTO Faculty
        VALUES(
        (1, 'Jane Smith', 'Accountant', 'jsmith@gmail.com', 'Chicago'),
        (2, 'Ned Wright', 'HR Rep', 'nwright@gmail.com', 'Denver'),
        (3, 'Sarah Jones', 'Sales Rep', 'sjones@gmail.com', 'New York'),
        (4, 'Austin Powers', 'Accountant', 'apowers@gmai.com', 'Seattle'),
        (5, 'Jack Bower', 'Sales Rep', 'jbower@gmail.com', 'Austin'));"""
    cursor.execute(SQL)

db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()

##createFacultyTable(cursor)
##insertFacultyTable(cursor)
