
Addtion = lambda a,b : a + b 
    
Substraction = lambda a,b : a - b

Division = lambda a,b : b / a

Multipliction = lambda a,b : a * b
    

def main():
    value1 = int(input("Enter 1'st Number :"))
    
    value2 = int(input("Enter 2'nd Number :"))

    print("Addition : ",Addtion(value1,value2))

    print("Substraction : ",Substraction(value1,value2))

    print("Division : ",Division(value1,value2))

    print("Multipliction : ",Multipliction(value1,value2))


"""
    if(Ret == True):
        print("It's A Vowel")
    else:
        print("It's not a Vowel")
"""
if __name__ == "__main__":
    main()