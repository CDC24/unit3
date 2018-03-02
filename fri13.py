#Caleb Callaway
#3/1/18
#fri13.py- finds the next 10 Friday the 13ths


from datetime import date
from calendar import weekday


day = date.today().day
month = date.today().month
year = date.today().year

fris = 0

print ("These are the next 10 Friday the 13 dates:")

while fris<10:
    if weekday(year,month,13)==4:
        print (month,"- 13 -",year)
        month+=1
        fris=fris+1
        if month == 13:
            year +=1
            month = 1
    else:
        month +=1
        if month == 13:
                year +=1
                month = 1

