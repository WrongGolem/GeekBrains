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
               'ten': 'десять'}  # создаем словарь


def num_translate(eng_num):  # создаем функцию для перевода
    """"Функция вызова перевода запрошенного числа, согласно словарю"""  # оставляем индексируемый комментарий
    if eng_num not in translation:  # условия поиска по словарю отсутсвующего элемента
        print('None')
    else:
        print(translation[eng_num])


num_translate("eight")
num_translate('two')
num_translate("eleven")
