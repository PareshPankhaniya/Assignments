string = input("Enter string : ")

if len(string) >= 2:
    print(string[:2] + string[-2:])
else:
    print('')