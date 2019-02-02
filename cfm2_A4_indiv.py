#Chrissi Martin Group 15
#Individual Assignment 4


#1.) You can find the Standard Documentation for Python in:


#2.)
##Algorithm:
##    show cwd
##    ask user input
##    find correct directory
##    show files
##    if (draft) in filename, change to (final)
##    show updated files

import os

def dir_choice():
    directs = [entry for entry in os.listdir(os.getcwd()) if os.path.isdir(entry)]

    print("Current Directories:\n", directs, "\n")
    choice = ""

    while choice not in directs:
        choice = input("Please select a valid directory: ")

    return choice
def dir_files():
    print("Files in the", os.path.basename(os.getcwd()), "directory:\n")
    files = os.listdir(os.getcwd())
    for item in files:
        if os.path.isfile(item):
            print(item)
            

def name_change():
    print()
    print("Updated files in the", os.path.basename(os.getcwd()), "directory:\n")
    files = os.listdir(os.getcwd())
    for file in files:
        os.rename(file, file.replace("(draft)", "(final)"))
        new_files = os.listdir(os.getcwd())
    for file in new_files:
        if os.path.isfile(file):
            print(file)


home = os.getcwd()
print(home)
folder = dir_choice()
os.chdir(os.path.join(os.getcwd() ,folder))
dir_files()
name_change()







