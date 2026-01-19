
def Factorial(No):
    Fact = 1
    for i in range(1 , No+1 , 1):
        Fact = Fact * i
    
    return Fact

def main():
    value = int(input("Enter Number :"))
    
    Ret = Factorial(value)

    print("The Factorial of Number ",value," is : ",Ret)

if __name__ == "__main__":
    main()