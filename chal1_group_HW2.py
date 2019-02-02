from bs4 import BeautifulSoup

file = open('fbi.html', 'r')
fbi = file.read()
soup = BeautifulSoup(fbi, 'html.parser')

most_wanted = soup.find_all('h3')
for mw in most_wanted:
    print(mw.a.string)
file.close()
