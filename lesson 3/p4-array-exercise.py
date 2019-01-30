numbers = [23, 12, 45, 11, 20, 50, 5]

# sum(numbers) is cheating in this particular exercise

total = 0
highest = numbers[0]
lowest = numbers[0]

for i in range(0, len(numbers)):
    #print(numbers[i])
    total += numbers[i]

    if numbers[i] > highest:
        highest = numbers[i]

    if numbers[i] < lowest:
        lowest = numbers[i]

avg = total / len(numbers)

print(total)
print(avg)
print(highest)
print(lowest)