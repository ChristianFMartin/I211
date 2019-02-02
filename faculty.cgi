#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb

string = "i211s18_cfm2" 		
password = "my+sql=i211s18_cfm2" 	

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
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
