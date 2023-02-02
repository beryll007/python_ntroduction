# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from random import randint

x = int(randint(1,1000))
y = int(randint(1,1000))
s = x + y
p = x * y
print(f'Sum of hidden numbers is {s}')
print(f'Product of hidden numbers is {p}')

for i in range(1,1001):
    for j in range(1,1001):
        if i + j == s and i * j == p:
            hid_num1 = i
            hid_num2 = j
print(hid_num1, hid_num2)

# print(x, y)