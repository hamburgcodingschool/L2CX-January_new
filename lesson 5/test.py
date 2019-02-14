# import turtle
#
# bob = turtle.Turtle()
# # print(bob)
#
#
# bob.lt(90)
#
#
# turtle.mainloop()

import requests
import json
import csv

req = requests.get("https://api.punkapi.com/v2/beers")

response = req.text

print(response)

y = json.loads(response)

print(y[0]['id'])


x = open('test1.csv', 'r')

cr = csv.DictReader(x)

for row in cr:
    print(row)
