
def PrintNatural(No):
    sum = 0
    for i in range(0 , No+1 , 1):
        sum = sum + i
    
    return sum

def main():
    value = int(input("Enter Number :"))
    
    Ret = PrintNatural(value)

    print("The Sum of Natural Numbers is : ",Ret)

if __name__ == "__main__":
    main()