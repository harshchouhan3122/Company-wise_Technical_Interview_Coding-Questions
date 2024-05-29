#PrimeNumber
#2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.

def isPrime(num):
    if num > 1:
        for i in range(2,num//2):
            if num%i==0:
                return 0
    return 1

num = int(input())
print(isPrime(num))