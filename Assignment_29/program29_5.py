import hashlib
import os
import sys

def CheckSum(FileName):

    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():

    if(len(sys.argv) != 2):
        print("Error : Invalid number of Arguments")
        return

    FileName1 = (sys.argv[1])

    Ret1 = os.path.exists(FileName1)


    if Ret1 and Ret2:

        hash1 = CheckSum(FileName1)
        hash2 = CheckSum(FileName2)

        if(hash1 == hash2):
            print("Success")
        else:
            print("Failuare")

    else:
        print("Invalid File")


if __name__ =="__main__":
    main()