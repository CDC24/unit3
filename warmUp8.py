#Caleb Callaway
#2/28/18
#warmUp8.py - finds sum of all numbers less than 100,000 that are divisible by 3, 10, and 17

total = 0
for i in range (0, 100001):
    if i%3==0 and i%10==0 and i%17==0:
        total += i
    i +=1
print (total)