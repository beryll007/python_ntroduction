# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.001, 1.2, 3.3, 5, 10.01]

def fract_diff(list):
    new_list = []
    for i in range(len(list)):
        if list[i]%1 != 0:
            new_list.append((list[i]%1))
    # print(new_list)
    max = new_list[0]
    min = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] > max:
            max = new_list[i]
        if new_list[i] < min:
            min = new_list[i]   
    return(max - min)
        
print(round((fract_diff(list)),3))

