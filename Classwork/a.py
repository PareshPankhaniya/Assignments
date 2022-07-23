import email


firstname="hemaxi patel"
email="hemaxipatel754@gmail.com"
password="12345678"



email_1=input("enter your email:=")
password_2=input("enter your password:=")
if email==email_1 and password==password_2:
    print("first name")
elif email!=email_1 and password!=password_2:
    print("you are entred wrong email and password")
elif email!=email_1 and password==password_2:
    print("wrong email")
elif email==email and len(password_2)<8:
    print("please entred password 8 digits")
else:
    print("wrong entry")