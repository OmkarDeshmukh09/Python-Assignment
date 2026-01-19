
def PrintOdd(No):
    
    for i in range(1 , No+1 , 1):
        if (i % 2 != 0):
            print(i,end=" ")    
    

def main():
    value = int(input("Enter Number :"))
    
    PrintOdd(value)

if __name__ == "__main__":
    main()