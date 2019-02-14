# if testYear % 4 == 0:
#     if testYear % 100 == 0:
#         if testYear % 400 == 0:
#             print("LEAP YEAR")
#         else:
#             print("NOT LEAP YEAR")
#     else:
#         print("LEAP YEAR")
# else:
#     print("NOT LEAP YEAR")

# if testYear % 4 != 0:
#     print("NOT LEAP YEAR")
# elif testYear % 100 != 0:
#     print("LEAP YEAR")
# elif testYear % 400 != 0:
#     print("NOT LEAP YEAR")
# else:
#     print("LEAP YEAR")

def leapYear(testYear):
    if testYear % 4 != 0:
        return False
    elif testYear % 100 != 0:
        return True
    elif testYear % 400 != 0:
        return False
    else:
        return True

# if leapYear(2004):
#     print("it's a leap year")
# else:
#     print("it is not")

year = 2019
leapYearCounter = 0

while leapYearCounter < 20:
    if leapYear(year):
        leapYearCounter += 1
        print("{}: {}".format(leapYearCounter, year))
    year += 1

