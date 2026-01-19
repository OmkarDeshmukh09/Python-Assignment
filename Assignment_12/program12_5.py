
def Display(No):

    while(No != 0):
        print(No,end=" ")
        No = No - 1


def main():

    Value = int(input("Enter the Number : "))
    
    Display(Value)

if __name__ == "__main__":
    main()