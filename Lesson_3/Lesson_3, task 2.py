translation = {'zero': 'ноль',
               'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}


def num_translate_adv(eng_num):
    """"Функция вызова перевода запрошенного числа, согласно словарю и приведения её в соответствие с заглавной буквой запроса"""
    if eng_num[0].isupper() == True:  # проверяем первую букву строки на наличие заглавных букв
        eng_num = eng_num.lower()  # приравниваем переменне
        print(str.capitalize(
            translation[eng_num]))  # используем метод строк для установки заглавной буквы в знаении в словаре
    elif eng_num not in translation:
        print('None')
    else:
        print(translation[eng_num])


num_translate_adv('Eight')
num_translate_adv('two')
num_translate_adv("eleven")
