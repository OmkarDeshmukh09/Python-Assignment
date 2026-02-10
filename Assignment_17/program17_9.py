def CountDigit(No):
    iCount = 0
    
    while(No != 0):
    
        iCount = iCount + 1
        #iDigit =  No % 10
        No = No // 10

    return iCount
    
def main():
    Number = int(input("Enter A Number : "))

    Ret = CountDigit(Number)

    print("The digit's in number is : ",Ret)

if __name__ == "__main__":
    main()