# Number Guess Game Murtic

import math
from random import randint

print("""Murtic Number Guess Game
""")
print("Try to guess the number the computer will choose in between 1 and 100")

playerGuess = 0
com_num = randint(1,100)
for x in range(10):
    playerGuess = input("Pick a number \n")
    if int(playerGuess) > 100:
        print("Pick a number inbetween 1 and 100")
    if com_num == playerGuess:
        print("you guessed the right number")
        break
    else:
        print("You have", 10 - x, "amount of tries left")




    






