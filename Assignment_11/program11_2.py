
def CountDigit(No):
    iCount = 0
    while(No != 0):
        
        No = int(No / 10)
        # No = No // 10
        iCount = iCount + 1

    return iCount
    
def main():

    value = int(input("Enter Number :"))
    
    Ret = CountDigit(value)

    print("Total Digits are : ",Ret)
    
if __name__ == "__main__":
    main()