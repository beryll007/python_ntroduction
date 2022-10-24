# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



def factoring(num):
    i = 2 # первое простое число
    mult_list = []

    while i <= num:
        if num % i == 0:
            mult_list.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return mult_list

try: 
    num = int(input("Input any natural number for factoriztion: "))
    while num < 1:
        num = int(input("Input any natural number for factoriztion: "))
    else:
        result = factoring(num)
        print(f'Here is the list of prime factors of your number {num} : {result}')
except:
    print(f'Your input should be integer positive number only!')

