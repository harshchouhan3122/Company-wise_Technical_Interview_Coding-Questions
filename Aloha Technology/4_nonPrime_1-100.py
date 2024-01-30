# Print non prime numbers from 1 to 100.

res = []
for num in range(1, 101):

    flag = True

    if num < 2:
        flag = False

    else:
        for i in range(2, int((num**0.5)+1)):
            if num%i == 0:
                flag = False
                break
        
    if flag == False:
        res.append(num)

print(res)