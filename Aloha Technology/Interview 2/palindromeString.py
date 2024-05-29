# Check the given string is palindrome or not

def checkPalindrome(string):
    res = ""
    for i in string:
        res = i+res
    if res == string:
        return True
    return False


inputs = {
    1: "abcba",
    2: "asdfdsa",
    3: "absvdf"
}


for i in inputs:
    print(f"Input : {inputs[i]}")
    print(f"Output : {checkPalindrome(inputs[i])}")
    print()