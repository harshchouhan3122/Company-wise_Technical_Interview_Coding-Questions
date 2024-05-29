n = 5  # Change the value of 'n' as needed

# Initialize the first number in the series
a, b = 0, 1

# Print the first number (special case for n=1)
if n == 1:
    print(a)

# Generate the rest of the series
elif n > 1:
    print(a, b, end=" ")
    count = 2
    while count < n:
        a, b = b, a + b
        print(b, end=" ")
        count += 1

# Output: 0 (for n=1)
