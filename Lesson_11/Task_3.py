data_list = []


class Int_only(Exception):
    def __init__(self, data):
        self.data = data


while len(data_list) != 10:
    inp_data = input('Введите число: ')


    try:
        if inp_data.isdigit() == True:
            data_list.append(inp_data)
        elif inp_data == 'stop':
            print(f'Список чисел: {data_list}')
            break
        else:
            print('Вводить можно только цифры')
            continue
    except ValueError:
        continue
    else:
        print(f'Вы ввели число: {inp_data}. Для вывода списка введите: stop')
