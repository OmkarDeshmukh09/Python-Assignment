
def ChkVowel(No):
    
    if (No == 'a' or No == 'e' or No == 'i' or No == 'o' or No == 'u'):
        return True
    else:
        return False    


def main():
    value = (input("Enter alphabet :"))
    
    Ret = ChkVowel(value)

    if(Ret == True):
        print("It's A Vowel")
    else:
        print("It's not a Vowel")

if __name__ == "__main__":
    main()