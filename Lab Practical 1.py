
passwords = [word.strip() for word in open("passwords.txt","r")]

show_list = [word for word in passwords]
#print("The current possible passwords are: \n", "-"*20 ,"\n",show_list)

clue_1 = [word for word in passwords if len(word) >= 6]
print("Clue 1: The password is at least 6 characters long")

print("The current possible passwords are: \n", "-"*20 ,"\n",clue_1)
print()
clue_2 = [word for word in clue_1 \
          if len([let for let in word if let in "abcdefghijklmnopqrstuvwxyz"]) >= 1]
#print(clue_2)
#Lecture 5 slides
print()
print("Clue 2: The password contains at least one letter.")
print("The current possible passwords are: \n", "-"*20 ,"\n",clue_2)
print()
##clue_3 = [word for word in clue_2 if [word[0] not in "aeiou" and word[1] in "aeiou"]]
clue_3 = []
for word in clue_2:
    if word[0] not in "aeiou" and word.lower()[1] in "aeiou":
        clue_3.append(word)
print()
print("Clue 3: The password does not start with a vowel, but the second character is a vowel.")
print("The current possible passwords are: \n", "-"*20 ,"\n",clue_3)         
#print(clue_3)
print()
clue_4 = [word for word in clue_3 if len([let for let in word.lower() if let not in "aeiou"]) >= 2* len([let for let in word.lower() if let in "aeiou"])]
print()
print("Clue 4: The password has at least twice as many consonants as vowels.")

print("The current possible passwords are: \n", "-"*20 ,"\n",clue_4)

###Bonus###

##clue_5 = []
##for word in clue_4:
##    for i in range(len(word)):
##        if word[i] == word[i+1]:
##            clue_5.append(word)
##clue_5 = [word for word in clue_4 if [let for let in word if [i for i in range(len(word))][let in word if let[i] == let[i+1]]]
##
##print(clue_5)



