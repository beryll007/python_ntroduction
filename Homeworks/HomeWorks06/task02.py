# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import* 

my_list = []

for i in range(0,randint(5,30)):
    my_list.append(randint(-10,10))
print('Here is a randomly created list: ')
print(my_list)

bottom_range = int(input('Input lower bound of desired range: '))
top_range = int(input('Input abouve bound of desired range: '))

for i in range(len(my_list)):
    if my_list[i] >= bottom_range and my_list[i] <= top_range:
        print(i)