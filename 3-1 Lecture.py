import xml.etree.ElementTree as ET

root = ET.parse("students.xml")


##fnames = root.findall("Student/name/first")
##lnames = root.findall("Student/name/last")

students = root.iter("Student")

fee_counter = 0
for student in students:
    fee = student.find("fees")
    fee_counter += int(fee.text)
    
print("The total amount of student fees is: $",fee_counter)



##print("The sudents are: ")
##for student in students:
##    print(student.find("name/first").text, student.find("name/last").text)


##for elem in elements:
##    print("Tag Name: ",elem.tag)
##    print("Tag Text: ",elem.text)
##    print("Children: ",list(elem))
##    print("-"*20)

##print("The students are: ")
##for i in range(len(fnames)):
##    print(fnames[i].text,lnames[i].text)
        



