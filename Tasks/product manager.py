mobile_store={}
menu="""
                    menu

                    press 1 for product manager
                    press 2 for customer
"""
status='true'
while status:
    specification={}
    print(menu)
    role=int(input("choose your role(1/2 :"))
    if role==1:
        print("product manager:=")
        product_name=input("enter product name:=")
        model_num=input("enter model num:=")
        color=input("enter color name:=")
        qty=int(input("enter qty:="))
        price=int(input("enter price:="))

        specification["model"]=model_num
        specification["color"]=color
        specification["qty"]=qty
        specification["price"]=price

        mobile_store[product_name]=specification
        print(mobile_store)
    elif role==2:
        print("customer")

    choice=input("do yo want to continue: press 'y' for yes and press 'n'for no :")
    if choice=='n' or choice=='no':
        status=False
    for k in mobile_store.keys():
        print("----------------------------")
        print(f"\n\n\nproduct:{k}")
        print('---------------------------------')
        print("model:"+mobile_store[k]['model'])
        print("color:"+mobile_store[k]['color'])
        print("qty:"+str(mobile_store[k]['qty']))
        print("price:"+str(mobile_store[k]['price']))
        
status='true'
while status:
    specification={}
    print(menu)
if role==2:
    status='true'
    while status:
        specification={}
    print(menu)
    print("customer product:=")
    product_name=input("enter product name:=")
    model_num=input("enter model num:=")
    qty=int(input("enter qty:="))
    price=int(input("enter price:="))

    specification["model"]=model_num
    specification["qty"]=qty
    specification["price"]=price
    

    mobile_store[product_name]=specification
    print(mobile_store)
elif role==2:
        print("customer")

choice=input("do yo want to continue: press 'y' for yes and press 'n'for no :")
if choice=='n' or choice=='no':
        status=False
for k in mobile_store.keys():
        print("----------------------------")
        print(f"\n\n\nproduct:{k}")
        print('---------------------------------')
        print("model:"+mobile_store[k]['model'])
        print("qty:"+str(mobile_store[k]['qty']))
        print("price:"+str(mobile_store[k]['price']))
        

