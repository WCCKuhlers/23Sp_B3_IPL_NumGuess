# Number Guess Game Velic

import math
from random import randint
import random

print("Velic Number Guessing Game")
print("Guess my number it is between 1 and 100")

playerans = int(input("Guess: "))
comans = random.randint(1,100)
guesses = 0

startgame = True
#while startgame and guesses < 10:
    #if comans == playerans:
        #print("You guessed my number, YOU WIN!")
        #startgame = False
    #else:
        #print("Nope thats not it")
        #guesses = guesses + 1
        #if playerans > comans:
            #print("But the number is less than", playerans)
        #else:
            #print("But the number is more than", playerans)
        #playerans = int(input("Guess: "))

#if guesses == 10:
    #print("You ran out of guesses")

    
while startgame and guesses < 10:
    if comans == playerans:
        print("You guessed my number, YOU WIN!")
        startgame = False
    else:
        print("Nope thats not it")
        guesses = guesses + 1
        if not guesses % 2 == 0:
            if playerans > comans:
                print("But the number is less than", playerans)
            else:
                print("But the number is more than", playerans)
            playerans = int(input("Guess: "))
        elif guesses % 2 == 0:
            playerans = int(input("Guess: "))
            
if guesses == 10:
    print("You ran out of guesses")
    print("The number was", comans)
       
