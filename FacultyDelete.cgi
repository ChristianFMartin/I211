#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb, cgi
string = "i211s18_cfm2" 			#change this to yours
password = "my+sql=i211s18_cfm2"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage()
def results_table(records):
    html = """
    <!doctype html>
    <html>
    <head><meta charset="utf-8">
    <title>Faculty Add</title></head>
        <body>
            <h1>New Faculty Member Added!</h1>
            <table border='1' width='100%'>
            <tr><th>FacultyID</th><th>Name</th><th>Title</th><th>Email</th><th>Areas</th></tr>
            {content}
            </table>
            <p><a href="FacultyAdd.html">Go Back</a></p>
        </body>
    </html>"""

    table = ""
    for row in records:
            table += "<tr>"
            for item in row:
                table += "<td  align='center'>"+item+"</td>"
            table += "</tr>"
    print(html.format(content = table))
    form = cgi.FieldStorage()

name = form.getfirst("name", "")
title = form.getfirst("title", "")
email = form.getfirst("email", "")
areas = form.getfirst("areas", "")
    
#establish DB connection
string = "i211s18_cfm2" 	#change this to yours
password = "my+sql=i211s18_cfm2"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

SQL = "DELETE FROM Faculty WHERE FacultyID = " + FacultyID + ";"
cursor.execute(SQL)
db_con.commit()
