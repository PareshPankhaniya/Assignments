str1 = input("Enter any string for str-1 : ")
str2 = input("Enter any string for str-2 : ")

new_str1 = str1[1] + str1[0] + str1[2:]
new_str2 = str2[1] + str2[0] + str2[2:]

print(new_str1 + " " + new_str2)