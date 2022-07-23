for i in range(1,6):
    even_count=0
    odd_count=0
    num=int(input("enter a  num"))
    print("num=",num)
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
    print("even count=",even_count)
    print("odd count=",odd_count)