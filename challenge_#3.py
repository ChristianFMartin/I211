##Group 15
##must be used in repl.it

file = open('outbreaks.html', 'r')
html = file.read()
file.close()

from bs4 import BeautifulSoup

with open('outbreaks.html') as lines:
  soup = BeautifulSoup(lines,"html.parser")

list_2017 = soup.find_all("div", id = "tabs-787255-1")[0]

disease2017 = list_2017.find_all('a')

for i in disease2017:
  print(i.get_text())

list_2016 = soup.find_all("div", id = "tabs-787255-2")[0]

disease2016 = list_2016.find_all('a')

for i in disease2016:
  print(i.get_text())


