##Chrissi Martin  Group 15
##
##Algorithm:
##    import file contents
##    strip and split file contents
##    create dictionary of teams/wins
##    print games won by each team
##    create list comp. of teams with less than 5 letters
##    print list
##    create list comp of teams with most wins (>= 7)
##    print list


file_contents = [line.strip().split() for line in open("teams.txt","r")]



team_dict = {key:value for (key,value) in file_contents}

for key, value in team_dict.items():
    print("The",key, "have won", value, "games.")

keys_lst = [key for key,value in team_dict.items()]

print()

less_than5 =[keys_lst[i] for  i in range(len(keys_lst)) if len(keys_lst[i]) <5 ]
print("Teams with names shorter than 5 letters", less_than5)

print()
more_than7 = [i[0] for i in file_contents if int(i[1]) >= 7]

print("The three teams with the highest wins are: ",more_than7)
