#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in (True,False):
    for y in (True,False):
        for z in (True,False):
            print(f'if x is {x}, y is {y}, z is {z} : the statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is {not(x or y or z) == (not x and not y and not z)}')
            