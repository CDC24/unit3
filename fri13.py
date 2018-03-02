#Caleb Callaway
#3/1/18
#fri13.py- finds the next 10 Friday the 13ths


from datetime import date
from calendar import weekday


day = date.today().day
month = date.today().month
year = date.today().year

for i in range 1-11):
    if weekday(year,month,day)==4:
        print (year, month, day)
    

