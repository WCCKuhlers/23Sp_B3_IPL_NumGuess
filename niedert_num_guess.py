# number guessing game niedert

import math
from random import randint

print("Number guessing game niedert")

print("pick a number between 1 and 100")
print("the computer will randomly pick a number")
print("Try to guess the number within 10 attempts")
playerGuess = 0
ans = str(input ("are you ready to start? "))

while ans == "yes":
    def generator():
        return randint (1,100)
    num = generator()
    guess = 0
    won = 0
    while playerGuess != num and guess < 10:
        playerGuess = int(input("pick a number between 1 and 100: "))
        if playerGuess < num:
            guess = guess + 1
            print("number of guesses:", guess)
            print("HIGHER")
        elif playerGuess > num:
            guess = guess + 1
            print("number of guesses:", guess)
            print("LOWER")
    if playerGuess == num:
        print("correct!")
        print("the number was: " + str(num)
        won = won + 1
        print("number of games won: ", won)
        
    if guess == 10:
        print("you failed")
        print("the computer number was: " + str(num))
        ans = str(input ("do you wish to play again? "))
