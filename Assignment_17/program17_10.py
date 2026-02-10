def SumDigit(No):
    iDigit = 0
    iSum = 0

    while(No != 0):

        iDigit =  No % 10
        iSum = iDigit + iSum
        No = No // 10

    return iSum
    
def main():
    Number = int(input("Enter A Number : "))

    Ret = SumDigit(Number)

    print("The Addition of digit's in number is : ",Ret)

if __name__ == "__main__":
    main()