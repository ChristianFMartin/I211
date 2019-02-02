from bs4 import BeautifulSoup

file2 = open('degrees.html', 'r')
degrees = file.read()
soup2 = BeautifulSoup(degrees, 'html.parser')

degree_options = soup2.find_all('td')
for option in degree_options:
    print(option.a.string)
file2.close()
