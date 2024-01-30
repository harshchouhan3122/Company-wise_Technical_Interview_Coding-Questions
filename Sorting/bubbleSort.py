arr = [5,6,2,3,0,9,7,8,1]

#bubbleSort
def bubbleSort1(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            count+=1
            if arr[j] > arr[j+1]:          # Change here for descending sort
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return [arr,count]
    return arr

# Optamized bubble sort
def bubbleSort2(arr):
    # count = 0
    for i in range(len(arr)-1):
        swap = 0        # to check that is array is sorted or not, if swap==0 -> sorted array
        for j in range(len(arr)-1-i):
            # count+=1
            if arr[j] > arr[j+1]:          # Change here for descending sort
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
        if swap==0:     #if array is sorted then it terminate the loop
            break
    # return [arr,count]
    return arr

print(arr)
print(bubbleSort1(arr))
print(bubbleSort2(arr))