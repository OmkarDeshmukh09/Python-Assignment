
from functools import reduce

Minimum = lambda a , b : b if(b < a) else a

def main():

    Data=[8,2,3,4,5,6,7,1]
    
    print("Before using reduce Function :")
    
    print(Data)
    
    MData = reduce(Minimum,Data)
    
    print("After using reduce Function :")
    
    print("Minimum element : ",MData)

if __name__=="__main__":
    main()
    