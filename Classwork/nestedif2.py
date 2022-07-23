marks=int(input("enter your marks:="))
if marks >=0 and marks<=100:
    if marks>=70:
        print("a gread")
    elif marks>=60 and marks <70:
        print("b gread")
    elif  marks >=50 and marks<60:
        print("c gread")
    elif marks>=40 and marks<50:
        print("d gread")
    else:
        print("fail")
else:
    print("invalid input")