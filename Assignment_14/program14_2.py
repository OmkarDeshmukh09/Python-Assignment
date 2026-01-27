
Square = lambda A : A * A * A 

def main():
    Value = int(input("Enter the Number :"))
    
    Ret = Square(Value)

    print("The Cube is : ",Ret)

if __name__ == "__main__":
    main()