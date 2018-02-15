#Caleb Callaway
#2/15/18
#countdown.py - counts down to 0 and prints boom


num = int(input("Enter a number: "))

for i in range (-num, 0):
    print (-i)
    if i == -1:
        print ("BOOOM! GOT 'EM")
    