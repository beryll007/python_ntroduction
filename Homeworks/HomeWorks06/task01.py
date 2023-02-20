# Задача 30: 
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print('This algorythm is designed to create an array and fill it with elements in arithmetic progression')

a1, d, n = int(input('Input the first element: ')), int(input('Input difference in arithmetic progression: ')),int(input('Input amount of elements: '))

ap = []
for i in range(n):
    ap.append(a1 + i*d)
print(ap)

