#! /usr/bin/env python3

import cgitb
cgitb.enable()
print('Content-type: text/html\n')

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Table</title>
</head>
<body>
        <table>{content}</table>
</body>
    
</html>"""

column = 10
row = 10
table=""
for i in range(row):
    table+="<tr>"
    for j in range(column):
        table+="<td>" +"Row "+str(i)+", Col "+str(j)+"</td>"
    table+="</tr>"

print(html.format(content=format))   
