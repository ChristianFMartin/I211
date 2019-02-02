#Chrissi Martin
#HW 1

#1.) Rock Paper Scissors Algorithm
#1) Ask user to input either rock,paper or scissors
#2) Randomly generate rock paper or scissors for computer choice
#3) Determine winner, or tie
    #-rock wins over scissors
    #-scissors win over paper
    #-paper wins over rock
    #-if same option is chosen by both user and computer, tie


#2.)Program that returns reverse input string
#ask user for string input
#strip sting into single values
#user reversed to change character positions

userData = input("Please enter a string: ")

print("".join(reversed(userData)))

#used information found in Python textbook and w3schools


#3.)
#create 2 empty lists
#ask user for 2 sets of data
#strip data into multiple single values
#remove commas
#append values into each empty list
#determine if lists contain any of the same data
userList1 = []
userList2 = []

userInfo1 = input("Please enter a series of characters, separated by commas.")
userInfo2 = input("Please enter a series of characters, separated by commas.")

userList1.append(userInfo1.split(","))
userList2.append(userInfo2.split(","))

print(userList1)
print(userList2)

counter = 0


for i in range(len(userInfo1)):
    if userInfo1[i] in userInfo2:
        true_or_false = "True"
    else:
        true_or_false = "False"



print(true_or_false)
    


