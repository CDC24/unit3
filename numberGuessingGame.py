#Caleb Callaway
#2/26/18
#numberGuessingGame.py- uses loops to make a number guessing game, prints out tries


from random import randint

num = randint (1,100)

i = 0

while True:
    i+=1
    guess= int(input("Guess a number from 1 to 100."))
    if guess == num:
        print ("You got it in",i,"guesses!")
        break
    elif guess > num:
        print ("Too high!")
    elif guess < num:
        print ("Too low!")
    else:
        print ("You did something wrong, son.")