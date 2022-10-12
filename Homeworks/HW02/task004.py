# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.


try:
    faces = int(input('Input amount of dimensions of the space in which the distance between two points will be calculated: '))
    a_coord = []
    for i in range(faces):
        a_coord.append(int(input(f"Input coordinates of point A in {i+1} plane: ")))
    b_coord = []
    for i in range(faces):
        b_coord.append(int(input(f'Input coordinates of point B in {i+1} plane: ')))
    print(a_coord, b_coord)
    # diff_list = []
    sum = 0
    for i in range(faces):
        # diff_b_a = (b_coord[i] - a_coord[i])**2
        sum = sum + (b_coord[i] - a_coord[i])**2
        # diff_list.append(diff_b_a)
    dist = (sum)**0.5
    # print(diff_list)
    # print(sum)
    print(round(dist, 3))
except:
    print('Wrong input!')

