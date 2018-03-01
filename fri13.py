#Caleb Callaway
#3/1/18
#fri13.py- finds the next 10 Friday the 13ths


from datetime import *
from calendar import weekday


day = date.today().day
month = date.today().month
year = date.today().year

print(weekday(year,month,day))