import sys

status = {}
f_name1 = sys.argv[1]
f_name2 = sys.argv[2]
f_name3 = sys.argv[3]
with open(f_name1, 'r', encoding='utf-8') as search_1, \
        open(f_name2, 'r', encoding='utf-8') as search_2, \
        open(f_name3, 'w', encoding='utf=-8') as new_txt:
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