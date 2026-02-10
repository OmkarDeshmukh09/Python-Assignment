def SumList(No):
    iSum = 0
    for i in No:

        iSum = iSum + i

    return iSum

def main():
    arr = []

    Size = int(input("Enter Number elements in list : "))

    for i in range(Size):
        Value = int(input("Enter the Elements :"))
        arr.append(Value)
    
    Ret = SumList(arr)

    print("The sum is : ",Ret)
     

if __name__ == "__main__":
    main()