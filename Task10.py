# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
from random import randint

amount_coin = int(input('введите количество монет: '))

m = 0
k = 0
coins = [0, 1]
for i in range(amount_coin):
    random.shuffle(coins)
    print(f'эта монета упала  {coins}')
    if int(coins[0]) == 0:
        k += 1
    if int(coins[0]) == 1:
        m += 1
print(f'всего монет орёл, решка {m, k}')

if m > k:
    ans = k
else:
    ans = m

print(f"минимальное количество монет, которые нужно перевернуть :{ans}")

# n = int(input("Введите расклад монет:"))
# count_nol = 0
# count_ed = 0
# for i in range(n):
#     x = int(input())
#     print(x)
#     if x == 0:
#         count_nol += 1
#     else:
#         count_ed += 1
# if count_ed > count_nol:
#     print(count_nol)
# else:
#     print(count_ed)
