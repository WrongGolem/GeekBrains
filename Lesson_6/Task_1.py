status = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as search_1:
    for info in search_1:
        information = info.split(' ')
        bio = (information[0], information[5], information[6],)
        status.append(bio)

for i in status:
    print(i)
