import os

def CheckFileContent(FileSrc,str):

    if(os.path.isfile(FileSrc)):

        fobjSrc = open(FileSrc,"r")

        for line in fobjSrc:
            for word in line.split():
                
                if(word == str):
                    return True
        
        fobjSrc.close()
        return False

    else:
        print("Invalid FileName")
        return 0

def main():
    
    FileSrc = input("Enter File Name : ")
    Word = input("Enter Word want to Search : ")

    Ret = CheckFileContent(FileSrc,Word)

    if(Ret == True):
        print("Word : ",Word," Exisits in File")
    else:
        print("Word : ",Word," don't Exisits in File")

if __name__ == "__main__":
    main()