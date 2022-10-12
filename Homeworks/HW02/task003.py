# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

first_str = input('Input the first string: ')
second_str = input('Input the second string: ')

count = 0
if len(first_str) > len(second_str):
    for i in range(len(first_str)):
        if first_str[i:i+len(second_str)] == second_str:
            count += 1
else:
    for i in range(len(second_str)):
        if second_str[i:i+len(first_str)] == first_str:
            count+=1

print(count)


