
def PalindromeNumber(No):
    
    temp = No
    Rev = 0
    
    while(No != 0):
    
        Digit = No % 10         
                
        Rev = Rev * 10 + Digit        

        No = No // 10           

    if(temp == Rev):
        return True
    else:
        return False                


def main():

    value = int(input("Enter Number :"))
    
    Ret = PalindromeNumber(value)

    if Ret == True:
        print("It is Palindone Number")
    else:
        print("It is not a Palindone Number ")

if __name__ == "__main__":
    main()