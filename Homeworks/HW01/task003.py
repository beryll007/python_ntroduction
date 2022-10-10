# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    x = int(input('Input position on X-axis: '))
    y = int(input('Input position on Y-axis: '))
    if x == 0 or y == 0:
        print('Try a non-zero values for coordinates')
    elif (x > 0  and y > 0):
        print('The point locates in the 1st quarter')
    elif (x < 0 and y > 0):
        print('The point locates in the 2nd quarter')
    elif (x < 0 and y < 0):
        print('The point locates in the 3d quarter')
    else:
        print('The point locates in the 4th quarter')
except:
    print('Try to input integer number')