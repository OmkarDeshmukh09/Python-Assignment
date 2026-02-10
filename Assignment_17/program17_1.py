import Arithmetic

def main():
    
    Data1 = int(input("Enter a 1st Number : "))
    Data2 = int(input("Enter a 2nd Number : "))

    Arithmetic.Addition(Data1, Data2)
    Arithmetic.Substraction(Data1, Data2)
    Arithmetic.Multiplication(Data1, Data2)
    Arithmetic.Division(Data1, Data2)

        
if __name__ == "__main__":
    main()