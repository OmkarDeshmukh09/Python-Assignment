import threading

def Prime(Arr):

    print("\nThe name of Thread is :", threading.current_thread().name)
    print("The ID of thread is   :", threading.get_ident())

    print("Prime Numbers are :")

    for num in Arr:
        if num > 1:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    break
            else:
                print(num)

def NonPrime(Arr):

    print("\nThe name of Thread is :", threading.current_thread().name)
    print("The ID of thread is   :", threading.get_ident())

    print("Non Prime Numbers are :")

    for num in Arr:
        if num <= 1:
            print(num)
        else:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    print(num)
                    break

def main():

    StringX = []

    iValue = int(input("Enter the Number elements :"))

    for i in range(iValue):
        value = int(input("Enter Element : "))
        StringX.append(value)

    print("The List is : ",StringX)

    T1 = threading.Thread(target=Prime,args=(StringX,),name="Prime")
    T2 = threading.Thread(target=NonPrime,args=(StringX,),name="NonPrime")
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()
    
    

    print("\nExit from Main Thread")
     

if __name__ == "__main__":
    main()