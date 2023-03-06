# Number Guess Game Stine
import math
from random import randint

print("Stine Number Guess")
print("Pick a number between 1 and 100")
print("The computer will randomly pick a number")
print("Try to guess the number the computer chose")

playerGuess = 0
ans = str(input("Are you ready to start?"))

while ans == "yes":
    def generator():
        randint(1,100)
    num = generator()
    guess = 0

    while playerguess!=num and guess < 10:
        playerGuess = int(input("Pick a number between 1 and 100"))
        if playerGuess <num:
            print("Too low, guess a higher number: ")
            guess = guess + 1
        elif playerGuess > num:
            print ("Too high, guess a lower number: ")
            guess = guess + 1
    if playerGuess = num:
        print ("You guessed the number: The number was " + str(num) + " and it took you " + str(guess) + " guesses"
            


    if guess == 10
        print ("You have exceeded the number of guesses, the computer  number was " + str(num))
