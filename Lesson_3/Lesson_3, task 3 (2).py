list_of_collegues = {}  # Содаем пустой словарь


def thesaurus(*names):  # Создаем функцию с условием *args
    for unit in names:  # Перебераем все аругменты
        if unit[0] not in list_of_collegues:  # Проверяем налиие ключей в словаре
            list_of_collegues[unit[0]] = unit  # Добавлем ключ и значение
        else:
            list_of_collegues[unit[0]] = [list_of_collegues[unit[0]],
                                          unit]  # Присваиваем к уже существующему ключу значение


thesaurus("Иван", "Мария", "Петр", "Илья")

print(list_of_collegues)
