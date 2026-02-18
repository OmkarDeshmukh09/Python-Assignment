
class Demo:
    def __init__(self,No1,No2):
        self.a = No1
        self.b = No2

    def Accept(self):
        print("1'st number is : ",self.a)
        print("2'nd number is : ",self.b)       

    def Addition(self):
 
        return self.a + self.b

    def Substraction(self):

        sub = 0 

        if(self.a < self.b):
            sub = self.b - self.a

        else:
            sub = self.a - self.b

        return sub

    def Multiplication(self):
        return self.a * self.b
    
    def Division(self):
        return  self.b / self.a
    
def main():

    iValue1 = int(input("Enter 1'st number : "))  
    iValue2 = int(input("Enter 2'nd number : "))
    print()

    obj1 = Demo(iValue1,iValue2)

    obj1.Accept()
    Ret = obj1.Addition()
    print("Addition is : ",Ret)

    Ret = obj1.Substraction()
    print("Substraction is : ",Ret)
    
    Ret = obj1.Multiplication()
    print("Multiplication is : ",Ret)
    
    Ret = obj1.Division()
    print("Division is : ",Ret)
    

if __name__ == "__main__":
    main()