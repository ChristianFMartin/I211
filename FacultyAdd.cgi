print('Content-type: text/html\n')

import MySQLdb,cgi

string = "i211s18_cfm2" 			#change this to yours
password = "my+sql=i211s18_cfm2"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage()
html = """
<html>
    <head><title>New Faculty Member Added</title></head>
    <body>
        <table border='1' width='30%'>
        <tr><th>FacultyID</th><th>Name</th><th>Title</th><th>Email</th><th>Areas</th></tr>
        {content}
        </table>
    </body>
</html>"""
name =form.getfirst('name')
title=form.getfirst('title')
email=form.getfirst('email')
areas=form.getfirst('areas')
try:
    SQL_insert= "INSERT INTO Faculty(Name,Title,Email, Areas) VALUES('"+str(name)+"','"+str(title)+"','"+str(email)+"','"+str(areas)+"');"
    SQL= "SELECT * FROM Faculty;"
    cursor.execute(SQL_insert)
    cursor.execute(SQL)
    results = cursor.fetchall()
except Exception as e:		#Here we handle the error
    print('<p>Something went wrong with the SQL Insert!</p>')
    print(SQL_insert, "\nError:", e)
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "\nError:", e)
else:				#This runs if there was no error
    table = ""
    for row in results:
        table += "<tr>"
        for entry in row:
            table += "<td  align='center'>" +str(entry)+ "</td>"
        table += "<td>Delete</td>"
        table += "<td> <a href='FacultyDelete.cgi'>Delete</a> </td>"
        table += "</tr>"
    print(html.format(content = table))

