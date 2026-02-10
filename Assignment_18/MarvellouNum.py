
def ChkPrime(brr):


    if(brr <= 1):
        return False
    
    for i in range(2,brr):
        if(brr % i == 0):
            return False
        
    return True

def ListPrime(arr):
    
    iSum = 0

    for num in arr:
        if ChkPrime(num):
            iSum = iSum + num

    return iSum