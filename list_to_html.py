data = [["Item", "Cost", "Type"], ["Coke", "$2", "Drink"],
        ["Water", "$0", "Drink"], ["Fries", "$4", "Appetizer"],
        ["Onion Rings", "$3", "Appetizer"], ["Steak", "$12", "Entree"],
        ["Chicken", "$8", "Entree"], ["Caesar Salad", "$7", "Entree"]]

        
out = open("html_table.html", "w")

html = """<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Table</title>
</head>
<body>

	<table>(content)</table>

</table>

</body>
</html>"""
table=""
for sublist in data:
    table+="<tr>"
    for elem in sublist:
        table+="<td>"+ str(elem) + "</td>"
    table+="</tr>"


out.write(html)
out.close()

print("Finished writing.")
