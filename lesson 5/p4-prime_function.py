import math

#prime function receives the number to test as a paremeter
#returns a boolean (True/False) if the number is prime or not

def prime(number):

    for i in range(2, math.ceil(math.sqrt(number) + 1)):
        if number % i == 0:
            return False

    return True

# MAIN CODE
print("What is the number?")
userNumber = int(input())

if prime(userNumber):
    print("That is a prime")
else:
    print("No prime here")


for i in range(1, 101):
    if prime(i):
        print(i)