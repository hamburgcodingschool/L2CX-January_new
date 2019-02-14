# 6 - Write a program that checks whether
# an number occurs in an array of numbers.

def existsInArray(needle, haystack):
    foundOne = False
    for number in haystack:
        if needle == number:
            foundOne = True
    return foundOne

l2cClass = ["Helder", "Fabia", "Leonie", "Carina", "Lexie"]
name = "Lexie"

# for i in range(0, len(numbers)):
#     print(numbers[i])

if existsInArray(name, l2cClass):
    print("IT EXISTS!")
else:
    print("IT DOES NOT!")


