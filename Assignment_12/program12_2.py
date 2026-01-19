
def DisplayFactors(No):
    
    for i in range(1,No+1):
        if(No % i == 0):
            print(i,end="\t")

def main():
    value = int(input("Enter Number :"))
    
    Ret = DisplayFactors(value)
"""
    if(Ret == True):
        print("It's A Vowel")
    else:
        print("It's not a Vowel")
"""
if __name__ == "__main__":
    main()