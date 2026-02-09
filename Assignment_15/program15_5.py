
from functools import reduce

Maximum = lambda a , b : b if(b > a) else a

def main():

    Data=[1,2,3,4,5,6,7,8]
    
    print("Before using reduce Function :")
    
    print(Data)
    
    MData = reduce(Maximum,Data)
    
    print("After using reduce Function :")
    
    print("Maximum element : ",MData)

if __name__=="__main__":
    main()
    