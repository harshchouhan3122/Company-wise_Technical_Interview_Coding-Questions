#DigitSum

num = 546

def digitSum(num):
    val = 0
    while(num!=0):
        val += num%10
        num //= 10
    return val


print(digitSum(num))