
from collections import Counter
item_list=[{'item': 'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
result= counter()
for d in item_list:
       result[d['items']]+=d['amount']
print(result)