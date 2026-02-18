
class Demo:
    def __init__(self,No1):
        self.Radius = No1
        self.PI = 3.14

    def Accept(self):
        print("Radius of Circle is : ",self.Radius)
        print("PI of Circle is : ",self.PI)       

    def CalculateArea(self):

        Area = 0 

        Area = self.PI * (self.Radius ** 2)

        print("Area of circle is : ",Area)

    def CalculateCircumference(self):
        
        Circumference = 0

        Circumference = 2 * self.PI * self.Radius

        print("Circumference of circle is : ",Circumference)

def main():

    iValue1 = float(input("Enter Radius : "))  

    obj1 = Demo(iValue1)
    obj2 = Demo(iValue1+10)

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()

if __name__ == "__main__":
    main()