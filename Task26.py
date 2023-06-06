# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def exponentiator(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    elif b > 0:
        return a * exponentiator(a, b - 1)
    else:
        return 1 / (a * exponentiator(a, -b - 1))
    
a, b = map(int, input("Введите число a > 0 и целое число b: "). split())
print(f'{a} ^ {b} = {exponentiator(a, b)}')