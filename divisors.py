#Caleb Callaway
#2/28/18
#divisors.py- uses loops to list divisors


num = int(input("Enter a number: "))

for i in range (0, num+1):
    if num%i==0:
        print (i)