from random import*
menu = """
         menu

    press 1 for generate note
    press 2 for view note
    press 3 for exit
"""
print(menu)
status = True
process = True
while status:
    print(menu)
    name = int(input("enter your choice number  :"))
    if choice ==1:
        while process:
            spec = {}
            name=int(input("enter E-genrator name : 898 "))
            if name =='y':
                process = True
            elif choice == 1:
                process = False
            print("--> invalied input ") 
    choice = (input("enter E-notebook name : anjli patel"))
    if choice ==2:
        while process:
         spec = {}
         if name=='y':
            process = True
         elif choice == 2:
            process = False
    choice = (input("enter E-notebook title  : python introduction "))
    if choice ==3:
      while process:
         spec = {}
         if name=='y':
            process = True
         elif choice == 3:
            process = False
    choice = (input("enter E-notebook content  : python high level programming language "))
    if choice ==4:
      while process:
        spec = {}
        if name=='y':
            process = True
        elif choice == 4:
            process = False        
    choice = input("do you want to enter name again press 'y' for yes and press 'n' for no :")
    if choice == 'y':
        status = True
    else:
        status = False
      
   

