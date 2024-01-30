# Python program for the above approach
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
# Function to print the fibonacci
# series in reverse order.
def fibo(n, a, b):
	if (n > 0):
		# Function call
		fibo(n - 1, b, a + b)
		# Print the result
		# print(a, end=" ")
        if isPrime(a):
		    print(a, end=" ")
                  
            


# Driver Code
if __name__ == "__main__":

	N = 10
	fibo(N, 0, 1)

	# This code is contributed by Samim Hossain Mondal.
