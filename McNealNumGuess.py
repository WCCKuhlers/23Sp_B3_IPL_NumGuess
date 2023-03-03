# Number Guess Game McNeal

import math
from random import randint

print("McNeals Number Guess")
print("pick a number between 1 and 100")
print("The computer will pick a random number")
print("try to guess the number the computer chose")

playerGuess = 0 #num player guessed
ans = str(input("Are you ready to start? if so type yes"))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0 #num of guesses

    while playerGuess!=num and guess < 10:
        playerGuess = int(input("Pick a number between 1 and 100: "))
        if playerGuess < num: 
            print("Too low! try again!")
            guess = guess + 1
        elif playerGuess > num:
            print("Too high! try again!")
            guess = guess + 1
        if playerGuess == num:
            print("Correct!")
            print ("the computers number was " + str (num))
            print ("the players number was " + str (playerGuess))

        if guess == 10:
            print("You exceeded 10 guesses!")
            print ("the computers number was " + str (num))


