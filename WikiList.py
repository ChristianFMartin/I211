import re, urllib.request, ssl, random, webbrowser

def wiki_list(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    body = re.findall('(?<=<body).+?(?=</body>)', lines, re.DOTALL)[0]
    hits = re.findall('(?<=href=").+?(?=")', body)
    wiki = [link for link in hits if "wiki" in link and ".org" not in link]
    return wiki

website = input("Where would you like to start?")
jumps = eval(input("How many jumps?"))

webbrowser.open(website)

for i in range(jumps):
    print("Jumping from:", website)
    pages = wiki_list(website)
    website = "http://en.wikipedia.org" + random.choice(pages)
    print("To:", website,"\n")
    webbrowser.open_new_tab(website)
    


    
    
    



