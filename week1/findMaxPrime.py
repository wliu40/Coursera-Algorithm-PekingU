'''
this program return the max prime number in the range[2, n]
返回小于等于n的最大的素数

'''
def findMaxPrime(n):
    primes = [2]
    candidateNum = 3
    while primes[-1] <= n:
        isPrime = True
        for i in primes:
            if candidateNum % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(candidateNum)
        candidateNum += 2
    print primes
    if(primes[-1] == 2):
        return 2
    return primes[-2]


print findMaxPrime(16)
