n = int(input('input your lenght of list:'))
my_list=[]
list_sort=[]
for i in range(n):
    print('number=',i)
    m= int(input('pleas enter your number:'))
    my_list.append(m)
    list_sort.append(m)
    
list_sort.sort()

if my_list==list_sort:

    print('this list is sorted')

else:
    print('this list is not sorted')