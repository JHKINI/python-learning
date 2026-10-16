n= int(input())
def is_prime(n):
    if  n ==2:
        return True
    elif n >2:
        for i in range(2,n-1,1): #in range(n-2):
            if n%i == 0:
                return False

        return True


