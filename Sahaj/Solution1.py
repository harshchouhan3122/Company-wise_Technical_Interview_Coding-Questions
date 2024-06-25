
l,h = input().split(" ")
l,h = int(l),int(h)

lower_block = list(map(int,input().split(" ")))
upper_block = list(map(int,input().split(" ")))

# print(l,h)
# print(lower_block)
# print(upper_block)

count = 0

if (l>=1 and l<=100000) and (h>=1 and h<=100000):

    if len(lower_block)==len(upper_block) and len(lower_block) == l:

        for i in range(l):
            if lower_block[i]+upper_block[i] < h:
                count += 1

        if count == l:
            print("YES")
        else:
            print("NO")
else:
    print(-1)