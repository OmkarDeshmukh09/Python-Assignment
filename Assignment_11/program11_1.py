
def PrimeNumber(No):
    for i in range(2, No,1):
        if (No % i != 0):
            return True
        else:
            return False    
    

def main():
    value = int(input("Enter Number :"))
    
    Ret = PrimeNumber(value)

    if(Ret == True):
        print("It's Prime number")
    else:
        print("It's Not Prime number")

if __name__ == "__main__":
    main()