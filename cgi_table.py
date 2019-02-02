out = open("cgi_table.html","w")

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
        table+="<td>" +"Row "+[i]+", Col "+[j]+"</td>"
    table+="</tr>"
out.write(html.format(content=table))

out.close()

    
