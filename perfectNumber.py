#Caleb Callaway
#3/1/18
#perfectNumber.py- determines whether or not something is a perfect number

num = int(input("Enter a number: "))

total=0
for i in range (1,num):
    if num%i==0:
        total+=i
print (total)

