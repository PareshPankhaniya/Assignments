product=[]
qty_list=[]
price=[]
data="""
                welcome to jay bhvani

                vadapav    30
                dabeli     30
                bhel       70
    """
print(data)
for i in range(1,3):
    product_name=input("enter your product:=").upper()
    qty=int(input("enter no.qty do you want:="))
    if product_name=="vadapav" or product_name=="dabeli":
        prive_value=30
        total_price=prive_value*qty
    product.append(product_name)
    qty_list.append(qty)
    price.append(total_price)
    for i in range(0,len(product)):
        print(f"{product[i]} {qty_list[i]}= {price[i]}")
    print("---------------REMOVE PRODUCT----------")
    product_name=input("enter product which you want to remove:").upper()
    position=product.index(product_name)
    product.pop(position)
    qty_list.pop(position)
    price.pop(position)
    for i in range(0,len(product)):
        print(f" {product[i]} {qty_list[i]}={price[i]}")