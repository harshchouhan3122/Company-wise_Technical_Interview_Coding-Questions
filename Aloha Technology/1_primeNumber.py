# Prime Number

num = int(input())

flag = True

if num < 2:
    flag = False

else:
    for i in range(2, int((num**0.5)+1)):
        if num%i == 0:
            flag = False
            break
        
if flag == True:
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")