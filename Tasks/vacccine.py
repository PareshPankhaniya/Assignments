import datetime

d = datetime.datetime.now()
d= (str)(d.date())
file = open(d,'a')

while True:
    file.write(f'today date is : {d}')
    n  =input('enter your name:')
    file.write(f'\nyour name is: {n}\n')
    g  =input('enter your gender:')
    file.write(f'\nyour gender is: {g}\n')
    a =input('enter your age:')
    file.write(f'\nyour age is: {a}\n')
    contact=int(input('enter your number:'))
    file.write(f'\nyour number is: {contact}\n')

    doze =int(input('enter vaccination doze:'))
    file.write(f'\n doze is: {doze}\n')
    print("Enter 1 for Covieshild\n2. for covaxin.")
    vaccine =input('enter your vaccine name:')
    a = 'covishield'
    b = 'covaxine'
    if vaccine == '1':
        file.write(f'\n your vaccine is: {a}\n')
    else:
  …
  break

file.close()