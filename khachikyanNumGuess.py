# Number Guess Game Khachikyan

import math
from random import randint

print("Khachikyan Number Guess")
print("Pick a number between 1 and 100")
print("The computer will randomly pick a number")
print("Try to guess the number the computer chose")

playerGuess = 0  # user entered number
ans = str(input ("Are you ready to start?"))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0  # number of tries (guesses)

    while playerGuess!=num and guess < 10:
        playerGuess = int(input("Pick a number between 1 and 100: "))
        if playerGuess < num:  #condition tested 
            print("Too low, please guess a higher number:  ")
            guess = guess + 1
        elif playerGuess > num: #condition tested
            print("Too high, please guess a lower number:  ")
            guess = guess + 1
    if playerGuess == num:
        print("You guessed the number!")
        print("The computer number was " + str(num))
        print("The player number was " + str(playerGuess))
    if guess == 10:
        print("You exceeded 10 guesses!")
        print("The computer number was " + str(num))
            
