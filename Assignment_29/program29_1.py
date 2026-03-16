import os

def main():
    FileName = input("Enter the File Name : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("The File ",FileName," Exist in current directory")

    else:
        print("The File ",FileName," do not Exist in current directory")      

    

if __name__ =="__main__":
    main()