'''
INPUT: string = "axdixxyova"
OUTPUT: 4
- string1 = "axdixxyova"
- string2 = "axdixxyova"     # Its a reverse string of string1
- now we have to print the number of characters of string2 which are at the same position as of string1
'''

str1 = input("Enter any string: ")
count = 0

str2 = str1[::-1]

for i in range(len(str1)):
    if str1[i] == str2[i]:
        count += 1

print(str2)
print(count)