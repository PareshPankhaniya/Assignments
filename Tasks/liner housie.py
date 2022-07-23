from itertools import count
from random import random


import random
main_ticket=[]
count=0
while count<12:
    ticket=random.randint(1,100)
    if ticket not in main_ticket:
        main_ticket.append(ticket)
        count+=1
print(main_ticket)
