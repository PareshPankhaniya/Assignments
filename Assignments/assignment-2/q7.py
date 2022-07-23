num1 = int(input("Enter any number for num-1 : "))
num2 = int(input("Enter any number for num-2 : "))
num3 = int(input("Enter any number for num-3 : "))
sum = 0

if num1==num2 or num2==num3 or num1==num3:
    print(f"sum : {sum}")
else:
    sum = num1 + num2 + num3
    print(f"sum : {sum}")
