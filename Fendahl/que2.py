arr = [0,-1,1,3,8,-8,-3,2]
temp = []

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1,len(arr)):
            if (arr[i] + arr[j] + arr[k]) == 0:
                temp.append([arr[i], arr[j], arr[k]])

print(temp)