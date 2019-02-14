# 3 - Write a program that asks the user for a number n
# and gives them the possibility to choose between
# computing the sum and computing the product of 1,…,n.


print("Hello Mr. User what is your number?")
userNumber = int(input())

print("Would you like to know the (s)um or (p)roduct of numbers 1 to " + str(userNumber))
type = input()

if type == "s":
    print("let's sum")
    total = 0
    for i in range(1, userNumber + 1):
        total = total + i
    print(total)
else:
    print("let's multiply")
    product = 1
    for i in range(1, userNumber + 1):
        product = product * i
    print(product)