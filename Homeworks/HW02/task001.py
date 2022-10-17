# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# Алгоритм получения цифр n-значного числа
# Несложно понять, по какому алгоритму можно найти каждую цифру n-значного числа num:

# Последняя цифра: (num % 10**1) // 10**0;
# Предпоследняя цифра: (num % 10**2) // 10**1;
# Предпредпоследняя цифра: (num % 10**3) // 10**2;
# .....
# Вторая цифра: (num % 10**n-1) // 10**n-2;
# Первая цифра: (num % 10**n) // 10**n-1.

# num = list(input('Input any real or integer number: '))
# print(num)
# if '.' in num:
#     num.remove('.')
# print(num)
# sum = 0
# list = []
# for i in range(len(num)):
#     sum = sum + int(num[i])
# print(sum)

# print(sum)

# def sum_of_digits(num):
#     sum = 0
#     if num < 0:
#         num *= -1
#     while int(num) != float(num): # не работает! 
#         num = num * 10
#         print(num)
#     while num > 0:
#         sum = sum + num % 10
#         num = num//10
#     return sum

# user_num = float(input('Input number: '))
# print(user_num)
# print(int(sum_of_digits(user_num)))


# num = float(123)
# print(type(num))
# while int(num) != float(num):
#     num = num * 10

# print(num)
# print(type(num))

# print(1.56 % 10)
# print(1.56 / 10)
# print(15.6 // 10)
 
# n = 0.56
# print(type(n))
# print(int(n))


# def number_of_digits_post_decimal(x):  
#     count = 0  
#     residue = x - int(x)  
#     # print(residue)
#     if residue != 0:  
#         multiplier = 1  
#         # while not (x*multiplier).is_integer():
#         while (x*multiplier) % 1 != 0: 
#             count += 1  
#             multiplier = 10 * multiplier 
            
#         return count

# print(number_of_digits_post_decimal(n))



# n = float(input('Введите число N: '))
# str_n = str(n)
# sum = 0

# for i in range(len(str_n)):
#     if str_n[i] == ',' or str_n[i] == '.':
#         j = len(str_n) - i - 1

# n_num = n * (10**j)

# for i in range(len(str_n) - 1):
#     sum = sum + n_num % 10
#     n_num = n_num // 10
# print(int(sum))

# a = 21345345.45623452346

# print(a%1)

def sum_of_digits(num):
    sum = 0
    if num < 0:
        num *= -1 
    inital_num = num    
    multiplier = 0
    while num % 1 != 0:
        num *= 10
        multiplier += 1
    num = inital_num * 10**multiplier
    # print(num)
    while num > 0:
        sum = sum + num % 10
        num = num//10
    return sum
    
try: 
    user_num = float(input('Input number: '))
    # print(user_num)
    print((f'Sum of digits of your number is: {int(sum_of_digits(user_num))}'))

except: 
    print('Your input should be integer or real number only!')