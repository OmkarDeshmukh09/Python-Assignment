import threading

def Even(No):
    for i in range(2,No*2+1,2):
        print("The Even Number's are :",i)

def Odd(No):
    for i in range(1,No*2+1,2):
        print("The Odd Number's are :",i)
    

def main():

    Value = int(input("Enter Number : "))

    T1 = threading.Thread(target=Even,args=(Value,))
    T2 = threading.Thread(target=Odd,args=(Value,))
    
    T1.start()
    T1.join()
    
    T2.start()
    T2.join()
     

if __name__ == "__main__":

    main()
