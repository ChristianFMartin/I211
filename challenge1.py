from bs4 import BeautifulSoup

file = open('fbi.html', 'r')
html = file.read()
file.close()
soup = BeautifulSoup(html, 'html.parser')

criminals = soup.find_all("h3")
for criminal in criminals:
    print(criminal.a.string)
