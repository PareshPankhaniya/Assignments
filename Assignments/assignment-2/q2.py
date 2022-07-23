from attr import Factory


num = int(input("Enter any number to know there factorial number : "))

def facto(num):
    if num == 1:
        return 1
    elif num < 1:
        return "Print num greater than 1"
    else:
        return num * facto(num-1)


print(facto(5))