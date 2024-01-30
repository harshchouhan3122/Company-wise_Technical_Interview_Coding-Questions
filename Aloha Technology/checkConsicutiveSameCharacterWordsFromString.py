#  Print the words from the given string, which has same consecutive characters

# str1 = "it is a bright day"
str1 = "an apple a days keeps doctor away"

# str1 = input()
str1 += " "

res = [] 
word = " "

flag = False

for i in str1:

    if i == word[-1]:
        flag = True

    if i == " " :
        if flag==True:
            res.append(word[1:])

        else:
            word = " "

        flag = False
        continue

    word += i

print(res)
