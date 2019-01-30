#ask the user for a number and show the times table for that number
# ex: 7
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70

print("Give me a number:")
userNumber = int(input())

counter = 0

while counter < 10:
    counter = counter + 1
    result = userNumber * counter
    #print(str(userNumber) + " x " + str(counter) + " = " + str(result))
    print("{} x {} = {}".format(userNumber, counter, result))