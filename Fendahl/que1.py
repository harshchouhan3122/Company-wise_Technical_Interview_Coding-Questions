# str = input()
str = "engineer"
res= 0

for i in range(len(str)):
    if len(set(list(str[:i]))) == len(str[:i]):
        res = max(res, len(str[:i]))
        # res = str[:i]

for i in range(len(str)):
    if len(set(list(str[i:]))) == len(str[i:]):
        res = max(res, len(str[i:]))
        # res = str[i:]

print(res)