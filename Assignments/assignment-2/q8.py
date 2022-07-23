num1 = int(input("Enter any number for num-1 : "))
num2 = int(input("Enter any number for num-2 : "))


def demo(num1, num2):
    if (num1==num2) or (num1+num2==5) or (num1-num2==5):
        return True

print(demo(num1, num2))
