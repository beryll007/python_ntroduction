# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def create_equation(k):
    equation = ''
    for i in range(k, 0, -1):
        if i > 1:
            coeff = (randint(0,100))
            if coeff > 1:
                equation = equation + str(coeff) + '*x^' + str(i) + ' + ' 
            elif coeff == 1:
                equation = equation + 'x^' + str(i) + ' + '
            elif coeff == 0:
                equation = equation

        elif i == 1:
            x_coeff = (randint(0,100))
            if x_coeff > 1:
                equation = equation + str(x_coeff) + '*x' + ' + ' + str(randint(1,100)) + ' = 0'
            elif x_coeff == 1:
                equation = equation + 'x' + ' + ' + str(randint(1,100)) + ' = 0'
            elif x_coeff == 0:
                equation = equation + str(randint(0,100)) + ' = 0'
             
    return equation

def save_in_file (string):
    with open('II четверть/Знакомство с языком Python/Homeworks/HW04/task3.txt', 'w') as file:
        file.write(string)
    print('Polynomial has been saved in file!')

try:
    num = int(input('Input the degree of the polynomial: '))
    while num < 1:
        print('Unable to create such polynomial!')
        num = int(input('Try to input natural number: '))
     
    polynomial = create_equation(num)
    print(f'Here is your polynomial: {polynomial}')
    save_in_file(polynomial)

except:
    print('Your input should be natural number!')





   


