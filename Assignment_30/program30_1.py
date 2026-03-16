import os

def CountLines(FileName):
    
    count = 0

    if(os.path.isfile(FileName)):

        fobj = open(FileName,"r")

        for line in fobj:

            count += 1
        
        return count
    else:
        print("Invalid FileName")
        return

def main():
    
    FileName = input("Enter File Name : ")

    Ret = CountLines(FileName)

    print("Total number of lines are : ",Ret)


if __name__ == "__main__":
    main()