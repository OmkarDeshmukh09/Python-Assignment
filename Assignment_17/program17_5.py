
def FactorialAdditionn(No):
    iValue = 1

    for i in range(0,No/2,1):
        if((No % i) == 0):
            return False
        
    
    return iValue
        

def main():
    
    Data = int(input("Enter a Number : "))

    Ret = FactorialAdditionn(Data)

    if(Ret == True):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if __name__ == "__main__":
    main()