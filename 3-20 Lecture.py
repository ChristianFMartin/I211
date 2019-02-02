out = open("template2.html", "w")

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Google Link</title>
</head>
<body>
	<p>Paragraph 1</p>
	<p>Paragraph 2</p>
	<a href="http://www.google.com">This takes you to Google!</a>
	<table border=1>
	<tr>
		<td>Row 1, Col 1</td>
		<td>Row 1, Col 2</td>
	</tr>
	<tr>
		<td>Row 2, Col 1</td>
		<td>Row 2, Col 2</td>
	</tr>
</table>

</table>

</body>
</html>"""

out.write(html)
out.close()

print("Finished writing.")
