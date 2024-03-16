#Input :  8 6
# Output : 153 deg

def angle(h,m):
    a = 0.0
    a = abs((h*30)+((15/30)*m)-(m*6))
    a = min(a, 360-a)
    return a

    # ang1 = (h*30) + (15/30)*m    
    # ang2 = m*6                     

    # ang3 = abs(ang1-ang2)

    # a = min(ang3, 360-ang3)
    # return a

# inputs= "8 6"
# output = 153

# h, m = 3, 0

# inputs= list(map(int, input().split(" ")))
# h, m  = int(inputs[0]), int(inputs[1])

# h, m = 10, 30
# h, m = 2, 30
# h, m = 8, 6
# h, m = 11, 56

# print("{:.1f}".format(angle(h,m)))




inputs = {
    1: [8,6],
    2: [2,30],
    3: [10,30],
    4: [11,56]
}

outputs = {
    1: 153.0,
    2: 105.0,
    3: 135.0,
    4: 22.0
}


for i in inputs:
    print(f"Input: {inputs[i][0]}:{inputs[i][1]}")
    h, m = inputs[i][0], inputs[i][1]
    print("Output: {:.1f} deg".format(angle(h,m)))
    # res = "{:.1f}".format(angle(h,m))
    # print(float(res)==outputs[i])
    print()
