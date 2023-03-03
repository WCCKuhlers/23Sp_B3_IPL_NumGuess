
# Number Guess Game

#import math
#from random import randint
#import random
#print ("Walser Number Guess")
#start_game = True
#
#
#guessesLeft = 10
#chosenNum = randint(1,100)
#playAns = int(input("The computer has chosen a number between 1 and 100 - try to guess it!"))
#playAgain = False
#
#while start_game:
#    if guessesLeft == 0:
#        print ("Out of guesses. You lose.")
#        start_game = False
#    if chosenNum == playAns:
#        print ("You guessed correctly! The number was", chosenNum)
#        start_game = False
#    if chosenNum > playAns:
#        guessesLeft = guessesLeft - 1
#        print ("Too low! You have", guessesLeft, "Guesses left!")
#        playAns = int(input("Guess again!"))
#    if chosenNum < playAns:
#        guessesLeft = guessesLeft - 1 
#        print ("Too high! You have", guessesLeft, "Guesses left!")
#        playAns = int(input("Guess again!"))
#    
#while start_game == False:
#    playAgain = str(input("Would you like to play again?"))
#    if playAgain == "yes":
#        playAgain = False
#        start_game = True
        
import math
from random import randint


print ("The computer will choose a number between 1 and 100. Try to guess it!")


playerGuess = 0
ans = str(input("Are you ready to start? yes or no"))

while ans == "yes":
    def generator():
        return randint(1,100)
    num = generator()
    guess = 0

    while playerGuess != num and guess < 10:
        playerGuess = int(input("Pick a number between 1 and 100"))
        if playerGuess < num:
            print("Too low! Try a higher number.")
            guess = guess + 1
        elif playerGuess > num:
            print("Too high! Try a lower number.")
            guess = guess + 1
    if playerGuess == num:
        print("You win! The number was", num)



























