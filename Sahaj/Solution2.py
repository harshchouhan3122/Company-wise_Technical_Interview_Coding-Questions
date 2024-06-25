N = int(input())
need = list(map(int,input().split(" ")))
M = int(input())

if N>0 and N<=10000000:
    if M>=0 and M<=1000000:
        rem = 0
        for i in need:
            cap = 3
            trip = 1
            j = i
            while(cap*trip < i):
                trip+=1
            rem = rem + (cap*trip-i)
        if rem <= M:
            print(rem)    
        else:
            print(-1)

