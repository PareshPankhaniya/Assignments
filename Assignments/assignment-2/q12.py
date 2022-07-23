from itertools import count

string = "Paresh Pankhaniya"
substring = input("Enter substring you want to find occurence of in string : ")

if substring in string:
    print(f"Total occurence of {substring} : {string.count(substring)}")
else:
    print("Entered substring doesn't exist in string")