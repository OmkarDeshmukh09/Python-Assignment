import threading

def SumElement(Arr):

    print("\nThe name of Thread is :", threading.current_thread().name)
    print("The ID of thread is   :", threading.get_ident())

    Sum = 0

    for num in Arr:
        Sum = Sum + num            

def ProductElement(Arr):

    print("\nThe name of Thread is :", threading.current_thread().name)
    print("The ID of thread is   :", threading.get_ident())

    Product = 1

    for num in Arr:
        Product = Product * num

def main():

    StringX = [10,20,30,40,50,60,70,80,90,100]

    print("The List is : ",StringX)

    T1 = threading.Thread(target=SumElement,args=(StringX,),name="MaxElement")
    T2 = threading.Thread(target=ProductElement,args=(StringX,),name="MinElement")
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()          

    print("\nExit from Main Thread")
     

if __name__ == "__main__":
    main()