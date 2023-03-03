import math
from random import randint

print("Schilling Number Guess")
print("Pick a number between 1 and 100")
print("The computer will randomly select a number")
print("Try to guess the computer's number correctly")

playerGuess = 0
ans = str(input("Are you ready to start? Yes or No: "))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0

    while playerGuess!=num and guess < 10:
        playerGuess = int(input("Pick A Number Between 1 And 100"))
        if playerGuess < num:
            print("Your guess was too low. Enter a higher number this time.")
            guess = guess + 1
        elif playerGuess > num:
            print("Your guess was too high. Enter a lower number this time.")
            guess = guess + 1
    if playerGuess == num:
        print("The computer number was " + str(num))
        print("You guessed... " + str(playerGuess))
        print("Wait,  you actually got it? Impressive.")
        print("It took you", guess, "guesses though. Try for a better score.")
        ans = "not yes"
    if playerGuess != num and guess == 10:
        print("Game Over. You lost. Now, leave.")
        print("The computer number was " + str(num))
        print("Try harder next time.")
        ans = "not yes"
