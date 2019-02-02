#Algorithm
#create function
#set my_pass equal to valid_pass
#if pass is 8+ char prints that it's valid
#if under 8 char, pass not valid
    #loop if not valid pass
#print your valid password is:

##def valid_pass(): 
##    while True:
##        my_pass = input("Please enter your password: ")
##        if len(my_pass) >= 8:
##            return my_pass
##        else:
##            print("Password entered not valid.")
##
##my_pass = valid_pass()
##
##print("Your valid password is: ",my_pass)

#algorithm
#create empty dict & list
#ask user input
#strip data and append into list
#create if statement to sort data
#sorted list
#def key = # of times int appears in dict
#print results

number_dict = {}
numbers_list = [1,2,2,3]

##numbers = input("Please enter a series of numbers between 1 and 10, separated by a comma. ")
##
##numbers_list.append(numbers.split(","))
##
##sorted(numbers_list)

def list_count():
    for i in numbers_list:
        print(i)
        numbers_list.count(i)
        number_dict[int(i)] = numbers_list.count(i)

list_count()
print(number_dict)





    
