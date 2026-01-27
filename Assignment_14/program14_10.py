
MaxNumber = lambda A, B, C: 1 if (A > B and A > C) else (2 if (B > A and B > C) else 3)

def main():
    Value1 = int(input("Enter First  Number :"))

    Value2 = int(input("Enter Second Number :"))

    Value3 = int(input("Enter Third  Number :"))
    
    Ret = MaxNumber(Value1,Value2,Value3)

    if (Ret == 1):
        print("The Maximum Number is : ",Value1)
    elif(Ret == 2):
        print("The Maximum Number is : ",Value2)
    else:
        print("The Maximum Number is : ",Value3)

if __name__ == "__main__":
    main()