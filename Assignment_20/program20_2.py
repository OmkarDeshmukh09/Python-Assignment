import threading


def EvenFactors(No):

    iSum = 0 

    for i in range(2,No+1,2):
        if(No % i == 0):
            iSum = iSum + i
            print("The Even Factors are :",i)

    print("The Addition of Even Factors is :",iSum)

def OddFactors(No):

    iSum = 0

    for i in range(1,No+1,2):
        if(No % i == 0):
            iSum = iSum + i
            print("The Odd Factors are :",i)

    print("The Addition of Odd Factors is :",iSum)

def main():

    Value = int(input("Enter Number : "))

    T1 = threading.Thread(target=EvenFactors,args=(Value,))
    T2 = threading.Thread(target=OddFactors,args=(Value,))
    
    T1.start()
    T1.join()
    
    T2.start()
    T2.join()

    print("Exit from Main Thread")
     

if __name__ == "__main__":
    main()