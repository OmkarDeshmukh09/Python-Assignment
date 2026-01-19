
def ChkGrater(No1,No2):
    if(No1 < No2):
        return No2
    else:
        return No2

def main():
    value1 = int(input("Enter 1'st Number :"))
    value2 = int(input("Enter 2'st Number :"))
    
    Ret = ChkGrater(value1,value2)

    print("The Grater number is : ",Ret)

if __name__ == "__main__":
    main()