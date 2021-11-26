import random

goblet_list=int(input(""))
goblet_list=[]
for d in range(1, len(goblet_list)):
        d=random.randint(1,6)
        goblet_list.append(d)
        print(goblet_list)