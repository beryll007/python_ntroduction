# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint
import time

coins = []
coins_amount = int(input('How many coins would you like to throw on the table? '))
for i in range(coins_amount):
    coins.append(randint(0,1))

for coin in coins:
    print(coin, end=' ', flush=True)
    time.sleep(0.2)

heads = 0
tails = 0
for i in coins:
    if i == 1:
        heads += 1
    else: 
        tails += 1
print()

if heads > tails:
    print(f'You need to turnover {tails} coins')
else: print(f'You need to turnover {heads} coins')
        
 
    

