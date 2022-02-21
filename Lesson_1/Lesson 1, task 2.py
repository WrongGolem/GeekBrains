# Вариация задания № 2 (без усложнения)
number_list = []  # создание списка №1
full_suma = 0  # создание переменной для суммирования результата

for unit in range(1001):  # функция перебирает все числа в обслати до 1000 и возводит в куб
    if unit % 2 != 0:
        number_list.append(unit ** 3)

for unit in number_list:  # функция перебирает все числа попавшие в список № 1
    suma = 0  # создание переменной suma ля следующей функции
    number = unit  #
    while unit > 0:  # функция производит суммирование каждого отдельного числа в каждом числе из списка № 1
        digit = unit % 10
        suma += digit
        unit = unit // 10
    if suma % 7 == 0:  # функция добавляет числа, сумма которых делится на 7 без остатка
        full_suma += number

print(full_suma)

# Вариация задания № 2 (с усложнением)
number_list = []
full_suma = 0

for unit in range(1001):
    if unit % 2 != 0:
        number_list.append(unit ** 3)

for unit in number_list:
    suma = 0
    unit += 17
    number = unit
    while unit > 0:
        digit = unit % 10
        suma += digit
        unit = unit // 10
    if suma % 7 == 0:
        full_suma += number

print(full_suma)
