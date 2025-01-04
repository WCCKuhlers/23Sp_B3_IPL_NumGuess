# Number Guess Game smith
# Kuhlers test 010425
import math
from random import randint

print ("Smith Number Guess")
print ("Pick a number between 1 and 100")
print ("The computer will randomly pick a number")
print ("You are trying to guess the computer's number in ten tries")

playerGuess = 0
ans = str(input("Are you ready to start?"))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0

    while playerGuess!=num and guess < 10:
        playerGuess = int(input("pick a number betwwen 1 and 100: "))
        if playerGuess < num:
            print ("To low, please enter a higher number:")
            guess = guess
        elif playerGuess > num:
            print ("To high,please guess a lower number: ")
            guess = guess + 1
    if playerGuess == num:
        print ("You guess the number")
        print ("The computer number was" + str(num))
        print ("The player guess was" + str(playerGuess))
