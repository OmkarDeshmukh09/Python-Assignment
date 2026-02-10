
from functools import reduce


def SourghtPrime(arr):
    if arr <= 1:
        return False

    for i in range(2, arr):
        if arr % i == 0:
            return False

    return True  
            
SquareIncriment = lambda arr: (arr * 2 )

Maximaum = lambda a,b : max(a,b)


def main():
    Data = []

    n =  int(input("Enter the number of element in list : "))
    
    for i in range(n):
        
        No = int(input("Element in list :"))

        Data.append(No)
    
    print(Data)

    Ret = list(filter(SourghtPrime,Data))

    print("After filter :", Ret)
    
    Ret = list(map(SquareIncriment,Ret))  

    print("List After map", Ret)

    Sum = reduce(Maximaum,Ret)

    print("Output of Reduce :",Sum)

if __name__ == "__main__":
    main()