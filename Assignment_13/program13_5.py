
def DisplayGrade(No):
    
    if(No < 0 or No > 100):
        print("Invalid Input")
        return

    if(No < 30):
        print(" Fail")
    elif(No <= 50):
        print(" Second Class")
    elif(No <= 60):
        print(" First Class")
    elif(No <= 100):
        print(" Distinction")

def main():
    value = int(input("Enter Marks :"))

    DisplayGrade(value)

if __name__ == "__main__":
    main()