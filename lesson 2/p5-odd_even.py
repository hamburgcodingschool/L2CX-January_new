# Print numbers from 1 to 100 with odd/even info
# 1 - Odd
# 2 - Even
# 3 - Odd
# ...
# 100 - Even

a = 0
while a < 100:
    a = a + 1
    if a % 2 == 0: # Even number
        print(str(a) + " - Even")
    else: # if not can only be Odd
        print(str(a) + " - Odd")