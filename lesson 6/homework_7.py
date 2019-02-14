# 7 -  Write a program that prints the names on odd positions in an array of names.

l2cClass = ["Helder", "Fabia", "Leonie", "Carina", "Lexie"]

for i in range(0, len(l2cClass)):
    name = l2cClass[i]
    if i % 2 != 0:
        print("{}: {}".format(i, name))

