
def Pattern(No):
    
    for i in range(0,No,1):
        print("  *  ",end="")
    


def main():
    
    Data = int(input("Enter a Number : "))

    Pattern(Data)

        
if __name__ == "__main__":
    main()