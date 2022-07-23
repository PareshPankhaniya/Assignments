positive_count=0
negetive_count=0
for i in range(1,6):
    no=int(input("enter a num="))
    print("no=",no)
    if no>=0:
        positive_count+=1
    else:

        negetive_count+=1
print("positive count=",positive_count)
print("negetive count=",negetive_count)
