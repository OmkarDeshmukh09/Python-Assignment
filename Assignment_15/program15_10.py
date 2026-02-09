
from functools import reduce

EvenCount = lambda data: len(list(filter(lambda x: x % 2 == 0, data)))


def main():

    Data = [1,2,3,4,5,6,7,8,9,10,11,12,15,20,31,23,33,30]
    
    print("Before using filter Function :")
    
    print(Data)
    
    MData = EvenCount(Data)
    
    print("After using filter Function :")
    
    print("Elements are : ",MData)

if __name__=="__main__":
    main()
    