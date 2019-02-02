#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211s18_cfm2" 			#change this to yours
password = "my+sql=i211s18_cfm2"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage()
sort_by = form.getfirst('sort','songID')
html = """
<html>
    <head><title>Tune Shop</title></head>
    <body>
        <table border='1' width='80%'>
        <tr><th>SongID</th><th>Title</th><th>Artist</th><th>Genre</th><th>Price</th></tr>
        {content}
        </table>
    </body>
</html>"""
try:					#Always surround .execute with a try!
        SQL = "SELECT * FROM Songs ORDER BY " + sort_by +";"
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception as e:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "\nError:", e)
else:				#This runs if there was no error
        table = ""
        for row in results:
                table += "<tr>"
                for entry in row:
                    table += "<td  align='center'>" +str(entry)+ "</td>"
                table += "<td> <a href='Purchase.cgi?songid="+str(row[0])+"'>Buy</a></td></tr>" 
                table += "</tr>"
print(html.format(content = table))
