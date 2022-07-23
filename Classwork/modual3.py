#Write a Python function to get the largest number, smallest num and sumof all from a list





list=[23,45,67,89,80,90]

# print(max(list))
# print(min(list))
# print(sum(list))






'''Write a Python program to count the number of strings where the stringlength is 2 or more and the first and last 
character are same from a givenlist of strings.'''


list=['abc','dbd','ggg','lac','rde']
count = 0

for i in list:
       if (len(i) > 2) and (i[0] == i[-1]):
              count += 1

print(count)




#Write a Python program to remove duplicates from a list.



l1=[12,34,55,67,44,55,12]
print(l1)
l2=[]
for i in  l1():
       if  i not in l2:
              l2.append(i)
print(l2)


# Write a Python program to check a list is empty or not.

list=[]
if len(list)==0:
       print(" list is Empty" )
else:
       print("list is  not empty")



# Write a Python function that takes two lists and returns true if they have at least one common member.

def compare(l1,l2):
       for i in range(len(l1)):
              if l1[i] in l2:
                     return True
              return False
print(compare([1,2,4],[4,5,6]))

#Write a Python program to generate and print a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30.

def  value():
       l=list()
       for i in range(1,30):
              l.append(i**2)
       print(l[:5])
       print(l[-5:])
value()



# Write a Python function that takes a list and returns a new list with uniqueelements of the first list.


def  list(l):
       a=[]
       for i in l:
              if i not in a:
                     a.append(i)
       return a
print(list([1,2,3,3,3,4,5,]))



# Write a Python program to convert a list of characters into a string.


s=['a','b','c','d']
str1=' '.join(s)
print(str1)


# Write a Python program to select an item randomly from a list.

import collections
from itertools import product
import random
color_list=['red','white','yellow','black']
print(random.choice(color_list))



# Write a Python program to find the second smallest number in a list

list = [23,45,64,85,25,335,443,23,35,3,35,533]
list.sort()
print("secound smallest number is",list(1))



#Write a Python program to get unique values from a list

l1=[1,4,5,3,2,3,4,5,4]
list=[]
for i in l1:
       if i not in list:
              list.append(i)
print(list)




#  Write a Python program to check whether a list contains a sub list


list=['a','w',[1,2,3,'hemaxi patel']]
for i in list:
       if len(i)>1:
              print("sublist is present in list")
              break
else:
       print("sublist is not present in list")









#  Write a Python program to split a list into different variables.



color=[('love','yes','no'),('valentine','no','yes'),('day','yes','yes')]
Variable1,Variable2,Variable3=color
print(Variable1)
print(Variable2)



#  Write a Python program to create a tuple with different data types.

#  Write a Python program to create a tuple with numbers.


tuple=5,10,15,20,25,30
print(tuple)
tuple=10,
print(tuple)



#  Write a Python program to convert a tuple to a string.
t=('h','e','m','a','x','i')
str=''.join(t)
print(str)



#  Write a Python program to check whether an element exists within atuple.

t=("w",3,"r","e","s","o","u","r","c","e")
print("r" in t)
print(5 in t) 

#  Write a Python program to find the length of a tuple.

t=("hemaxipatel")
print(t)
print(len(t))




#  Write a Python program to convert a list to a tuple.


list=[1,2,3,4,5,6,7,8]
print(list)
t=list
print(t)



#  Write a Python program to reverse a tuple.

x=(1,2,3,4,5)
result=reversed(x)
result=tuple(result)
print(result)

#  Write a Python program to replace last value of tuples in a list.

l=[(10,20,30),(40,50,60,),(70,80,90)]
print([t[:-1]+(100,)for t in l])




#  Write a Python program to find the repeated items of a tuple.

t=(1,2,3,4,5,6,7,8,6,6,6,6,6,)
print(t)
count=t.count(6)
print(count)





#  Write a Python program to remove an empty tuple(s) from a list of tuples.





l=[(1,2,3),(4,5),()]
for tuple in l:
       if (len(tuple)==0):
              l.remove(tuple)
print(l)





#  Write a Python program to unzip a list of tuples into individual lists.

l=[(1,2),(3,4),(5,6)]
print(list(zip(*l)))




#  Write a Python program to convert a list of tuples into a dictionary.














#  Write a Python script to sort (ascending and descending) a dictionary byvalue.
from operator
d={'python':90,'cpp':100,'java':80,'php':60}
print("original dictionary:=",d)
asending=dict(sorted(d.items(),key=operator.item(1)))
print(asending)
disending=dict(sorted(d.items(),key=operator.item(1),reverse=True))
print(disending)





#  Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dic4={}
for d in (dic1,dict2,dict3):dic4.update(d)
print(dic4)

#  Write a Python script to check if a given key already exists in a dictionary.


d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
       if x in d:
              print("key is present in the dictionary")
       else:
              print("key is not present in the dictionary")
is_key_present(5)
is_key_present(9)







#  Write a Python script to print a dictionary where the keys are numbers between 1 and 15.


d=dict()
for x in range(1,16):
       d[x]=x**2
print(d)


#  Write a Python program to check multiple keys exists in a dictionary

student={'name':'hemaxi','class':'b','roll no':'3'}
print(student.keys()>={'class','name'})
print(student.keys()>={'name','hemaxi'})
print(student.keys()>={'roll no','name'})



#  Write a Python script to merge two Python dictionaries



d1={'a':100,'b':200}
d2={'x':300,'y':200}
d=d1.copy()
d.update(d2)
print(d)



#  Write a Python program to map two lists into a dictionary

keys=['red','green','black']
Values=['#ff0000','#008000','#0000ff']
color_dictionary=dict(zip(keys>Values))
print(color_dictionary)


#  Write a Python program to combine two dictionary adding values forcommon keys.
# o d1 = {'a': 100, 'b': 200, 'c':300}
# o d2 = {'a': 300, 'b': 200,’d’:400}


from collections import counter

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d=counter(d1)+counter(d2)
print(d)




#  Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

from collections import counter

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d=counter(d1)+counter(d2)
print(d)





#  Write a Python program to print all unique values in a dictionary.


dict={'511':'vishnu','512':'vishnu','513':'ram','514':'ram','515':'sita'}
list=[]
for val in dict.values():
       if val in list:
              continue
       else:
              list.append(val)
print(list)




# Write a Python program to create and display all combinations of letters,selecting each letter from a different key in a dictionary

from itertools import product
d={'1':['a','b'],'2':['c','d']}
for x,y,in product(*d.values()):
       print(x+y)







#  Write a Python program to find the highest 3 values in a dictionary

from heapq import nlargest
my_dict={'a':500,'b':5874,'c':560,'d':400,'e':5874,'f':20}
three_largest=nlargest(3,my_dict,key=my_dict.get)
print(three_largest)






#  Write a Python program to combine values in python list of dictionariesSample data: 


from collections import Counter
item_list=[{'item': 'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
result=counter()
for d in item_list:
       result[d['items']]+=d['amount']
print(result)




#  Write a Python program to create a dictionary from a string.
#  Write a Python function to calculate the factorial of a number (a nonnegative integer)
#  Write a Python function to check whether a number is in a given range
#  Write a Python function to check whether a number is perfect or not.
#  Write a Python function that checks whether a passed string is palindromeor not
#  Write a Python program to read a random line from a file.
#  Write a Python program to convert degree to radian
#  Write a Python program to calculate the area of a trapezoid
#  Write a Python program to calculate the area of a parallelogram
#  Write a Python program to calculate surface volume and area of a cylinder
#  Write a Python program to returns sum of all divisors of a number
#  Write a Python program to find the maximum and minimum numbersfrom the specified decimal numbers