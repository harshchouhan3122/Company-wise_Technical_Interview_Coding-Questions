str1 = "Aloha Technology "
print(str1)

str2 = ""
for i in str1:
    str2 = i + str2
print(str2[1:])


str3 = ""
temp = ""
for i in str1:
    if i == " ":
        str3 = temp +" "+ str3
        temp = ""
        continue
    temp += i
print(str3)


str4=""
temp=""
for i in str1:
    if i == " " :
        str4 += temp + " "
        temp = ""
    temp = i + temp
print(str4)
    

str5 = ""
temp1=""
temp2=""
for i in str1:
    if i==" ":
        if len(temp1) > 5:
            str5 += temp1 + " "
        else:
            str5 += temp2 + " "
        temp1, temp2, count = "", "", 0
        continue
    temp1 = i+temp1
    temp2 = temp2+i
print(str5)