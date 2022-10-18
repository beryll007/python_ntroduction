# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def random_list_creator(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(0,9))
    return rand_list

def mirror_multiplication(list):
    prod_list = []
    for i in range((len(list)+1)//2):
        prod_list.append(list[i]*list[-(i+1)])
    return prod_list

try:
    num = int(input('Input amount of elements of the list: '))
    my_list = random_list_creator(num)
    print(f'Here is the list of {num} randomly chosen numbers: \n{my_list}')
    print(f'And here is the list where i multiplied the first and the last element and the second with the second to the last and so on pairwise: \n{mirror_multiplication(my_list)}')
except:
    print('Your input should be integer number only!')
