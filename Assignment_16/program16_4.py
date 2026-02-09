
def Display(data):
    
    for i in range(1,6,1):
        print(data)

def main():
    
    Data = input("Enter a Massage : ")

    Ret = Display(Data)

    print("The Addition is : ",Ret)
        
if __name__ == "__main__":
    main()