##Chrissi Martin Team 15 
###1
##Algorithm:
##    import xml.etree.ElementTree as ET
##    create root
##    find tags w/in root
##    set bookid,title,author,price equal to tags
##    if tag matches bk_id entered return title, author, price
##    else return "not found"
##2
##Algorithm:
##    find title,price,author,genre
##    if genre = computer
##    print title,author,price

##3
##Algorithm:
##    create genre list
##    add genre to list unless genre already in list
##    print genre list
import xml.etree.ElementTree as ET

books = root.iter("book")

def display_book(book_id):
    root = ET.parse("library.xml")

    books = root.iter() 
    for book in books:
        title = book.find("catalog/book/title")
        author =  book.find("catalog/book/author")
        price = book.find("catalog/book/price")

        if book_id in book.attrib:
            return(title.text + "/n" + author.text + "/n" + price.text)
    return "Not Found"

print(display_book("bk107"))

for book in books:
    title = book.find("title")
    author =  book.find("author")
    price = book.find("price")
    genre = book.find("genre").text


    if genre == "Computer":
        print(title.text + " " + author.text + " " + price.text)

genre_list = []
root = ET.parse("library.xml")
books = root.iter("book")
for book in books:
    genre = book.find("genre").text
    if genre not in genre_list:
        genre_list.append(genre)
print(genre_list)




