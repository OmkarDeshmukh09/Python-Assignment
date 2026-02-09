
from functools import reduce

Addition = lambda a , b : b + a   

def main():

    Data=[1,2,3,4,5,6,7,8]
    
    print("Before using reduce Function :")
    
    print(Data)
    
    MData = reduce(Addition,Data)
    
    print("After using reduce Function :")
    
    print(MData)

if __name__=="__main__":
    main()
    