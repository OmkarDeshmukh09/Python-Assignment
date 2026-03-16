import os

def DisplayFileContent(FileName):
    
    count = 0

    if(os.path.isfile(FileName)):

        fobj = open(FileName,"r")

        for line in fobj:
            
            print(line,"\n")

    else:
        print("Invalid FileName")
        return 0

def main():
    
    FileName = input("Enter File Name : ")

    DisplayFileContent(FileName)


if __name__ == "__main__":
    main()