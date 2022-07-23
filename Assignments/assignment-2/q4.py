a1, b1, swap1 = 6,4,0
swap1 = a1
a1 = b1
b1 = swap1

print("-------- Swaping with temp variable --------")
print(f"a1 : {a1}")
print(f"b1 : {b1}")


print("\n\n-------- Swaping without temp variable --------")
a1,b1 = b1,a1
print(f"a1 : {a1}")
print(f"b1 : {b1}")
