# have the computer generate a random number between 1 and 100
# The user will have 10 guesses to guess the computers number
# After each guess the computer will tell the user if the number is
# too high or too low

import math
from random import randint

print("Winders Number Guess")
print("Pick a number between 1 and 100")
print("The computer will randomly select a number")
print("You are trying to guess the computer's number in 10 tries")

playerGuess = 0
ans = str(input ("Are you ready to start, answer yes  "))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0

    while playerGuess!=num and guess <10:
        playerGuess = int(input("Pick a number between 1 and 100"))
        if playerGuess < num:
            print("Too low, guess a higher number:  ")
            guess = guess + 1
        elif playerGuess > num:
            print("Too high, guess a lower number:  ")
            guess = guess + 1
        if playerGuess == num:
            print("You guessed the number:  The number was " + str(num) + " and it took you " + str(guess) + " guesses")




        if guess ==10:
            print("You have exceeded the number of guesses, the computer number was " + str(num))
