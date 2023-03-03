#  Number Guess Game Mendoza v2

import math
from random import randint
import random
start_game = True
playerGuesses = 0

print ("Mendoza Number Guess Game")
print ("- The computer will randomly pick a number between 1 and 100")
print ("- Your goal is to try and guess the number that the computer chose")
print ("- You have 10 tries to guess the computers number before it's game over")
print (" ")
computerNum = randint(1,100)

while start_game:
    playerGuess = str(input("Pick a number between 1 and 100 "))
    playerGuessNum = int(playerGuess)

    if computerNum == playerGuessNum:
        print("You guessed the computer's number!", "(", computerNum, ")")
        playerRespWin = str(input("Would you like to play again? yes or no "))
        if playerRespWin == "yes":
            startGame = True
            print(" ")
            print("Mendoza Number Guess Game")
            print("- The computer will randomly pick a number between 1 and 100")
            print("- Your goal is to try and guess the number that the computer chose")
            print("- You have 10 tries to guess the computers number before it's game over")
            print(" ")
        else:
            start_game = False
    else:
        print("You did not guess the computer's number")
        playerGuesses = playerGuesses + 1
            
    if computerNum < playerGuessNum:
        print("The number you guessed it too high! Hint: Pick a lower number")
        print(" ")

    if computerNum > playerGuessNum:
        print("The number you guessed is too low! Hint: Pick a higher number")
        print(" ")
    
    if playerGuesses == 11:
        start_game = False
        print("Game over, you did not guess the computer's number after 10 guesses")
        print("The computer's number was", computerNum)
        playerRespLoss = str(input("Would you like to play again? yes or no "))
        if playerRespLoss == "yes":
            startGame = True
            print(" ")
            print("Mendoza Number Guess Game")
            print("- The computer will randomly pick a number between 1 and 100")
            print("- Your goal is to try and guess the number that the computer chose")
            print("- You have 10 tries to guess the computers number before it's game over")
            print(" ")
        else:
            start_game = False

    
    

