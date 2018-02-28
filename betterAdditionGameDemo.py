#Caleb Callaway
#2/28/18
#betterAdditionGameDemo.py - more loop practice- a better addition game

from random import randint

numCorrect = 0
while numCorrect <5:
    num1= randint (-10,10)
    num2= randint (-10,10)
    answer = input ("What is " + str(num1) + " + " +str(num2) + "? ")   #convert to str so it doesnt get confused\
    if answer == num1+num2:
     numCorrect+=1
    else:
        print ("You idiot! It was", num1+num2)