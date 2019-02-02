#Chrissi Martin Team 15

#1
#fox hex code:
#     hexcode = re.findall('(#[A-Fa-f0-9]{6})',lines)

##Algorithm:
##    read webpage contents
##    find wins and losses in one list
##        L or W followed by 2 sets of two numbers
##    count the amount of wins
##    count amount of losses
##    return counts
##    #Bonus Algorithm
##    remove the W or L for each entry in list
##    split both scores into two separent entries w/in own list
##    convert both scores into integers
##    subtract scores
##    return score difference
##    total score differences
##    


#Code
import re, urllib.request, ssl

def win_loss(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    lines = web_page.read().decode(errors="replace")
    web_page.close()

    
    wins_lose = re.findall('([A-Z][" "][\d]{2}-[\d]{2})', lines)
    win_count = 0
    loss_count = 0
    total_differences = 0


    
    for game in wins_lose:
        if "W" in game:
            win_count += 1
        if "L" in game:
            loss_count += 1     
##Bonus##
        differences = game.replace("W ", "")
        dif = differences.replace("L ", "")
        scores = dif.split("-")
        a = scores[0]
        b = scores[1]
        a = int(a)
        b = int(b)
        if a < b:
            dif = (b - a)
        else:
            dif = (a - b)
        total_differences += dif


            
        
##    print(wins_lose)
    print("Wins: ",win_count)
    print("Losses: ",loss_count)
    print()
    print("Bonus:")
    print("Total Difference: ",total_differences)






win_loss("http://cgi.soic.indiana.edu/~dpierz/mbball.html")

