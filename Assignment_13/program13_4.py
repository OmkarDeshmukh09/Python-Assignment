
def ChkPerfect(No):
    iSum = 0
    for i in range(1,No-1):
        if(No % i == 0):
            iSum = iSum + i
    
    if(iSum == No):
        return True
    else:
        return False

def main():
    value = int(input("Enter Number :"))

    Ret = ChkPerfect(value)

    if(Ret == True):
        print("Is a Perfect Number ")
    else:
        print("Is not a Perfect Number")

if __name__ == "__main__":
    main()