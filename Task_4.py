# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time
rang = input('Введите диапазон случайного числа от 0 до 99: ')
if rang.isdigit() == False or int(rang) > 99:
    print('Введенные данные не соответствуют условиям')
    exit()

sec = str(time.time())
result = 0
if int(rang) <= 9:
    result = int(sec[13])
elif int(rang) <= 99 and int(sec[16]) >= 5:
    result = int(sec[12:14])
else:
    result = int(sec[13])

while result > int(rang):
    result = result - int(rang)

print(result)