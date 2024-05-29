# Count the character in the string

def charCount(string):
    res = {}
    for i in string:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res



inputs = {
    1: "abcba",
    2: "asdfdsa",
    3: "absvdf",
    4: ":aaammffk"
}


for i in inputs:
    print(f"Input : {inputs[i]}")
    print(f"Output : {charCount(inputs[i])}")
    print()