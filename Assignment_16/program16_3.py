
def Display(No):
    iSum = 0

    for i in No:

        iSum = iSum + i
    
    return iSum

def main():
    
    Data = [10,11,10,11]

    Ret = Display(Data)

    print("The Addition is : ",Ret)
        
if __name__ == "__main__":
    main()