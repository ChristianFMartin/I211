#! /usr/bin/env python3
import sqlite3

print('Content-type: text/html\n')



	

db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()

try:				#Always surround .execute with a try!
        SQL = "SELECT * FROM Faculty;"
        cursor.execute(SQL)
        results = cursor.fetchall()
        SQL2 = "DESCRIBE Faculty;"
        cursor.execute(SQL2)
        results2 = cursor.fetchall()
except Exception as e:	#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
else:				#This runs if there was no error
        result = "'<table border='1' width='30%'>'"
        result += '<tr>'
        for column in results2:
       
            result += '<th>' + str(column[0]) + '</th>'
        result += '</tr>'
        for item in results:
            result += '<tr>'
            for i in range(len(item)):
                result += ' <td>' + str(item[i]) + '</td>'
            result += '</tr>'
        result += '</table>'    
        
        print(result)

updateName = input("Who would you like to update?")
updateTitle= input("Please enter new title.")
updateEmail= input("Please enter new email.")
updateArea= input("Please enter new areas.")

try:
    SQL = "UPDATE Faculty
    SET Name = 'updateName', Title = 'updateTitle', Email = 'updateEmail', Areas = 'updateArea'
    WHERE Name = 'updateName';"
    cursor.execute(SQL)
    db_con.commit()
except Exception as e:	#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
else:				#This runs if there was no error
        result = "'<table border='1' width='30%'>'"
        result += '<tr>'
        for column in results2:
       
            result += '<th>' + str(column[0]) + '</th>'
        result += '</tr>'
        for item in results:
            result += '<tr>'
            for i in range(len(item)):
                result += ' <td>' + str(item[i]) + '</td>'
            result += '</tr>'
        result += '</table>'

        print(result)
