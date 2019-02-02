#Chrissi Martin
#Individual HW 2

#1.) Hangman Program

import random
word_list = ["learn","python","music","games","wonderful","podcast"]

word = random.choice(word_list)


##rep_word = ("-"*int(len(word)))


##while guess <= 10:
##    letter_guess = input("Please enter your guess: ")
##    if letter_guess in word:
##        letter_guess.replpace(

#print(word)

blanks = []
blanks.extend(word)

for i in range(len(blanks)):
    blanks[i] = "-"

print(' '.join(blanks))


count = 0
n_count = 0

#used stackoverflow for information on .extend()

while count < len(word):
    print("Incorrect Guess Count: ",n_count)
    guess = input("Please guess a letter. ")
    

    for i in range(len(word)):
        if word[i] == guess:
            blanks[i] = guess
            count += 1
    if guess not in word:
        n_count += 1
    print(''.join(blanks))
    
    if n_count >= 10:
        print("Sorry, you did not correctly guess the word.")
        break

print ("Good job! You guessed it!")


#2.)Rock, Paper, Scissors

rps_lst = ["rock","paper","scissors"]

rps_choice = random.choice(rps_lst)

rps_input = input("Please enter your choice: (rock, paper or scissors) ")

print("Your choice: ",rps_input," ","Computer choice: ",rps_choice)

if rps_input == rps_choice:
    print("Tie!")
else:
    if rps_input == "rock":
        if rps_choice == "paper":
            print("Paper covers rock. Computer wins.")
        elif rps_choice == "scissors":
            print("Rock crushes scissors. You win!")
    elif rps_input == "paper":
        if rps_choice == "rock":
            print("Paper covers rock. You win!")
        elif rps_choice == "scissors":
            print("Scissors cut paper. Computer wins.")
    elif rps_input == "scissors":
        if rps_choice == "rock":
            print("Rock crushes scissors. Computer wins.")
        elif rps_choice == "paper":
            print("Scissors cut paper. You win!")

    

                



