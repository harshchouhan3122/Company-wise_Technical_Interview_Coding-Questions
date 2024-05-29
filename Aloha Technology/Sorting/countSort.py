arr = [5,6,2,3,0,9,7,8,1]

#count Sort
def countSort1(arr):
    arr1 = {}
    for i in arr:
        if i not in arr1:
            arr1[i] = 1
            continue
        arr1[i] += 1

    print(arr1)

    arr1 = sorted(arr1)
    print(arr1)
    arr2 = []
    for i in arr1:
        while(arr1[i]>0):
            arr2.append(i)
            arr1[i] -= 1
        
    return arr2


def countSort2(arr):
    pass

print(arr)
print(countSort1(arr))
# print(countSort2(arr))