"""
Roleplaying Character Generator
"""

from random import randint
from time import sleep

print("RPG Character Generator v1")
print("What class would you like to be?")
print("Press 1 for Elf")
print("Press 2 for Warrior")
print("Press 3 for Halfling")
print("Press 4 for Amazon")
choice = int(input("Who do you choose? "))
sleep(1)
if choice == 1:
    print("You have chosen the Elf class a wise and powerful choice")
    hp = randint(1,100)
    mp = randint(1,20)
    dex = randint(1,10)
    print("Your character has",hp,"hit points",mp,"magic points and",dex,"dexterity")
elif choice == 2:
    print("You have chosen the Warrior class, a powerful figher, yet lacking intelligence")
    hp = randint(1,100)
    mp = randint(1,20)
    dex = randint(1,10)
    print("Your character has",hp,"hit points",mp,"magic points and",dex,"dexterity")
elif choice == 3:
    print("You have chosen the Halfling, what a shame")
    hp = randint(1,100)
    mp = randint(1,20)
    dex = randint(1,10)
    print("Your character has",hp,"hit points",mp,"magic points and",dex,"dexterity")
else:
    print("The Amazon are a proud a noble clan, but forget to pay their taxes")
    hp = randint(1,100)
    mp = randint(1,20)
    dex = randint(1,10)
    print("Your character has",hp,"hit points",mp,"magic points and",dex,"dexterity")


