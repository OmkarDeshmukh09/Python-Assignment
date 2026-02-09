
def ChkDivBy5(No):
    if( No % 5 == 0):
        print("True")
    
    else:
        print("False")


def main():
    
    Data = int(input("Enter a Number : "))

    ChkDivBy5(Data)

        
if __name__ == "__main__":
    main()