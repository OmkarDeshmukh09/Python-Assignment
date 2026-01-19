
def SumDigit(No):
    iSum = 0
    while(No != 0):
        
        Digit = No % 10         #Last digit gets copied into Digit
        
        iSum = Digit + iSum     #Sum of Last Digit is Done
        
        No = No // 10           # Last Digit is Removed
    
    return iSum                 # Sum of Digit of Number is Done
    
def main():

    value = int(input("Enter Number :"))
    
    Ret = SumDigit(value)

    print("Total Sum of Digits are : ",Ret)
    
if __name__ == "__main__":
    main()