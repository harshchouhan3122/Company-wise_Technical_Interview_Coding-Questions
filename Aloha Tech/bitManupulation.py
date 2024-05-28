# Check the given number is the power of 2 or not

def check(n):
    return (n&(n-1))==0


def countSetBits(n):
    count = 0
    while(n>0):
        if (n&1 != 0):
            count += 1
        n>>=1
    return count

def checkOddEven(n):
    if(n&1 ==0):
        return "Even"
    return "Odd"

def uppertoLower(char1):
    return chr((ord(char1)+32))

num = 100
char = "A"

# print(check(num))
# print(countSetBits(num))
# print(checkOddEven(num))
print(uppertoLower(char))