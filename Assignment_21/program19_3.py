
from functools import reduce


def Sourght(arr):
        return( arr >= 70) and (arr<= 90)
            
def Incriment(arr):
     return (arr + 10)

def Product(a,b):
         return(a * b)


def main():
    Data = []

    n =  int(input("Enter the number of element in list : "))
    
    for i in range(n):
        
        No = int(input("Element in list :"))

        Data.append(No)
    
    print(Data)

    Ret = list(filter(Sourght,Data))

    print("After filter (70 to 90) :", Ret)
    
    Ret = list(map(Incriment,Ret))  

    print("After increment by 10 :", Ret)

    Sum = reduce(Product,Ret )

    print(Sum)

if __name__ == "__main__":
    main()