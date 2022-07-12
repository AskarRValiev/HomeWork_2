#2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

import math

n = input('Введите целое положительное число: ')
result = []
if n.isdigit() == False:
    print('Введенные данные не соответствуют услоиям')
    exit()
else:
    for i in range(1, int(n)+1):
        result.append(math.factorial(i))
print(result)