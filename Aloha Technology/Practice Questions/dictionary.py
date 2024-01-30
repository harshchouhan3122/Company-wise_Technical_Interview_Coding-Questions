# sortingDictionary

def dict(arr):
    dict1 = {}
    for i in arr:
        if i not in dict1:
            dict1[i] = 1
            continue
        dict1[i]+=1
    return dict1


def sort1(dict1):
    pass


arr = [1,4,5,7,2,9,8,5,6,4,4,0,3,34,5,4,3,2,1]
dict1 = dict(arr)   # Convert array to dictionary using frequency

print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())


ls1 = dict1.keys()
ls2 = dict1.values()

ls3 = list(zip(ls1,ls2))
# print(ls1)
# print(ls2)
# print(ls3)

# print(ls3[2][-1])

# ls3 = sorted(ls3, key=lambda x:x[-1], reverse=True)
# print(ls3)

# res = {key:val for key, val in sorted(dict1.items(), key=lambda x:x[0])}
# print(res)
res = [[key,val] for key, val in sorted(dict1.items(), key=lambda x:x[1])]
print(res)