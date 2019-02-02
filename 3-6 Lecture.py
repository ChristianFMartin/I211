import xml.etree.ElementTree as ET

root = ET.parse("students.xml")

students = root.iter("Student")


##def id_find(num):
##    for student in students:
##        stu_id = student.find("id").text
##        stu_name = student.find("name/first").text + " " + student.find("name/last").text
##        
##        if num == stu_id:
##            return stu_name
##        
##    return "Not Found"
            


##print(id_find("0019846768"))
##print(id_find("0019846789"))
##print(id_find("0012345556"))
##        
    

def fee_find(name):
    root = ET.parse("students.xml")

    students = root.iter("Student")
    
    for student in students:
        stu_name = student.find("name/first").text + " " + student.find("name/last").text
        stu_fee = student.find("fees")

        if name == stu_name:
            return (stu_name + " owes " + stu_fee.text + " " + stu_fee.attrib['c'] + " " + stu_fee.attrib['units'])
    return "Not Found"

print(fee_find("Rose Dawson"))
print(fee_find("Jack Sparrow"))
print(fee_find("No Body"))



