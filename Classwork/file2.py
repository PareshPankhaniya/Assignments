"""
r : read mode
w : write mode
a : append mode
"""

f=open("example.txt","r")

l1=f.readlines ()
print("---------->",l1)
print("no.of lines in file:",len(l1))



print("1rd line of file",l1[0])