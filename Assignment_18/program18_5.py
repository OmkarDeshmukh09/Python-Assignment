import MarvellouNum

def main():

    arr = []

    Size = int(input("Enter Number elements in list : "))

    for i in range(Size):
        Value = int(input("Enter the Elements :"))
        arr.append(Value)
    
    Ret = MarvellouNum.ListPrime(arr)

    print("The Addition of Prime number in list is : ",Ret)
     

if __name__ == "__main__":
    main()