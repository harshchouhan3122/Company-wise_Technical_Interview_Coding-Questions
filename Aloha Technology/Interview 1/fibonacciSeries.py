#FibonacciSeries

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181.

#FibonacciSeriesinReverseOrder
# 4181, 2584, 1597, 987, 610, 377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0


def fibo(term):
    arr = [0,1]
    
    if term<=2:
        return arr[:term]

    a, b = arr[0], arr[1]
    c1 = 2
    while(c1<term):
        c = a+b
        arr.append(c)
        a,b = b, c
        c1+=1
    return arr

term = 12
print(fibo(term))

