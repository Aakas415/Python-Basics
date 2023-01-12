from cmath import pi
import math

r = float(input("Enter radius of circle: "))

def findArea():
    area =  math.pi * r * r
    print("The area of circle is: ",area)
    return area

def findCircumference():
    circumfarence =  2 * math.pi * r
    print("The Circumfarence is: ",circumfarence)
    return circumfarence

findArea()
findCircumference()