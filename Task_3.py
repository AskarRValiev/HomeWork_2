#3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = input('Введите целое положительное число: ')
result = []
if n.isdigit() == False:
    print('Введенные данные не соответствуют услоиям')
    exit()
else:
    dictionary = {}
    for i in range(1, int(n)+1):
        dictionary[i] = (1 + 1/i)**i
    
print(dictionary)