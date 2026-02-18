
class Numbers:

    Value = 0

    def __init__(self,No1):
        self.a = No1
        

    def ChkPrime(self):
        for i in range(2,self.a//2+1):
            if((self.a % i) == 0):
                return False
            
        return True    

    def ChkPerfect(self):
        Sum = 0 

        for i in range(1,self.a):
            if((self.a % i) == 0):
                Sum = Sum + i

        if Sum == self.a:
            return True
        else: 
            return False

    def Factors(self):

        for i in range(1,self.a + 1):
            if(self.a % i == 0):
                print("The Factors are ",i)

    def SumFactors(self):
        sum = 0 
        for i in range(1,self.a//2 + 1):
            if(self.a % i == 0):
                sum = sum + i
        return sum    
    
def main():

    iValue1 = int(input("Enter 1'st number : "))  

    print()

    obj1 = Numbers(iValue1)

    Ret = obj1.ChkPrime()
    if(Ret == True):
        print( "It's Prime")
    else:
        print("It's not Prime")
    
    Ret = obj1.ChkPerfect()
    if(Ret == True):
        print( "It's Perfect number")
    else:
        print("It's not Perfect Number")
    
    obj1.Factors()

    Ret = obj1.SumFactors()
    print("Sum of Factors is : ",Ret)

if __name__ == "__main__":
    main()