"""
Currency Converter
"""
#This is a single line comment!!

from time import sleep
#Import the sleep function from the library time
print("Welcome to LesCo Currency Converter")
print("What currency do you wish to convert?")
print("Press 1 for USD")
print("Press 2 for CND")
choice = (int(input("Make your choice: ")))

if choice == 1:
    rate = float(input("Please enter the exchange rate: "))
    sleep(0.5)
    print("How many £ would you like to change to USD $?")
    sleep(0.5)
    gbp = float(input("Enter Value :> "))
    sleep(1)
    usd = (gbp * rate)
    print("£",gbp,"converts to","$",round(usd,2))
else:
    rate = float(input("Please enter the exchange rate: "))
    sleep(0.5)
    print("How many £ would you like to change to CND $?")
    sleep(0.5)
    gbp = float(input("Enter Value :> "))
    sleep(1)
    cnd = (gbp * rate)
    print("£",gbp,"converts to","$",round(cnd,2))


