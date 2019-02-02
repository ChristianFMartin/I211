import urllib.request, re
page = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/cgi_tables.cgi")
out = page.read().decode(errors="replace")
page.close()

tbl = re.findall('(?<=<tr>).+?(?<=</tr>)',out,re.DOTALL)[0]
tbl_data = re.findall('(?<=<td>).+?(?<=</td>)',tbl,re.DOTALL)
data_lst = []

for data in tbl_data:
    data_lst.append(data)
print("Data loaded from file: ")
print(data_lst)

