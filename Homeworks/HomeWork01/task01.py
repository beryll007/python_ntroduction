# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример: 123 -> 6(1+2+3); 100 -> 1(1+0+0)

num = int(input("Введите трехзначное число: "))

first_digit = num//100
second_digit = (num//10) % 10
third_digit = num % 10
print(f'{first_digit} + {second_digit} + {third_digit} = {first_digit + second_digit + third_digit}')


