
def PrintEven(No):
    
    for i in range(1 , No+1 , 1):
        if (i % 2 == 0):
            print(i,end=" ")    
    

def main():
    value = int(input("Enter Number :"))
    
    PrintEven(value)

if __name__ == "__main__":
    main()