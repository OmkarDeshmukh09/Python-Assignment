
MaxNumber = lambda A , B :True if A > B else False

def main():
    Value1 = int(input("Enter First Number :"))

    Value2 = int(input("Enter Second Number :"))
    
    Ret = MaxNumber(Value1,Value2)

    if (Ret == True):
        print("The Maximum Number is : ",Value1)
    else:
        print("The Maximum Number is : ",Value2)

if __name__ == "__main__":
    main()