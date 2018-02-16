#Caleb Callaway
#2/15/18
#gauss.py - prints out sum of numbers in a range

start = int(input("Enter the beginning number of the range: "))
end = int(input("Enter the end number of the range: "))
space = int(input("Enter how much to go up by each time: "))

total = 0
for i in range (start, end+1):
    i+=space
    total = total+i
    if i == end:
        print (total)
