import urllib.request
import re
import os

webpage = urllib.request.urlopen("https://en.wikipedia.org/wiki/2017_in_film")

contents = webpage.read().decode(errors="replace")
webpage.close()


# '(?<=yes).+?(?=no)'
tables = re.findall('(?<=of 2017</caption).+?(?<=/table>)',contents,re.DOTALL)[0]

##print(tables)

movies = re.findall('(?<=<i><a href=")/wiki.+?(?=")',tables)
##print(movies)
print("Highest Grossing Movies of 2017")
print("-"*25)
for movie in movies:
    print(movie)
##'<tr>(.*?)</tr>'
print()
movie_choice = input("Please choose a movie from our list. ")

movie_page = urllib.request.urlopen("https://en.wikipedia.org"+movie_choice)

movie_contents = movie_page.read().decode(errors="replace")
movie_page.close()


movie_plot = re.findall('(?<=id="Plot">Plot</span>).+?(?<=<span class="mw-headline")', movie_contents, re.DOTALL)[0]

print(movie_plot)
