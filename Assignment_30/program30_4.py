import os

def DisplayFileContent(FileSrc,FileDest):

    if(os.path.isfile(FileSrc)):

        fobjSrc = open(FileSrc,"r")

        fobjDest = open(FileDest,"w")

        for line in fobjSrc:
            fobjDest.write(line)
        
        print("File copied from ",FileSrc," to ",FileDest," successfully")
            

    else:
        print("Invalid FileName")
        return 0

def main():
    
    FileSrc = input("Enter File Name : ")
    FileDest = input("Enter File Name : ")

    DisplayFileContent(FileSrc,FileDest)


if __name__ == "__main__":
    main()