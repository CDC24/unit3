#Caleb Callaway
#2/15/18
#printStars.py - prints out many characters


num = int(input("Enter a number: "))

for i in range(1,  num+1):
    print (" "*(num-i)," *"*i)
