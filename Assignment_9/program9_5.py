
def ChkDivisiable(No):
    if(No % 3 == 0 ) and (No % 5 == 0):
        return True
    else:
        return False

def main():
    value = int(input("Enter Number :"))
    
    Ret = ChkDivisiable(value)

    if (Ret == True):
        print("The ",value," is Divisiable by 3 & 5 ")
    else:
        print("The ",value," is Not Divisiable by 3 & 5 ")

if __name__ == "__main__":
    main()