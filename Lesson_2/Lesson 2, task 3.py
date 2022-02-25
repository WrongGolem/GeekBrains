origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5',
               'градусов']  # присваиваем название оригинальному списку
string_list = ''

for unit in origin_list:  # функция перебора в оригинальном списке
    if any(map(str.isdigit, unit)):  # функция определени наличия цифр в списке
        if len(unit) < 2:  # функция определения длины цифры
            string_list += ' "'
            string_list += '0' + unit
            string_list += '"'
        else:
            string_list += ' "'
            string_list += unit
            string_list += '"'
    else:
        string_list += ' ' + unit

print(origin_list)
print(string_list)