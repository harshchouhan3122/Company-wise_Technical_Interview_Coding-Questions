# Check the first repeating character in the string

def checkRepeat(string):
    res = {}
    sym = [" ", ",","%"]
    for i in string :
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1

        if res[i] == 2 and i not in sym:
            return i
        
    return res

inputs = {
    1: "abc def bac",
    2: "asdfdsa",
    3: "absvdf",
    4: ":aaammffk"
}


for i in inputs:
    print(f"Input : {inputs[i]}")
    print(f"Output : {checkRepeat(inputs[i])}")
    print()