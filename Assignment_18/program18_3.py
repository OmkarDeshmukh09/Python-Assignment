def ListQue(No):
    min = No[0]
    for i in No:

        if(min > i):
            min = i

    return min

def main():
    arr = []

    Size = int(input("Enter Number elements in list : "))

    for i in range(Size):
        Value = int(input("Enter the Elements :"))
        arr.append(Value)
    
    Ret = ListQue(arr)

    print("The Min in list is : ",Ret)
     

if __name__ == "__main__":
    main()