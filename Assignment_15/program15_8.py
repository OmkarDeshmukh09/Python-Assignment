
from functools import reduce

DivBy3And5 = lambda a  :  a % 3 == 0 and a %5 == 0

def main():

    Data = [1,2,3,4,5,6,7,8,9,10,11,12,15,20,31,23,33,30]
    
    print("Before using filter Function :")
    
    print(Data)
    
    MData = list(filter(DivBy3And5,Data))
    
    print("After using filter Function :")
    
    print("Elements divisible by 3 and 5 : ",MData)

if __name__=="__main__":
    main()
    