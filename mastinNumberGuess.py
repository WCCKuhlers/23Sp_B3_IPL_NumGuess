#Number Guess Game Mastin
import math
from random import randint
print("Number guessing game")
print("Pick a number between 1 and 100")
comNum=randint(1,100)
print("The computer will randomly pick a number")
print("Try to guess the number the computer chose")
playerGuess=0
ans=str(input("ARE YOU READY? y/n"))

while ans=="y":
    def generator():
        return randint(1,100)
    num = generator()
    guess=0

    while playerGuess!=num and guess<10:
        playerGuess=int(input("pick a number between one and a hundred:"))
        if playerGuess < num :
            print("Too low, guess higher")
            guess=guess+1
        elif playerGuess > num :
            print("Too high, guess lower")
            guess=guess+1
    if playerGuess==num:
        print("you guessed correctly")
        print("The number was: 4"+str(num))
    if guess==10:
        print("you exceeded 10 guesses!")
        print("The nnumber was: "+str(num))

    
