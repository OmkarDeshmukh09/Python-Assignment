
Multiply = lambda a, b : a * b

def main():
    Value1 = int(input("Enter the 1'st number : "))
    Value2 = int(input("Enter the 2'st number : "))

    Ret = Multiply(Value1,Value2)

    print("The Multiplication of ",Value1," & ",Value2," is : ",Ret)
     

if __name__ == "__main__":
    main()