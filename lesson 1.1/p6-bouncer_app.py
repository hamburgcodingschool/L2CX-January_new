# BOUNCER APP
#
#

print("Hello! How old are you?")
age = int(input())

if age < 6:
  print("Have some milk")
else:
  if age < 18:
    print("Have a Fritz")
  else:
    print("Have a Beer")

print("Thanks for coming!")