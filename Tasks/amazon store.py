data="""
                    1.press 1 for add items
                    2.press 2 for chech items
                    3.press 3 for remove items
                    4.press 4 for view items
        """

amazon_store=[]

print("Welcome to Amazon Store")
status=True
while status:
    print(data)
    choice=int(input("enter a choise:="))
    if choice==1:
        item_name=input("enter items:=")
        amazon_store.append(item_name) 
    elif choice==2:
        item_name=input("enter items:=")
        if item_name in amazon_store:
            print("avalible")
        else:
            print("not avalible") 
    elif choice==3:
        item_name=input("enter items:=")
        if item_name in amazon_store:
            amazon_store.remove(item_name)
        else:
            print("sorry item not exist")
    elif choice==4:
        print("total no of items in amazon store=",len(amazon_store))
        print("--------------------------")
        for  item in amazon_store:
            print(item)
    else:
        print("invalid input")
    user_choice=input("do you want to perfom more operations press 'y' for yes and  press 'n' for no ")
    if user_choice=='n' or user_choice=='no' or user_choice=='N':
            status=False
    else:
            status=True
