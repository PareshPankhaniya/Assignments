string = input("Enter string : ")

if len(string) % 4 == 0:
    print(f"String in reverse : {string[::-1]}")
else:
    print(f"String as normal : {string}")
