
def Display(No):
    
    while(No != 0):
        print(No,end="\t")
        No = No - 1

def main():
    
    Data = int(input("Enter a Number : "))

    Display(Data)

if __name__ == "__main__":
    main()