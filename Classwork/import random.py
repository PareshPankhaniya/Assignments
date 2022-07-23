import random


num=random.randint(1,100)
print(num)

subject_list=("c","c++","java","python")
print(random.choice(subject_list))

subject_list=("c","c++","java","python")
random.suffle(subject_list)
print(subject_list)


