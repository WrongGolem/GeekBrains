for unit in range(101):  # создание функции для перебора значения процентов
    if 11 <= unit <= 14:
        print(unit, 'процентов')
    elif unit % 10 == 1:
        print(unit, 'процент')
    elif 2 <= unit % 10 <= 4:
        print(unit, 'процента')
    elif 5 <= unit <= 100:
        print(unit, 'процентов')
