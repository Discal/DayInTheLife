# Dev: Marcus Jackson
# start date: 05/27/2023
# Description: Text-based RPG

import random
import time


def displayWelcome():
    print("\bWelcome To A Day In The Life")
    print()


def chooseResponse():
    response = " "
    while response != "1" and response != "2" and response != "3":  # Input validation
        response = (input("Choose your response: "))
    return response


def pathOneChoices():
    pathChoices = ["blah", "blah blah", "blah blah blah"]

    for number, letter in enumerate(pathChoices, start=1):
        print(number, letter)

    userChoice = chooseResponse()

    if userChoice == "1":
        print("you got to go blah")
        time.sleep(3)
        print("instant blah")
        print()
    else:
        print("time to blah")
        time.sleep(2)
        print("back to cuddling blah")
        print()








answer = input("Would you like to continue? (yes/no) ").lower().strip()
if answer == "yes":
    displayWelcome()
    time.sleep(5)
    print(
        "This is just a filler message for the moment, normally a detailed opening story would go here, "
        "but i'm too busy trying to actually figure out the coding part of this. Anyway, "
        "what do you want to do when you wake up?")
    pathOneChoices()
    time.sleep(3)
    print("That's always your favorite way to wake up! Welp, time to clock in to the old 9 to 5")
    time.sleep(2)
    print("I wonder how the first call will be")
else:
    print("Well, back to sleep I go")




#     print("1- Cup of coffee and trip to the Oval office")
#     print("2- Cuddled up with babe")
#     print("3- Morning workout routine")


#     #Path One      
#     if answer == 1: 
#         print("You bounce out of bed, pookie hat still on, make your way to the leasing office for coffee (yes, for free)")

#
