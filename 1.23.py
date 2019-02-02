##def squares(num):
##    squares_lst = [i*i for i in range(0,num + 1)]
##    return squares_lst
##
##print(squares(10))
##

##lower_b = int(input("Please enter a lower bound. "))
##
##upper_b = int(input("Please enter an upper bound. "))
##
##div = int(input("Please enter number to divide by. "))
##
##
##div_lst = [i for i in range(lower_b,upper_b + 1) if i % div == 0]
##
##print(div_lst)
file_name = input("Please enter a file name: ")
all_lines = [line.strip() for line in open("lines.txt","r")]

two_v_words = [word for line in all_lines for word in line.split("") if len([let for let in word if let in "aeiou"]) >= 2]

print("All lines in the file: ",all_lines)
print("The words in the file that contain 2 or more vowels: ", two_v_words)
                            

vowels = []
for letter in 'awesome':
    if letter in ['a','e','i','o','u']:
        vowels.append(letter)

print(vowels) # ['a', 'e', 'o', 'e']

# option 2 with list comprehension
# In this example, the first letter is the value that we want in the new list
# and the if portion is the filter step
vowels = [letter for letter in 'awesome' if letter in ['a','e','i','o','u']]
print(vowels) # ['a', 'e', 'o', 'e']

# Count of 3 letter words in a string
len([word for word in "the quick brown fox jumps over the lazy dog".split(" ") if len(word) == 3])

# figure out the length
    # for each word in the string "the quick brown fox jumps over the lazy dog" split(" ") into an array
        # if the length of each word is 3
