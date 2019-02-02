##import re
##
##text_file = open('quote.txt','r')
##lines = text_file.read()
##text_file.close()
##
##print("Words beginning with a capital letter:", re.findall("[A-Z][\w]*", lines))
##print("Words ending in 'ing':", re.findall("[\w]*ing", lines))
##print("Words with two a's in them:", re.findall("[\w]*[a][\w]*[a][\w]*", lines))
##print("Phrases that begin and end with a comma:", re.findall("[,][\s\w]*[,]", lines))
##print("The number of words that begin with the letter 'v':", len(re.findall("[vV][\w]+", lines)))

import urllib.request
import re

link = "http://www.soic.indiana.edu/about/contact/index.html"
f = urllib.request.urlopen(link)
file = f.read().decode(errors = "replace")
f.close()

print("Searching: http://www.soic.indiana.edu/about/contact/index.html")
print("Found the following phone numbers:", re.findall("[(][\d]{3}[)] [[\d]{3}-[\d]{4}", file))
