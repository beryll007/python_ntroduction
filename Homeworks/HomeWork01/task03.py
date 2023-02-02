# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

ticket = ''
while len(ticket) != 6 or not ticket.isdigit():
    ticket = (input("Input your ticket number: "))
    
sum_1 = 0
sum_2 = 0
for i in ticket[:3]:
    sum_1 += int(i)
for i in ticket[3:]:
    sum_2 += int(i)

if sum_1 == sum_2:
    print('Your ticket will bring you a good luck!')
else: print('Throw this piece of paper away!')