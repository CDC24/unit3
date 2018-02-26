#Caleb Callaway
#2/26/18
#numberGuessingGame.py- uses loops to make a number guessing game, prints out tries


from random import randint

num = randint (1,10)

i = 0

while True:
    i+=1
    guess= input ("Guess a number from 1 to 100.")
    if guess == num:
        print ("you got it in",i,"guesses!")
        break