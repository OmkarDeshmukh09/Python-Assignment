
# C:\Users\DELL\OneDrive\Desktop\Python_Assignment\Assignment_17>python program17_7.py
# Enter a Number : 5
#         1       2       3       4       5
#         1       2       3       4       5
#         1       2       3       4       5
#         1       2       3       4       5
#         1       2       3       4       5


def DisplayPattern(No):
    
    for i in range(0,No,1):
        iValue = 1
        for j in range(0,No,1):
        
            print("\t",iValue,"",end="")
            iValue = iValue + 1 
        print("")
        
        

def main():
    
    Data = int(input("Enter a Number : "))

    DisplayPattern(Data)

        
if __name__ == "__main__":
    main()