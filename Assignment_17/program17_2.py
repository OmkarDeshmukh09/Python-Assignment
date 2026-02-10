
def DisplayPattern(No):
    
    for i in range(0,No,1):
        for j in range(0,No,1):
            print("\t*",end="")
        print("")
        

def main():
    
    Data = int(input("Enter a Number : "))

    DisplayPattern(Data)

        
if __name__ == "__main__":
    main()