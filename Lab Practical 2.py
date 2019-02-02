#Chrissi Martin

#Algorithm
##read webpage contents
##store page contents in string
##use regex to find news article
##print all news articles
##ask user for input
##find headine w/ that phrase

#bonus

#Code
import re, urllib.request, ssl, webbrowser, os

def web_site(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    headlines = re.findall('(?<="headline").+?(?=<)',lines)
    




    print("Searching:", url)
    print()
    print("A list of articles found on this site: ")
    for headline in headlines:
        print(os.path.basename(headline))
        

    print()
    article_search = input("Please enter a word to search for: ")
    for headline in headlines:
        if article_search in os.path.basename(headline):
            print(headline)

    
    



    
        



web_site("http://cgi.soic.indiana.edu/~dpierz/news.html")
