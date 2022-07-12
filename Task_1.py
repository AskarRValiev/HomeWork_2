#1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def is_number(str): #проверка, являются ли введенные данные числом
    try:
        float(str)
        return True
    except ValueError:
        return False

n = input('Введите вещественное число: ')
if is_number(n) == False:
    print('Это не число')
    exit()
else:
    sum = 0
    for item in n:
        if is_number(item) == False: #отсекаем минусы и запятые
            continue
        else:
            sum += int(item)
        
print(f'Сумма цифр = {sum}')