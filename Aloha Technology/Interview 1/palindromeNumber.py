#PalindromeNumber

def isPalindrome(num):
    orgNum = num
    revNum = 0
    while(num!=0):
        revNum = revNum*10 + num%10
        num //= 10
    if orgNum == revNum:
        return True
    return False

num = 12343210
print(isPalindrome(num))