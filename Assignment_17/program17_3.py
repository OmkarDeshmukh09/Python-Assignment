
def Factorial(No):
    iValue = 1

    while(No != 0):
        iValue = iValue * No
        No = No - 1
    
    return iValue
        

def main():
    
    Data = int(input("Enter a Number : "))

    Ret = Factorial(Data)

    print("Factorial is : ",Ret)
        
if __name__ == "__main__":
    main()