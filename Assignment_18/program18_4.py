
def ListQue(Brr,No):

    iCount = 0

    for i in Brr:

        if(No == i):
            iCount = iCount + 1

    return iCount

def main():
    arr = []

    Size = int(input("Enter Number elements in list : "))

    for i in range(Size):
        Value = int(input("Enter the Elements :"))
        arr.append(Value)
    
    freq = int(input("Enter the number to check Frequency of : "))
    
    Ret = ListQue(arr,freq)

    print("The Frequency in list is : ",Ret)
     

if __name__ == "__main__":
    main()