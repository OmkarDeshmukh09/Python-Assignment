
from functools import reduce

ElementProduct = lambda a , b :  a * b 

def main():

    Data = [1,2,3,4,5,6,7,8,9,10,11,12,15,20,31,23,33,30]
    
    print("Before using filter Function :")
    
    print(Data)
    
    MData = reduce(ElementProduct,Data)
    
    print("After using reduce Function :")
    
    print("Elements Element's Product : ",MData)

if __name__=="__main__":
    main()
    