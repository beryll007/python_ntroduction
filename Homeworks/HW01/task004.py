# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

# print("this algorythm is an example of simple calcualtor. You'll be asked to input three ")


try:
    first_num = float(input("Input first number: "))
    second_num = float(input("Input second number: "))
    operation = input("Input one of the supported operations which are the following: +, -, /, *, mod, pow, div: ")
    if operation == '+':
        print(first_num+second_num)
    elif operation == '-':
        print(first_num-second_num)
    elif operation == '/':
        if second_num == 0:
            print('divide by zero error!')
        else:
            print(first_num/second_num)
    elif operation == '*':
        print(first_num*second_num)
    elif operation == 'mod':
        if second_num == 0:
            print('divide by zero error!')
        else:
            print(first_num%second_num)
    elif operation == 'pow':
        print(first_num**second_num)
    elif operation == 'div':
        print(first_num//second_num)
except:
    print("Wrong input!")


