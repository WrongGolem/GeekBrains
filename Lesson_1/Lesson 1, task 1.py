duration = int(input())  # создание переменной для ввода пользователем

if duration // 86400 != 0:
    print(duration // 86400, 'дн', (duration % 86400) // 3600, 'час', (duration % 3600) // 60, 'мин', duration % 60,
          'сек')
elif duration // 86400 == 0 and (duration % 86400) // 3600 != 0:
    print((duration % 86400) // 3600, 'час', (duration % 3600) // 60, 'мин', duration % 60, 'сек')
elif duration // 86400 == 0 and (duration % 86400) // 3600 == 0 and (duration % 3600) // 60 != 0:
    print((duration % 3600) // 60, 'мин', duration % 60, 'сек')
else:
    print(duration % 60, 'сек')
