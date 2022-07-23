# write a python to check if a number is positive,negetive or zero.


import string


num = int(input("enter a number :"))
if num>=1:
        print("positive")
elif num==0:
        print("zero")
else:
            print("negetive")



 # write a python program to get the factorial number of given number.  

f=1
Num= int(input("enter a number")) 
if int(num)>=1:
        for i in range(1,int(num+1)):  
                f=f*i
                print("f is ",num,"is",f)  


# writw a python program to get the fibonacci series of given range.
n1=0
n2=1
limit=int(input("enter a number"))
print(n1)
print(n2)

count=2
while count<limit:
        n3=n1+n2
        n1=n2
        n2=n3
print(n3)
count=1
# write a python program that swap two number with temp variablr and without temp variablr.

a=10
b=20
a,b=b,A
print(a)
print(b)
# temp variable

temp=A
a=b
b=temp
print(a)
print(b)



#write a python program to find whether a given number is even or odd,print out  an appropeiatw message to the user.


num=int(input("enter a number"))
if num%2==0:
        print("num is even")
else:
        print("num is odd")





#write a python program to test whether a passed letter ia a vowel or not.

letter=input("enter a letter")
if letter=='a'or letter=='e' or letter=='i'or letter=='o' or letter=='u':
        print("it is vowel" )
else:
        print("it is not vowel")




#write a python program to sum of three given integers.however,if two values are equal sum will be zero.


num1=int(input("enter a number1"))
num2=int(input("enter a number2"))
num3=int(input("enter a number3"))
ans=num1+num2+num3
if num1==num2 or num1==num3 or num2==num3:
        print(0)
else:
        print(ans)



#write a python program to that  will return  true if the two given integervalues are equal or their sum of difference is 5.

num1=int(input("enter a number1"))
num2=int(input("enter a number2"))
ans1=num1+num2
ans2=num1-num2
if num1==num2 or ans1==5 or ans2==5:
        print("true")
else:
        print("false")


#write a python program to  sum of firast n positive intrgers.

n=int(input("enter a number"))
sum=(n*(n+1)/2)
print(sum)


#write a python program to length of string.

name=input("enter a name")
print(len(name))


# writw a python program to count the number of charaters(character frequency) in string.

na=input("enter a  string:=")
ch=input("enter search  character=:")
f=0
for i in na:
    if i == ch:
        f=f+1
print("length of string is",f)


#write a python program to count occurence of a substring in a string.




str1='hello hemaxi.hello python'
print()
print(str1.count("hello"))
print()

# write a python pogram  to count the occurence of  each word in given sentance.

str=input("enter  a string")
word=input("enter word:=")
a=[]
count=0
a=str.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
       count=count+1
print("count of the word is:")
print(count)


#write a python program to get a single string from two given strings,separated bt a space and swap the first two characters of each string.

a1='abc'
a2='xyz'
temp=a2
a2=a1[:2]+a2[2:]
a1=temp[:2]+a1[2:]
print(a2+' '+a1)

#write a python program to  add'ing'  at the end of a given  string(length should be a at lest 3.) if the given string already ends with 'ing' add 'ly'  instead if the string length of the given string is less than 3,leave if unchanged.


a1="string"
if len(a1)>=3:
        if a1[-3:]=="ing":
                a1=a1+'ly'
        else:
                a1=a1+'ing'
        print(a1)
else:
        print(a1)



# write a python program to find the first appearance of the substring'not' and'poor' from a given string,if not follows the 'poor',replace the whole 'not'....'poor' sunstring with 'good'.return the resulting string.
#write a python function that takes a list of words and returns the length of the longest one.


def find_longest_word(words_list):
        word_len=[]
        for n in words_list:
                word_len.append((len(n),n))
        word_len.short()
        return word_len[-1][1]
print(find_longest_word(["php","java","python"]))


#write a python program to  reverse get a string if its length is a multiple 4.


list_str=["java","python","php","code","tool"]
for str in list_str:
        if((len(str)%4)==0):
                print(str)


#write a python program to get a string made of the first 2 and the last 2 chars from a given a string.if the string length is lesa than 2,return instead of the empty string.



def strings_from_ends(str):
        if len(str)<2:
                return' '
        return str[0:2]+str[-2:]
print(strings_from_ends("hemaxipatel"))





#write a python function to insert a string i n the middele of a string.


def insert_string_middle(str,word):
        return str[:2]+word+ str[2:]
print(insert_string_middle('[[]]','python'))
print(insert_string_middle('{{}}','php'))
print(insert_string_middle('<<>>','html'))