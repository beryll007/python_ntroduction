# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> не



# a = int(input("Input first number: "))
# b = int(input("Input second number: "))
# if a**2 == b or b**2 == a:
#     print("yes")
# else: print("no")

# try:      ### https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
#     number1 = int(input('Введите первое число: '))
#     number2 = int(input('Введите второе число: '))
#     if number1 ** 2 == number2:
#         print(f'{number2} является квадратом числа {number1}')
#     elif number2 ** 2 == number1:
#         print(f'{number1} является квадратом числа {number2}')
#     else:
#         print('Ни одно из числе не является квадратом другого')
# except:
#     print('Введите целое число')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

### 1
# num = [int(i) for i in input("Input five integer numbers separated by commas : ").split(', ')[:5]]
# max_num = num[0]
# for i in range(len(num)):
#     if num[i] > max_num:
#         max_num = num[i]
# print(num)
# print(max_num)

###2
# num = [int(i) for i in input("Input five integer numbers separated by commas : ").split(', ')]
# print(max(num))

###3
# print(max([int(i) for i in input("Input five integer numbers separated by commas : ").split(', ')]))

###4
# def create_list():
#     array = []
#     for i in 5:
#         value = int(input("Введите число: "))
#         array.append(value)
#     return array
# def find_max(array):
#     max = array[0]
#     for i in range(len(array)):
#         if array[i]>max:
#             max = array[i]
#     return max

# res = create_list()
# print(res)
# max = find_max(res)
# print(f"Максимальное значение в списке равно {max}")

###5
# try:
#     numbers = []
#     for i in range(5):
#         numbers.append(int(input(f'Введите число {i+1}: ')))
#     max_num = numbers[0]
#     min_num = numbers[0]
#     index_max = 0
#     index_min = 0
#     sum = 0
#     for i in range(len(numbers)):
#         sum += numbers[i]
#         if numbers[i] > max_num:
#             max_num = numbers[i]
#             index_max = i
#         elif numbers[i] < min_num:
#             min_num = numbers[i]
#             index_min = i
#     print('Максимальное число =', max_num, 'Индекс = ', index_max)
#     print('Минимальное число =', min_num, 'Индекс = ', index_min)
#     print('Среднее арифметическое = ', sum/len(numbers))
# except:
#     print('Введите целое число')

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input("Input integer number: "))
# for i in range (-n, n+1):
#     print(i, end=' ')

# N = 5
# spam = list(range(-N, N+1))
# print(spam)


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# num = float(input('Input float number: '))
# # print(int(num)) # прием отделения целой части дроби
# number = num*10
# if int(number%10) == 0:
#     print('No')
# else:
#   print(int(number%10))

## One more variant

# d = float(input('Input float number'))
# d1= int( (d*10) % 10 )
# print(d1)


# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Input number: '))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print("yes")
else:
    print('no')

### Homework: 

# #Task01

# # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# # Пример:
# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет

# day = int(input('Input number corresponding to the day of the week: '))
# if day in range(1,6):
#     print("This day is just usual day. Go to work!")
# if day in range(6,8):
#     print("Finally it's weekend! Chill!")
# else: print("Try another number from 1 to 7, where 1 is for Monday")

## Task02



