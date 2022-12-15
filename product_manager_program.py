menu = """

            MENU 

        press 1 for product manger
        press 2 for customer 
        press 3 for exit

        """
products = {}
my_cart = {}

def product_manager_ac():    
            product_name = input("Enter product name : ")
            qty = int(input("Enter no. of qty : "))
            price = int(input("Enter price : "))

            spec['qty'] = qty 
            spec['price'] = price
            if product_name in products:
                old_qty = products[product_name]["qty"]
                spec['qty'] = qty + old_qty
                spec['price'] = price
                products[product_name] = spec
            else:
                products[product_name] = spec

            print(products)

def customer_ac():
    total = 0 
    status = True 
    while status:
        spec = {}
        print("-------------------  PRODUCT  LIST  ---------------- ")
        for k in products.keys():
            price = products[k]['price']
            print(f" {k}  -  Rs. {price} ")
        else:
            print("----------------------------------- ")

        product_name = input("Enter product which you want to purchase : ")
        if product_name in products.keys():
            qty = int(input("Enter no. of qty do you want : "))
            main_qty = products[product_name]["qty"]
            if qty<main_qty:
                price = products[product_name]["price"]
                print("price will be : ",price*qty)
                main_qty -= qty
                products[product_name]["qty"] = main_qty
                spec['qty'] = qty # customer side qty 
                spec['price'] = qty*price
                my_cart[product_name] = spec
            else:
                print("stock not available")
        else:
            print("Product not available")
        choice = input("do you want more product : press 'y' for yes and press 'n' for no : ")
        if choice == 'y':
            status = True 
        else:
            print("-------------------  MY CART  ---------------- ")
            for k in my_cart.keys():
                qty = my_cart[k]['qty']
                price = my_cart[k]['price']
                total += price
                print(f" {k}  : {qty} =  Rs. {price} ")
            else:
                print("----------------------------------- ")
                print(f"TOTAL PAYBALE AMOUNT WILL BE : {total}")
            status = False

status = True 
process = True
while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        while process:
            spec = {}
            product_manager_ac() 
            ch = input("do you want to add more products : press 'y' for yes and press 'n' for no : ")
            if ch=='y':
                process = True
            else:
                process = False
    elif choice==2:
        print("Customer")
        customer_ac()
        pass
    else:
        print("THANK YOU FOR USING THIS APPLICATION ")
        status = False
    program_status = input("Do you want to go main menu : press 'y' for yes and press 'n' for no :  ")
    if program_status=='y':
        status = True
    else:
        status = False

