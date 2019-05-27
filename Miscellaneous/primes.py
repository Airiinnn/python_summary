#returns the prime factors of n
def find_primes(n):
    n = int(n)
    if n==1:
        return False
    arr=[]
    while n!=1:
        if n%2==0:
            arr.append(2)
            n/=2
        else:
            for i in range(3, int(n+1), 2):
                if n%i==0:
                    arr.append(i)
                    n/=i

    return arr
    
#returns the nth prime, with the 1st prime being 2
def get_nth_prime(n):
    n=int(n)
    arr=[2]
    if n==1:
        return 2
    check=3
    counter=1
    while counter<n:
        for i in arr:
            if i>int(check**0.5):
                arr.append(check)
                counter+=1
                break
            if check%i==0:
                break
        check+=2        
    return arr[-1]

#returns array of first n primes
def first_n_primes(n):
    n=int(n)
    arr=[2]
    if n==1:
        return arr
    check=3
    counter=1
    while counter<n:
        for i in arr:
            if i>int(check**0.5):
                arr.append(check)
                counter+=1
                break
            if check%i==0:
                break
        check+=2
    return arr
    
#returns array of all primes below n
def all_primes_below_n(n):
    n=int(n)
    arr=[2]
    if n==1:
        return arr
    check=3
    while check<n:
        for i in arr:
            if i>int(check**0.5):
                arr.append(check)
                break
            if check%i==0:
                break
        check+=2
    return arr

def is_prime(n):
    if n==2:
        return True
    if n%2==0 or n==1 or n==0:
        return False
    for i in range(3,int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True
