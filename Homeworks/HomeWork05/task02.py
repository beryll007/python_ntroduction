# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""

from random import *
import time

def start():
    name = "Hey! What's your name? "
    for i in name:
        time.sleep(0.1)
        print(i, end = '', flush = True)
    player = input()

    first_message = f"Hi, {player}! I'd like to play one game with you. It's quite easy. Will you play with me?\n"
    for i in first_message:
        time.sleep(0.1)
        print(i, end = '', flush = True)
    
    agreement = input('Y or N:')
    
    while agreement not in ('Y', 'y', 'N', 'n'):
        agreement = input('Y or N:')
    
    else:
        if agreement == 'Y' or agreement == 'y':
            second_message = "There are 2021 sweets on the table.\nEach player is allowed to take from 1 to 28 sweets by turn.\nThe one who takes the last sweets wins.\n"
            for i in second_message:
                time.sleep(0.1)
                print(i, end = '', flush = True)
        if agreement == 'N' or agreement == 'n':
            second_message = f"Ok, {player}! But you have to play with me anyway!\n"
            for i in second_message:
                time.sleep(0.1)
                print(i, end = '', flush = True)
            
    # print(f"I'd like to play one game with you")
    # print(f'There are 2021 sweets on the table')
    # print(f'Each player is allowed to take from 1 to 28 sweets by turn')
    # print(f'The one who takes the last sweets wins ')
    print('*' * 100)
    return player

def rnd_turn(player):
    message = f"Let's flip to see who goes first!\n"
    for i in message:
        time.sleep(0.1)
        print(i, end = '', flush = True)
    print()
    # coin = '()'
    # print('() | () | () | ()')
    n = randint(0, 1)
    if n == 0:
        print(f'{player} goes first!')
    else:
        print(f'AI goes firs!')
    return n

def level_to_choose():
    message = "Pick the difficulty level and try to defeat the AI\nInput H for Hard mode and L for Light mode:"
    for i in message:
        time.sleep(0.05)
        print(i, end = '', flush = True)
    # print(f'Pick the difficulty level and try to defeat the AI')
    # print(f'Input H for Hard mode and L for Light mode:')
    while True:
        level = input()
        if level not in ('H','h','L', 'l'):
            print('Input H or L')
        else:
            if level == 'L' or level == 'l':
                level = 0
                # print("You've picked the Light Mode. It shouldn't be very difficult")
                message = "You've picked the Light Mode. It shouldn't be very difficult\n"
                for i in message:
                    time.sleep(0.05)
                    print(i, end = '', flush = True)
            if level == 'H' or level == 'h':
                level = 1
                message = "You've picked the Hard Mode. Good luck!'\n"
                for i in message:
                    time.sleep(0.05)
                    print(i, end = '', flush = True)
                # print("You've picked the Hard Mode. Good luck!")
            break
    return level

def turn_player(sweets):
    n = 29
    while n > 28 or n < 1:
        n = input('How many sweets do you take? ')
        if n.isdigit():
            n = int(n)
            if n > 28 or n < 1:
                print(f"You're not allowed to take {n} sweets! Take from 1 to 28")
            # проверка на остаток
            if n > sweets:
                print(f'There is no so many sweets on the table left!')
                n = 29
        else:
            print(f'Wrong input! Enter the number from 1 to 28!')
            n = 29
    return n

def turn_ai_hard(sweets):
    n = sweets % 29
    if n == 0:
        n = randint(1, 28)
    return n

def turn_ai(mathces):
    n = randint(1, 28)
    return n


# name = "Hey! What's your name? "
# for i in name:
#     time.sleep(0.1)
#     print(i, end = '', flush = True)
# player = input()

# first_message = f"Hi {player}! I'd like to play one game with you\nThere are 2021 sweets on the table\nEach player is allowed to take from 1 to 28 sweets by turn\nThe one who takes the last sweets wins\n"
# for i in first_message:
#     time.sleep(0.1)
#     print(i, end = '', flush = True)
#     print('*' * 100)

sweets = 2021
count = 1
name = start()


level = level_to_choose()
turn = rnd_turn(name)
while True:
    print(f'\n>>>>>>>>>> Round: {count} <<<<<<<<<<')
    if turn % 2 == 0:
        time.sleep(0.5)
        print(f"{name}'s move! There are {sweets} sweets left")
        n = turn_player(sweets)
        print(f'{name} is taking {n} sweets')
    elif turn % 2 == 1:
        time.sleep(0.5)
        print(f"AI's turn! There are {sweets} sweets left")
        if level == 1:
            n = turn_ai_hard(sweets)
            print(f'AI is taking: {n}')
        else: 
            if sweets <= 28:
                n = sweets
            else:
                n = turn_ai(sweets)
            print(f'AI is taking: {n}')
    sweets -= n
    if sweets == 0:
        if turn % 2 == 0:
            print(f'{name} wins!')
        else:
            print(f'AI wins!')
        break
    turn += 1
    count += 1






