
def ChkNum(No):
    if( No > 0):
        print("Positive number")
    
    elif(No < 0):
        print("Negitive number")
       
    else:
        print("Zero")


def main():
    
    Data = int(input("Enter a Number : "))

    ChkNum(Data)
        
if __name__ == "__main__":
    main()