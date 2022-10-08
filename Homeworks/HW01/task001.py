 #Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def day_off_check(day):
#     try: 
#         if day in range(1,6):
#             print('This is not a day-off, go to work! ')
#         elif day in range(6,8):
#             print("It's a day-off, take a rest. ")
#         else:
#             print('Try another integer number from 1 to 7, where 1 is for monday')
#     except:
#         print('Try to input integer number')

# day = int(input('Input integer number representing the day of the week: '))

# day_off_check(day)



day_off = [6,7]
week_day = [1,2,3,4,5]
your_day = (input('Input integer number representing the day of the week: '))
try: 
    if int(your_day) in day_off:
        print('yes')
    elif int(your_day) in week_day:
        print('no')
    else:
        print('there is no such day in a week')
except:
    print("Try to input integer number from 1 to 7, where 1 is for Monday")


