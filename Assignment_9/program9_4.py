
def Cube(No):
    ret = No * No * No
    return ret

def main():
    value = int(input("Enter Number :"))
    
    Ret = Cube(value)

    print("The Cube of ",value," is : ",Ret)

if __name__ == "__main__":
    main()