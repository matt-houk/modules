#module for finding hypotenuse and a 
#leg of a right triangle using pythagorean theorem

def hypotenuse(a, b):
    c = (a**2 + b**2)**0.5
    return c
def leg(a, c):
    b = (c**2 - a**2)**0.5
    return b
