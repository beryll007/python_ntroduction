# # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# total_cranes = int(input("How many paper cranes was made in total? "))

# petya = int(total_cranes / 6)
# serezha = int(petya)
# katya = int(2*(petya+serezha))

# if petya + serezha + katya != total_cranes:
#     print("I can not solve this!")
#     print(f'i do not know who made {total_cranes - (petya+katya+serezha)} of {total_cranes} cranes')
# elif petya + serezha + katya == total_cranes:  
#     print(petya, katya, serezha)


s = int(input('How many paper cranes was made in total? '))
flag = False
for a in range(s):
    for b in range(s):
        for c in range(s):
            if a == b and (a + b) * 2 == c and a + b + c == s:
                print(a, c, b)                
                flag = True
if flag != True:
    print("no answer")