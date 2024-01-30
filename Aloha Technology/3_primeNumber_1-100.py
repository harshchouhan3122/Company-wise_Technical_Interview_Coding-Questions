# Print prime numbers from 1 to 100
res = []

for num in range (2, 101):

    flag = True

    for i in range(2, int((num**0.5)+1)):
        if num%i == 0:
            flag = False
            break
            
    if flag == True:
        res.append(num)

print(res)