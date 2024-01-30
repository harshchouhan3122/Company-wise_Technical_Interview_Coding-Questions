arr = [5,6,2,3,0,9,7,8,1]


#selection Sort
def selectionSort1(arr):
    count = 0           # No. of times loop runs
    for i in range(len(arr)):
        minVal = arr[i]
        idx = i
        for j in range(i+1,len(arr)):
            count +=1
            if arr[j]<minVal:           # Change here for descending sort
                idx = j
                minVal = arr[j]
        arr[i], arr[idx] = arr[idx], arr[i]
    return [arr,count]
    return arr

# Optimized Code (for the sorted array , it will not execute further rounds) 
def selectionSort2(arr):
    count = 0           # No. of times loop runs
    for i in range(len(arr)):
        minVal = arr[i]
        idx = i
        swap = 0
        for j in range(i+1,len(arr)):
            count +=1
            if arr[j]<minVal:           # Change here for descending sort
                swap += 1
                idx = j
                minVal = arr[j]
        if swap == 0:
            break
        arr[i], arr[idx] = arr[idx], arr[i]
    return [arr,count]
    return arr


print(arr)
print(selectionSort1(arr))
print(selectionSort2(arr))