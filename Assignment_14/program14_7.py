
Divisiable5 = lambda A :True if A % 5 == 0 else False

def main():
    Value = int(input("Enter Number :"))
    
    Ret = Divisiable5(Value)

    if (Ret == True):
        print("The Number is Divisiable by 5 ")
    else:
        print("The Number is  Not Divisiable by 5 ")

if __name__ == "__main__":
    main()