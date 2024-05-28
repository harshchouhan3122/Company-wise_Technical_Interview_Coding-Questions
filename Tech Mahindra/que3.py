# convert binary number to decimal number

'''
Basic Test Case:

Input: "1101"
Expected Output: 13
Zero Input:

Input: "0"
Expected Output: 0
Power of 2:

Input: "100000"
Expected Output: 32
Leading Zeros:

Input: "001010"
Expected Output: 10
Large Binary Number:

Input: "110110111001101101010"
Expected Output: 225498
All Ones:

Input: "111111111"
Expected Output: 511
Mix of Zeros and Ones:

Input: "101001101"
Expected Output: 333
'''

def decNum(binNum):
    res = 0
    num = list(str(binNum))
    num = num[::-1]
    for i in range(len(num)):
        if num[i] == "1":
            res += 2**i
    return res


# binNum = 1101
# print(decNum(binNum))


inputs = {
    1 : 1101,
    2 : 0,
    3 : 100000,
    # 4 : 0x001010,
    # 5 : 110110111001101101010,
    6 : 111111111,
    7 : 101001101
}

outputs = {
    1 : 13,
    2 : 0,
    3 : 32,
    4 : 10,
    5 : 225498,
    6 : 511,
    7 : 333
}

for i in inputs:
    print(f"Inputs : {inputs[i]}")
    print(f"Output : {decNum(inputs[i])}")
    print()