import random

def myOwnChoiceFunction(list):
    pos = random.randint(0, len(list) - 1)
    return list[pos]

names = ["Helder", "Fabia", "Linda", "Leonie", "Carina", "Lexy"]

print(random.choice(names))
print(myOwnChoiceFunction(names))
