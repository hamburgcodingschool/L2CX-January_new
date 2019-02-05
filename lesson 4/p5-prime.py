import math

number = 12 # ask the user for a number later

# print(number % 2 == 0)
# print(number % 3 == 0)
# print(number % 4 == 0)
# print(number % 5 == 0)
# print(number % 6 == 0)

# counter = 0
# for i in range(2, number):
#     if number % i == 0:
#         counter += 1
#
# if counter == 0:
#     print("{} is a prime number".format(number))
# else:
#     print("{} is NOT a prime number".format(number))

isPrime = True
for i in range(2, math.ceil(math.sqrt(number) + 1)):
    if number % i == 0:
        isPrime = False
        break

if isPrime:
    print("{} is a prime number".format(number))
else:
    print("{} is NOT a prime number".format(number))