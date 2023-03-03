# number guess game linderbaum

import math
from random import randint
import random

print("Linderbaum Number Guess")
print("The computer will randomly pick a number 1-100, try to guess the number")

playerans = int(input("Guess: "))
comans = random.randint(1,100)
guesses = 0

startgame = True
while startgame and guesses < 10:
    if comans == playerans:
        print("You win")
        startgame = False
    else:
        guesses = guesses + 1
        if playerans > comans and guesses % 2 != 0:
            print("Wrong, Less")
        elif playerans < comans and guesses % 2 != 0:
            print("Wrong, More")
        else:
            print("Wrong")
        playerans = int(input("Guess: "))

if guesses == 10:
    print("Wrong, you ran out of guesses")
    print("The correct answer was:", comans)
    

