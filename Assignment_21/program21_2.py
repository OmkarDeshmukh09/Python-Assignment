import threading

def MaxElement(Arr):

    print("\nThe name of Thread is :", threading.current_thread().name)
    print("The ID of thread is   :", threading.get_ident())

    Max = 0

    for num in Arr:
        if num > Max:
            Max = num

    print("Max Number is : ",Max)        

def MinElement(Arr):

    print("\nThe name of Thread is :", threading.current_thread().name)
    print("The ID of thread is   :", threading.get_ident())

    Min = Arr[0]

    for num in Arr:
        if num <= 1:
            print(num)
    
    print("Min Number is : ",Min)

def main():

    StringX = []

    iValue = int(input("Enter the Number elements :"))

    for i in range(iValue):
        value = int(input("Enter Element : "))
        StringX.append(value)

    print("The List is : ",StringX)

    T1 = threading.Thread(target=MaxElement,args=(StringX,),name="MaxElement")
    T2 = threading.Thread(target=MinElement,args=(StringX,),name="MinElement")
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()
    
    

    print("\nExit from Main Thread")
     

if __name__ == "__main__":
    main()