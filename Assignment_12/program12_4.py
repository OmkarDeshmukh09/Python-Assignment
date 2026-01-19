import time

def Display(No):

    for i in range(1,No+1):
        print(i,end=" ")


def main():

    Value = int(input("Enter the Number : "))

    start_time = time.time()

    Display(Value)

    end_time = time.time()

    print("\ntime Requried : ",end_time-start_time)

if __name__ == "__main__":
    main()