#Chrissi Martin Team 15
#1.) since %A repesents the day of the week as a full name,
#not a two digit number.

## 2.) Algorithm:
##    import csv and datetime
##    read shop records csv and create variable
##    create list for weekend days
##    find what day of week item was sold
##    if the item sold on weekends, print it
    
#3.)

import csv
import datetime


shop_data = csv.DictReader(open("shoprecords.csv","r"))
weekend = ["Saturday","Sunday"]

for entry in shop_data:

#stackoverflow to help find weekday of sale

    date = entry["Date"]
    day, month, year = (int(x) for x in date.split('/'))    
    result = datetime.date(year, day, month)
    day_of_wk = (result.strftime("%A"))
##    print(entry["Item"], "was sold on", entry["Date"], ", a", day_of_wk)
    if day_of_wk in weekend:
        print(entry["Item"])
    
