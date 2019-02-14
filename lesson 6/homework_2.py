# 2 - Modify the previous program such
# that only multiples of three or five are considered in the sum,
# e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

# (17) 3+5+6+9+10+12+15 = 60

userNumber = 17 # ASK THE USER FOR A NUMBER INSTEAD

total = 0
for i in range(1, userNumber + 1):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i

print(total)