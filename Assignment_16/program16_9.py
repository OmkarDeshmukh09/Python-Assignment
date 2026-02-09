
def DisplayEven(No):
    
    for i in range(2,No*2+1,1):
        if(i % 2 == 0):
            print(i,end="\t")

def main():
    
    Data = int(input("Enter a Number : "))

    DisplayEven(Data)

        
if __name__ == "__main__":
    main()