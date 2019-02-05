import random

randomNumber = random.randint(1, 100)

print("What's your guess?")
userNumber = int(input())

counter = 1
userWon = True
while userNumber != randomNumber:
    # check if the number is too high or too low
    # tell it to the user

    counter += 1

    if counter > 6:
        userWon = False
        break

    if userNumber > randomNumber:
        print("You're number is too high!")
    if userNumber < randomNumber:
        print("You're number is too low!")

    print("Try again:")
    userNumber = int(input())

if userWon:
    print("WHOOHOO! DONE!")
else:
    print("YOU SUCK USER!")