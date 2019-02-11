# create a program that fills an array with 5 numbers from 1 to 100
# SUGGESTION:
# step 1: create a random number from 1 to 100
# step 2: create a loop that runs 5 times
# step 3: make that loop create (and print for testing) 5 random numbers
# step 4: put those numbers in an array instead of printing them
# step 5: print the array

import random

def someRandomNumbers():

    myRandomNumbers = []
    for i in range(0, 5):
        n = random.randint(1, 100)
        myRandomNumbers.append(n)

    return myRandomNumbers

print(someRandomNumbers())