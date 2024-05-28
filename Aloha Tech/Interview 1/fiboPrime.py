#Fibonacci Prime
# 2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073

def isPrime(num):
    count = 0 
    if num > 1:
        # for i in range(2,int(num**(0.5)+1)):
        for i in range(2,num//2):
            count += 1
            if num%i==0:
                print(num,count)
                return 0
    return 1

def fiboPrime(term):
    if term<1:
        return []

    arr = [0,1]
    a, b = arr[0], arr[1]    
    arr = []

    count = 0
    while(count<term):
        c = a+b
        a,b = b, c

        if (isPrime(c) and c!=1):
            arr.append(c)
            count += 1
    return arr

term = 9
res = fiboPrime(term)
print(res)