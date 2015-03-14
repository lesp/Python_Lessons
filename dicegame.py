"""
Dice Game
"""

from random import randint
while True:
    play = input("Would you like to play a game?")
    if play == "yes":
        sides = int(input("How many sides on your dice? 4,6 or 12?"))
        if sides == 4 or sides == 6 or sides == 12:
            guess = randint(1,sides)
            print("The dice has rolled a",guess)
        else:
            print("Please choose the correct number of sides")
    else:
        print("Exit")
        break
    
