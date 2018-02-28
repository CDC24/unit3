#Caleb Callaway
#2/28/18
#divisors.py- uses loops to list divisors


num = int(input("Enter a number: "))


print ("Divisors:")    
for i in range (1, num):
    if num%i==0:
        print (i)