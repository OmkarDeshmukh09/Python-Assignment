
# C:\Users\DELL\OneDrive\Desktop\Python_Assignment\Assignment_17>python program17_8.py
# Enter a Number : 5
#         1       
#         1       2      
#         1       2       3
#         1       2       3       4   
#         1       2       3       4       5


def DisplayPattern(No):
    iCnt = 0

    for i in range(1,No+1,1):
        for j in range(1,No+1,1):
            if(i >= j):
                print("\t",j,"",end="")
            
        print("")
        
        

def main():
    
    Data = int(input("Enter a Number : "))

    DisplayPattern(Data)

        
if __name__ == "__main__":
    main()