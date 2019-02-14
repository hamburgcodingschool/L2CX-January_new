# for userNumber in range(1, 13):
#
#     for i in range(1, 11):
#         res = userNumber * i
#         print("{} x {} = {}".format(userNumber, i, res))
#
#     print("-------------")


def showTimesTable(userNumber):
    for i in range(1, 11):
        res = userNumber * i
        print("{} x {} = {}".format(userNumber, i, res))

for i in range(1, 13):
    showTimesTable(i)
    print("-------------")