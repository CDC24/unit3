#Caleb Callaway
#3/5/18
#quiz3.py

i = -15
while i < -8:
    print (i)
    i +=1


for i in range (-15, -8):
    print (i)
    
    
total =0
for i in range (-100,1001):
    if i%2==0:
        total +=i
print (total)


while True:
    words = input("Enter something: ")
    if "alpaca" in words or "Alpaca" in words:
        break