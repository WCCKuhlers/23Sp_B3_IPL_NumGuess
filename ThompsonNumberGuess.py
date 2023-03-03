import math
from random import randint

print("Thompson Number Guess")
print("Pick a number between 1 and 100")
print("The computer will randomly select a number")
print("Try to guess the computer's number correctly")

playerGuess = 0
ans = str(input("Are you ready to start? yes or no: "))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0


    while playerGuess!=num and guess < 10:
        playerGuess = int(input("Pick a number between 1 and 100: "))
        if playerGuess < num:
            print("Too low, please guess a higher number: ")
            guess = guess + 1
        elif playerGuess > num:
            print("Too high, please guess a lower number: ")
            guess = guess + 1
    if playerGuess == num:
        print("You got the right number: ")
        print("The computer number was " + str (num))
        print("The player number was " + str (playerGuess))
    if playerGuess != num and guess == 10:
        print("Game Over. You lost. leave me now stinky.")
        print("The computer number was " + str(num))
        print("Try harder next time stinky.")
        ans = "not yes"
