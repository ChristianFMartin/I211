#! /usr/bin/env python3

import cgi, random, MySQLdb

print('Content-type: text/html\n')

form = cgi.FieldStorage()

string = "i211s18_cfm2" 	#change username to yours!!!
password = "my+sql=i211s18_cfm2" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()
def get_weapon(cursor, winner):
    try:
        SQL="SELECT Weapon FROM Robot WHERE Name = '"+winner+"';"
        cursor.execute(SQL)
        weapon=cursor.fetchall()[0][0]
    except:
        weapon="something went wrong with SQL"
    return weapon


def deactivate(cursor, dead_bot):
    try:
        SQL="UPDATE Robot SET Active = 'False' WHERE Name = '"+dead_bot+"';"
        cursor.execute(SQL)
        db_con.commit()
    except:
        print("Row not deleted!")

def robot_fight(cursor,robot1,robot2):
    botlist=[robot1,robot2]
    winner=botlist.pop(random.randint(0,1))
    loser=botlist[0]
    output=winner+" wins the round with its "+get_weapon(cursor, winner)+'.<br>'
    output+=loser+" is now deactivated."
    deactivate(cursor,loser)
    return output

#main
html="""<html>
<head><title>Robot Fight!</title></head>"""
try:
    SQL = "SELECT Name FROM Robot;"
    cursor.execute(SQL)
    names = cursor.fetchall()
except Exception as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "Error:", e)
else:   #This runs if there was no error
    if not form.getfirst("robot1",None):
        html+="""<body>
            <H1>Choose two robots to face off!</H1><hr />
            <FORM method="post" action="robot_fight.cgi">
            <H3>Please select robots:</H3>
            <p> Robot Name:
            <select name="robot1">"""
        for name in names:
            html+="<option>"+name[0]+"</option>"
        html+="</select>"
        html+="""<select name="robot2">"""
        for name in names:
            html+="<option>"+name[0]+"</option>"
        html+="""</select></p>
    <input type="submit" value="Fight!" />
    </FORM>
    <hr />"""
    else:
        robot1=form.getfirst("robot1")
        robot2=form.getfirst("robot2")
        html+=robot_fight(cursor,robot1,robot2)
html+="""</body>
</html>"""
print(html)



