#! /usr/bin/env python3
import cgi

print('Content-type: text/html\n')

form = cgi.FieldStorage()

item = form.getfirst('item','unknown item')
cost = form.getfirst('cost',0)
dev_m = form.getfirst('dev_m',10)
total_cost = int(cost)+int(dev_m)
total_cost = str(total_cost)
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
    <body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a <em>{0}</em> delivered by drone.</p>
<p>Your total comes to ${1}</p>
    </body>
</html>"""

print(html.format(item,total_cost))
