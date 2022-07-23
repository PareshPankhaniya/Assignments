num = int(input("Enter any integer number : "))

if num == 0:
    print(f"It's {num}")
elif num % 2 == 0:
    print(f"{num} is even")
elif num % 2 != 0:
    print(f"{num} is odd")

