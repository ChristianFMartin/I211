main_list = []
headers = ["Name","Age","Hometown"]

for i in range(5):
    person_info = input("Please provide a name, age, and hometown, spearated by commas.")
    person_info = person_info.split(",")
    person_info[1] = int(person_info[1])
    person_info.insert(0,person_info.pop(1))
    main_list.append(person_info)

main_list.sort()

str_template = "{}\t{}\t{}"
print(str_template.format(headers[1],headers[0],headers[2]))

print("-"*40)

for item in main_list:
    print(str_template.format(item[1],item[0],item[2]))

    


##persons =[]
##for i in range(5):
##    name = input("Enter name \n")
##    age = input("Enter age \n")
##    hometown = input("Enter hometown \n")
##    person = [name,age,hometown]
##    persons.append(person)

##
##print(persons)
