import math

def area_of_triangle(a, b, c):
    # check if the combination of sides is possible
    if a+b > c and a+c > b and b+c > a:
        # calculate semi-perimeter
        s = (a+b+c)/2
        # calculate area using Heron's formula
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area
    else:
        return "The combination of sides is not possible"

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

print("Area of the triangle: ", area_of_triangle(a, b, c))
