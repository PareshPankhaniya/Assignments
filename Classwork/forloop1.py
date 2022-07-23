from operator import truediv


status =truediv
while status:
    marks=int(input("enter your matks"))
    if marks<35:
        print("fail")
        stauts=False
    else:
        print("pass")

