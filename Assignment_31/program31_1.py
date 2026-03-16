# Whrite the automation script to print the file name with extention .txt

import os
import sys

def DirectoryFileSearch(DirName,FileExtension):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such Director ")
        return
    
    Ret  = os.path.isdir(DirName)
    if(Ret == False):
        print("There is no such File ")
        return
     
    for (FolderName, SubFolder, FileName )in os.walk(DirName):
        for File in FileName:
            if(File.endswith(FileExtension)):
                print("File Name : ",File)   

def main():
    border = "-"*55

    print(border)
    print("------------------ Directory File Search  ------------------")
    print(border)

    if(len(sys.argv) == 1):
        print(" Invalid number of Command line Arguments !")
        return

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This Automation  Script is used to : ")
            print(" 1 : Make copy of the existing folder .")
            print(" 2 : By using the command line input.")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use this Automation Script is used to : ")
            print("ScriptName.py SourceDirectory DestinationDirectory")
            print(" SourceDirectory : It is a name for Directory that you want to Search from ")
            print("DestinationDirectory : Name of the Directory you want to copy")
    
        else:
            print("Enable to proceed as there is no such option..")
            print("please use --u or --h for more details...")

    # python Demo.py 5 Data
    
    elif (len(sys.argv) == 3):

        DirectoryFileSearch(sys.argv[1], sys.argv[2])

    else:
        print("Invalid No.of Command line arguments...")
        print("Enable to proceed as there is no such option..")
        print("please use --u or --h for more details...")

    print(border)
    print("----------Thank You For Using Our Script----------")
    print(border)
    

if __name__ =="__main__":
    main()