import random

# prints a random number between 1 and 100 (both inclusive)

# n = random.randint(1, 100)
#
# print(n)

# let's generate 20 random numbers from 1 to 100
# count how many are higher than 50


counter = 0

for i in range(0, 20):
    randomNumber = random.randint(1, 100)

   # print(randomNumber)

    if randomNumber > 50:
        counter += 1 # counter = counter + 1
       # print("FOUND 1!")

    # print("-----------")

print("I counted " + str(counter) + " numbers higher than 50.")
print("I counted {} numbers higher than 50.".format(counter))