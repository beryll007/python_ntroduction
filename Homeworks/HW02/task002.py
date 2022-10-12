# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# try:    
#     n = int(input('Input integer number: '))
#     mult = 1
#     list = []
#     for i in range(1,n+1):
#         mult = mult*i
#         list.append(mult)
#     print(list)
# except:
#     print("Use only INTEGER number!")


def fac(num):
    if num > 0:
        mult = 1
        list = []
        for i in range(1, num + 1):
            mult *= i
            list.append(mult)
    else:
        list = [0]
    return(list)

try:
    user_num = int(input('Input integer number: '))
    print(fac(user_num))
except:
    print('Your input should be integer number!')


    
