string = input("Enter an string : ")

if len(string) >= 3:
    if string[-3:] == 'ing':
        print(f"New string : {string + 'ly'}")
    else:
        print(f"New string : {string + 'ing'}")
else:
    print(f"{string}")

