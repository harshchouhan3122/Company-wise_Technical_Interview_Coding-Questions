def checkPrime(num):
    for i in range(2, int(num**0.5 +1)):
        if num%i == 0:
            return False
    return True

def primeNumSeries(num1, num2):
    res = []
    for i in range(num1, num2):
        if i<2:
            continue
        else:
            if checkPrime(i):
                res.append(i) 
    return res

num1 = int(input("Enter lower limit: "))
num2 = int(input("Enter upper limit: "))

print(primeNumSeries(num1, num2))
