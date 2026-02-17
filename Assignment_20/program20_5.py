import threading

def DisplayIncreasing(No):
     
    for i in range(0,No+1,1):
        print(i,end=" ")
    
    print("\nThe name of Thread is : ",threading.current_thread().name)
    print("The ID of thread is   : ",threading.get_ident())

def DisplayDecreasing(No):
    
    while(No != 0):
        print(No,end=" ")
        No = No - 1

    
    print("\nThe name of Thread is : ",threading.current_thread().name)
    print("The ID of thread is   : ",threading.get_ident())


def main():

    StringX = int(input("Enter the Number :"))

    T1 = threading.Thread(target=DisplayIncreasing,args=(StringX,),name="DisplayIncreasing")
    T2 = threading.Thread(target=DisplayDecreasing,args=(StringX,),name="DisplayDecreasing")
    
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    
    

    print("Exit from Main Thread")
     

if __name__ == "__main__":
    main()