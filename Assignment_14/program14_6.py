
EvenOdd = lambda A :True if A % 2 == 0 else False

def main():
    Value = int(input("Enter Number :"))
    
    Ret = EvenOdd(Value)

    if (Ret == True):
        print("The Number is Even ")
    else:
        print("The Number is  Odd ")

if __name__ == "__main__":
    main()