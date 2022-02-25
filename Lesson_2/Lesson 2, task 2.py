origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5',
               'градусов']  # присваиваем название оригинальному списку
secondary_list = []  # создаем пустой список

for unit in origin_list:  # функция перебора в оригинальном списке
    if any(map(str.isdigit, unit)):  # функция определения наличия цифр в списке
        if len(unit) < 2:  # функция определения длины цифры
            secondary_list.append('"')
            secondary_list.append('0' + unit)
            secondary_list.append(('"'))
        else:
            secondary_list.append('"')
            secondary_list.append(unit)
            secondary_list.append(('"'))
    else:
        secondary_list.append(unit)

print(' '.join(secondary_list))
