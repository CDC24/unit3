#Caleb Callaway
#3/1/18
#fri13.py- finds the next 10 Friday the 13ths


from datetime import date
from calendar import weekday


day = date.today().day
month = date.today().month
year = date.today().year

fris = 0

while fris<=10:
    if weekday(year,month,day)==4:
        if day == 13:
            print (year, month, day)
            month+=1
            fris+=1
            if month == 13:
                year +=1
                month = 1

