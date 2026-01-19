
def Table(No):
    for i in range(No,No*10+1,No):
        print(i,end=", ")

def main():
    value = int(input("Enter Number to print table  :"))
    
    Table(value)

if __name__ == "__main__":
    main()