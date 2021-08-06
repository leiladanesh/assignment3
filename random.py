import random

list_data=[]

n =int(input())
while n != len(list_data):
    my_list=random.randint(1,n)

    if my_list not in list_data:
  
        list_data.append(my_list)


print(list_data)
result=list(dict.fromkeys(list_data))
print(result)
