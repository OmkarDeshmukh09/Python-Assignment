
def ChkNum(No):
    if (No % 2 == 0):
        return True
    
    else:
        return False 

def main():
    
    Data = int(input("Enter a number : "))

    Ret = ChkNum(Data)

    if(Ret == True):
        print("The Number is Even")
    
    else:
        print("The Number is Odd")
        
if __name__ == "__main__":
    main()