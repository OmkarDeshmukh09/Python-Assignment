import threading

def Small(str):
    Count = 0 

    for ch in str:
        if(ch.islower()):
            Count = Count + 1

    print("The name of Thread is : ",threading.current_thread().name)
    print("The ID of thread is   : ",threading.get_ident())
    print("The Total numbers of Small letters in String is : ",Count)

def Capital(arr):

    Count = 0 

    for ch in str:
        if(ch.isupper()):
            Count = Count + 1

    print("The name of Thread is : ",threading.current_thread().name)
    print("The ID of thread is   : ",threading.get_ident())
    print("The Total numbers of Capital letters in String is : ",Count)

def main():

    StringX = input("Enter the String :")

    print("The List is : ",StringX)

    T1 = threading.Thread(target=Small,args=(StringX,),name="Small")
    T2 = threading.Thread(target=Capital,args=(StringX,),name="Capital")
    
    T1.start()
    T1.join()
    
    T2.start()
    T2.join()

    print("Exit from Main Thread")
     

if __name__ == "__main__":
    main()