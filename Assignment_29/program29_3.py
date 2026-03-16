import os
import sys

def main():

    if(len(sys.argv) != 3):
        print("Error : Invalid number of Arguments")
        return

    FileName = (sys.argv[1])

    FileDest = (sys.argv[2])

    Ret = os.path.exists(FileName)

    if(Ret == True):
        
        fobj = open(FileName,"r")

        Data = fobj.read()

        fobj.close()

        print("The Data from File is : ")
        print(Data)

        fobj = open(FileDest,"w")

        fobj.write(Data)

        print(FileDest)

        fobj.close()

    else:
        print("The File ",FileName," do not Exist in current directory")      




if __name__ =="__main__":
    main()