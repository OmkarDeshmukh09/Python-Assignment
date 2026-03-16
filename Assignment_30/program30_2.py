import os

def CountWords(FileName):
    
    count = 0

    if(os.path.isfile(FileName)):

        fobj = open(FileName,"r")

        for line in fobj:
            
            words = line.split()
            count = count + len(words)
        
        return count
    else:
        print("Invalid FileName")
        return 0

def main():
    
    FileName = input("Enter File Name : ")

    Ret = CountWords(FileName)

    print("Total number of words are : ",Ret)


if __name__ == "__main__":
    main()