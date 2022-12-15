import random
rl=[]
while len(rl) in range(12):
  random_number=random.randint(1,101)
  if random_number not in rl:
    rl.append(random_number)
for n in rl:
  print(n,end=' ')
USER=rl[0:6]
COMPUTER=rl[6:]
print("\nUSER")
for n1 in USER:
  print(n1,end=" ")
print("\nCOMPUTER")
for n2 in COMPUTER:
  print(n2,end=" ")
random.shuffle(rl)
ln=rl
status=True
while status:
  for i  in ln:
    print("\n LUCKY NUMBER : ",i)
    print("\n")
    if i in USER:
      USER.remove(i)
      print("USER")
      for i1 in USER:
        print(i1,end=" ")
      print("\n")
      print("COMPUTER")
      for i2 in COMPUTER:
        print(i2,end=" ")
      print("\n")
      ln.remove(i)
      if len(USER) ==0:
        print("USER is the winner")
        status=False
    else:
      COMPUTER.remove(i)
      print("COMPUTER")
      for i2 in COMPUTER:
        print(i2,end=" ")
      print("\n")
      for i1 in USER:
        print(i1,end=" ")
      print("\n")
      ln.remove(i)
  if len(ln) ==0:
    status=False

