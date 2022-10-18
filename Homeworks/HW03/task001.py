# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_of_odd_pos_elements(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum

import random

def random_list_creator(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(0,9))
    return rand_list

try:
    num = int(input('Input amount of elements of list: '))
    list = random_list_creator(num)
    print(f'Here is the list of {num} random numbers: {list}')
    sum = sum_of_odd_pos_elements(list)
    print(f'Sum of elements with odd indices is: {sum}')

except:
    print('Your input should be integer number only!')

