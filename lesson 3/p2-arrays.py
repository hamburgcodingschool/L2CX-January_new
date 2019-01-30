
names = ["Helder", "Fabia", "Linda", "Leonie", "Carina", "Ivan", "Lexy"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
# print(names[6])

#print all elements with position on the left
#ex:
# 0: Helder
# 1: Fabia ...
counter = 0

while counter < len(names):
    #print(str(counter) + ": " + names[counter])
    print("{}: {}".format(counter + 1, names[counter]))
    counter += 1  # counter = counter + 1

