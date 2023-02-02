# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input('What is the size of your chocolate bar? Pieces in one side: '))
m = int(input('And in another side: '))
k = int(input(f'Your chocolate bar consist of {n*m} pieces. How many squares do you want to chip off your chocolate bar? '))

if k < n*m and (k%n == 0 or k%m == 0):
    print("Ok, and and which part will you leave to yourself now?")
else: 
    print("No, you can't split the chocolate bar like that")
