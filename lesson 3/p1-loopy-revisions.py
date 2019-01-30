# print all the numbers from 1 to 100
# add ! if multiple of 3
# add !! if multiple of 4
# add !!! if multiple of 3 and 4
# 1
# 2
# 3!
# 4!!
# 5
# 6!
# 7
# 8!!
# 9!
# 10
# 11
# 12!!!
# ...

# counter = 0
# while counter < 100:
#     counter = counter + 1
#     if counter % 12 == 0:
#         print(str(counter) + "!!!")
#     else:
#         if counter % 4 == 0:
#             print(str(counter) + "!!")
#         else:
#             if counter % 3 == 0:
#                 print(str(counter) + "!")
#             else:
#                 print(counter)


# counter = 0
# while counter < 100:
#     counter = counter + 1
#
#     if counter % 12 == 0:
#         print(str(counter) + "!!!")
#     elif counter % 4 == 0:
#         print(str(counter) + "!!")
#     elif counter % 3 == 0:
#         print(str(counter) + "!")
#     else:
#         print(counter)


counter = 0
while counter < 100:
    counter = counter + 1

    text = str(counter)

    if counter % 3 == 0:
        text = text + "!"
    if counter % 4 == 0:
        text = text + "!!"

    print(text)