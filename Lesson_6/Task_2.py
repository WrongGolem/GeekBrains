status = []
spammer = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as search_1:
    for info in search_1:
        information = info.split(' ')
        if information[0] not in spammer:
            spammer[information[0]] = 1
        else:
            spammer[information[0]] += 1

inverse = [(value, key) for key, value in spammer.items()]
print(f'Ip адресс {max(inverse)[1]} произвел запрос {max(inverse)[0]} раз')
