# Задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def uniq_elements(list):
    uniq_num = []
    for i in list:
        if i not in uniq_num:
            uniq_num.append(i)
    return uniq_num

import random

def random_list_creator(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(0,9))
    return rand_list


try:
    num = int(input('Input amount of elements of list: '))
    list = random_list_creator(num)
    print(f'Here is the list of {num} random numbers: \n{list}')
    result = uniq_elements(list)
    print(f'And here is the new list with uniq elements from the list above: \n{result}')
  
except:
    print('Your input should be integer number only!')