"""
PI = 3.14

CalculateAreaCircle = lambda radius: PI * radius ** 2

"""

def CalculateAreaCircle(radius):

    PI = 3.14

    Area = PI * radius**2

    return Area

def main():
    value = int(input("Enter Radius :"))

    print("Area of Circle is : ",CalculateAreaCircle(value))

if __name__ == "__main__":
    main()