arr = [5,6,2,3,0,9,7,8,1]

#Insertion Sort
def insertionSort1(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = i-1
        while(prev>=0 and arr[prev]>curr):      #Ascending Order Sorting
            arr[prev+1] = arr[prev]
            prev-=1
        arr[prev+1] = curr
    return arr

def insertionSort2(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = i-1
        while(prev>=0 and arr[prev]<curr):      #Descending Order Sorting
            arr[prev+1] = arr[prev]
            prev-=1
        arr[prev+1] = curr
    return arr


print(arr)
print(insertionSort1(arr))
arr = [5,6,2,3,0,9,7,8,1]
print(insertionSort2(arr))