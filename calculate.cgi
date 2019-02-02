#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()
html = """
<!doctype html>
<html>
    <head>
	   <meta charset="utf-8">
	   <title>Form in CGI</title>
    </head>
    <body>
	   <p>{content}</p>
    </body>
</html>"""
try:
    total=eval(form.getfirst('num1','0')) + eval(form.getfirst('num2','0'))
except:
    total = "Error, invalid numbers"

print(html.format(content ='Your total is: '+str(total)))

