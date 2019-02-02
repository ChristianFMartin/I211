import os
def directory_choice():
    
    home = os.getcwd()
    files = os.listdir(home)
    
    dirs = []
    print(files)


    for entry in files:
        if os.path.isdir(entry):
            print(entry)
            dirs.append(entry)
            print("Current directories: \n", dirs, "\n")
            choice = ""
            
            print(dirs)
            while choice not in dirs:
                choice = input("Please select a valid directory: ")

            return choice


folder = directory_choice()





        



