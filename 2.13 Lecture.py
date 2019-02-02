import urllib.request

web_page = urllib.request.urlopen("http://www.soic.indiana.edu/")
contents = web_page.read().decode(errors="replace")
print(contents)

web_page.close()

file_out = open("page.html","w",encoding="utf-8")
file_out.write(contents)
file_out.close()

print("All done! Open page.html in your browser!")
