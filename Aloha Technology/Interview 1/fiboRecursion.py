#FibonacciSeriesinReverseOrder
# 4181, 2584, 1597, 987, 610, 377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0


# def fibo(term):
#     a, b = 0, 1
#     c1 = 2
#     arr = [0,1]
#     while(c1<term):
#         c = a+b
#         arr.append(c)
#         a,b = b, c
#         c1+=1
#     return arr


def fiboRecursion(n):
    # Base cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Recursive case: Fibonacci sequence
    print("Done")
    fib_sequence = fiboRecursion(n - 1)
    print("1:", fib_sequence)
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print("2:", fib_sequence)
    return fib_sequence

term = 5
print(fiboRecursion(term))
