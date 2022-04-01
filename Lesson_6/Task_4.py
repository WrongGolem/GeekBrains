import sys

status = {}

with open('users.csv', 'r', encoding='utf-8') as search_1, \
        open('hobby.csv', 'r', encoding='utf-8') as search_2, \
        open('personal_information.txt', 'w', encoding='utf=-8') as new_txt:
    for bio in search_1:
        hobby = search_2.readline().strip()
        if not hobby:
            hobby = None
        if bio not in status:
            status[bio.strip()] = hobby
        new_txt.write(f'{bio.strip()}: {hobby}\n')
    content = search_2.read()
    if content:
        sys.exit(1)
