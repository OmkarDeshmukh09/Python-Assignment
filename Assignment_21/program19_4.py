
from functools import reduce


def SourghtEven(arr):
        return(arr % 2 == 0) 
            
def SquareIncriment(arr):
     return (arr ** 2 )

def ProductAdd(a,b):
         return(a + b)


def main():
    Data = []

    n =  int(input("Enter the number of element in list : "))
    
    for i in range(n):
        
        No = int(input("Element in list :"))

        Data.append(No)
    
    print(Data)

    Ret = list(filter(SourghtEven,Data))

    print("After filter :", Ret)
    
    Ret = list(map(SquareIncriment,Ret))  

    print("List After map", Ret)

    Sum = reduce(ProductAdd,Ret)

    print("Output of Reduce :",Sum)

if __name__ == "__main__":
    main()