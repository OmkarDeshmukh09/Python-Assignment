
from functools import reduce

LenGrater = lambda a  : len(a) > 5 

def main():

    Data = ["omkar","vitthal","ram","shree","abhijit","mansvi"]
    
    print("Before using filter Function :")
    
    print(Data)
    
    MData = list(filter(LenGrater,Data))
    
    print("After using filter Function :")
    
    print("List of element grater than 5 : ",MData)

if __name__=="__main__":
    main()
    