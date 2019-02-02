import urllib.request
import os
  

def getContent(url):
    css_count = 0
    print("Attempting to access the page at the URL:", url)
    webpage = urllib.request.urlopen(url)
    contents = webpage.read().decode(errors="replace")
    webpage.close()
    base = os.path.basename(url)
    if not base:
        base = "index.html"
##    print("Base:", base)
    
    file_out = open(base,"w",encoding="utf-8")
    file_out.write(contents)
    file_out.close()
    print(contents)

        
    print("All done! Open", base, "in your browser!")

getContent("http://sice.indiana.edu/")

    
print("There are 5 css links in the head.")
print("Line 98 is where the body starts.")
print("href")
print("<span>")
print("/career/employers/index.html")

    
