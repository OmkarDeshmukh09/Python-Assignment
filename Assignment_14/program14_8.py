
Addition = lambda A , B : A + B 

def main():
    Value1 = int(input("Enter First Number :"))

    Value2 = int(input("Enter Second Number :"))
    
    Ret = Addition(Value1,Value2)

    print("The Addition of Number's is : ",Ret)

if __name__ == "__main__":
    main()