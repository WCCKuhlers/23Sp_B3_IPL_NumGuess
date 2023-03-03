# Number guess Game Williams

import math
from random import randint

print("Williams Number Guess")
randNum = randint(1,100)
userNum = 0

for x in range(1,10):
    
    try:
        userNum = int(input("Pick a number between 1 and 100\nWhat is your guess? "))
    except ValueError :
        print("Please enter a valid number\n")

    while not userNum > -1 and not userNum < 101:
        try:
            userNum = int(input("Pick a number between 1 and 100\nWhat is your guess? "))
        except ValueError :
            print("Please enter a valid number\n")
        




        

    if userNum == randNum:
            (f"You won! the number you picked was {userNum}\n")

    else:
        print(f"you lost you have {10 - x} tries left\n")
        if not x % 2 == 0:
            greaterThanOrLessThan = 'less than' if userNum < randNum else 'greater than'
            print(f'your number is {greaterThanOrLessThan} the computer number')
            
            
            
