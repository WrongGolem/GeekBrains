import sys

status = {}

with open('users.csv', 'r', encoding='utf-8') as search_1, \
        open('hobby.csv', 'r', encoding='utf-8') as search_2:
    for bio in search_1:
        hobby = search_2.readline().strip()
        if not hobby:
            hobby = None
        if bio not in status:
            status[bio.strip()] = hobby
    content = search_2.read()
    if content:
        sys.exit(1)

with open('personal_information.txt', 'w', encoding='utf=-8') as new_txt:
    unit = ()
    for key in status:
        unit = f'{key} : {status[key]}\n'
        new_txt.write(unit)
