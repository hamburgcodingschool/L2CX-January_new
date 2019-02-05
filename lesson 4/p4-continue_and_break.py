

for i in range(1, 10):
    print(i)

    if i == 5:
        break #stops the loop no matter what else is going on...

print("-------- MY AWESOME SEPARATOR ----------")

for i in range(1, 10):

    if i % 4 == 0:
        continue #ignores the rest of the block and jumps back to the top of the loop

    print(i)
