# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def dec_to_bin_converter(n):
    m = ''
    while n > 0:
        m = str(n % 2) + m
        n = n//2
    return (int(m))

try:
    n = int(input('Input number in decimal notation to convert it into binary notation: '))
    num_bin = dec_to_bin_converter(n)
    print(f'Number {n} in decimal system is {num_bin} in binary number system')
except:
    print('Try to input any number in decimnal number system.')