
def ReverseNumber(No):
    Rev = 1
    while(No != 0):
    #   7521 
        Digit = No % 10         # Last digit gets copied into Digit
        
        Rev = Digit * 10        # Sum of Last Digit is Done
        
        No = No // 10           # Last Digit is Removed
    
    return Rev                  # Sum of Digit of Number is Done
    
def main():

    value = int(input("Enter Number :"))
    
    Ret = ReverseNumber(value)

    print("Reverse Number  : ",Ret)
    
if __name__ == "__main__":
    main()