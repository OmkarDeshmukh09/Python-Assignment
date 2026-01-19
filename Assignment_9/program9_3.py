
def Square(No):
    ret = No * No
    return ret

def main():
    value = int(input("Enter Number :"))
    
    Ret = Square(value)

    print("The Square of ",value," is : ",Ret)

if __name__ == "__main__":
    main()