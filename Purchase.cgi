#! /usr/bin/env python3

import cgi, random, MySQLdb

print('Content-type: text/html\n')

form = cgi.FieldStorage()
songid = form.getfirst("songid", "0")


string = "i211s18_cfm2" 	#change username to yours!!!
password = "my+sql=i211s18_cfm2" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

html = """
<html>
    <head><title>New Song Purchased</title></head>
    <body>
        {content}
        <form action='ViewSongs.cgi' method='get'>
            <h2> View My Songs </h2>
            <input type="radio" name="sort" value="Song">Title
            <input type="radio" name="sort" value="Artist">Artist
            <input type="radio" name="sort" value="Genre">Genre
            <p>
            <button type="submit">View Songs</button>
        </form>
    </body>
</html>"""
try:
    SQL_Purchase = "INSERT INTO MyTunes(SongID) VALUES("+ songid +");"
    cursor.execute(SQL_Purchase)
    db_con.commit()            
    SQL = "SELECT Artist,Song,Price FROM Songs WHERE songID=' " + songid+ "';"
    cursor.execute(SQL)
    results = cursor.fetchall()
except Exception as e:		#Here we handle the error
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "\nError:", e)
else:				#This runs if there was no error
    display = ""
    for song in results:
        display += "Thank you for purchasing " + str(song[0]) + "'s " + str(song[1]) + " for $" + str(song[2])
print(html.format(content = display))

