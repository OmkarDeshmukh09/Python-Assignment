def ListQue(No):
    max = 0
    for i in No:

        if(max < i):
            max = i

    return max

def main():
    arr = []

    Size = int(input("Enter Number elements in list : "))

    for i in range(Size):
        Value = int(input("Enter the Elements :"))
        arr.append(Value)
    
    Ret = ListQue(arr)

    print("The Max in list is : ",Ret)
     

if __name__ == "__main__":
    main()