import math

def sumItUp(a, b):
    total = a + b
    print(total)

sumItUp(10, 5)
sumItUp(5, 5)


# circleArea (takes the radius as a paremeter, prints the area of the circle)

def circleArea(radius):
    res = math.pi*(radius*radius)
    print("Area: {}".format(res))

def circlePerimeter(radius):
    res = 2*math.pi*radius
    print("Perimeter: {}".format(res))

def circleAP(radius):
    circleArea(radius)
    circlePerimeter(radius)


circleAP(6)