#Number Guess Game Ben

import math
from random import randint
print("Bens Number Guess")
print("Pick a number between 1 and 100")
print("The computer will randomly select a number")
print("You are trying to guess the computer's number in ten tries")

playerGuess = 0
ans = str(input ("Are you ready to start, answer yes "))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0

    while playerGuess!=num and guess < 10:
        playerGuess = int(input("Pick a number between 1 and 100: "))
        if playerGuess < num:
                 print("too low, guess a higher number: ")
                 guess = guess + 1
        elif playerGuess > num:
                  print("Too high, guess a lower number: ")
                  guess = guess + 1
        if playerGuess == num:
                 print("you guessed the number: The number was " + str(num) + " and it took you " + str(guess) + " guesses")






        if guess == 10:
            print("you have exeeded the number of guesses, the computer number was "
                + str(num))
    
