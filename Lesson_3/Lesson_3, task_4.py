list_of_collegues = {}  # Содаем пустой словарь


def thesaurus_adv(*names):  # Создаем функцию с условием *args
    for unit in names:  # Перебераем все аругменты
        temperate_list = {}  # Создаем локальный словарь
        unit = unit.split(' ')  # Производим разделение Имени/Фамилии для создания ключей
        if unit[-1][0] not in list_of_collegues:  # Проверяем налиие ключей в словаре
            temperate_list[unit[0][0]] = unit[0] + ' ' + unit[-1]  # Добавлем ключ и значение в локальный словарь
            list_of_collegues[unit[-1][0]] = temperate_list  # Добавлем ключ и значение в основной словарь
        else:
            temperate_list[unit[0][0]] = unit[0] + ' ' + unit[-1]
            list_of_collegues[unit[-1][0]] = [list_of_collegues[unit[-1][0]], temperate_list]


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print(list_of_collegues)
